---
layout: post
title: "Simulating with SimPy"
author: "David Kraemer"
categories: ln 
tags: [programming,recursion,Python]
---

Discrete event simulation is *such a pain* to implement from scratch. The
basic premise---continuous simulations can be "discretized" by processing the
moments where the state jumps---is classic and well-trodden.[^1] But actual
implementation is a nightmare. In theory we want to have a number of features in
a discrete event simulation:

1. Versatile but general notions of events.
2. Centralized organization and handling of events.
3. Clear separation of the simulation specifics from the event handling.

There are some rather sophisticated design choices that need to be made
correctly in order to pull off a library meeting these criteria. Unfortunately I
don't have the time (or experience) to balance those trade-offs.

That's where [SimPy][SimPy URL] purports to enter the picture. According to
their project description,

> SimPy is a process-based discrete-event simulation framework based on standard
> Python. Processes in SimPy are defined by Python generator functions and can,
> for example, be used to model active components like customers, vehicles or
> agents. SimPy also provides various types of shared resources to model limited
> capacity congestion points (like servers, checkout counters and tunnels).

In a simulation, active components are called *processes*, which are managed by
the *environment*. The interaction between processes and environment is
encapsulated through *events*. The environment holds information such as the
simulation clock (which tracks the time---real or artificial---of the
simulation) and the event queue (which maintains scheduled events). 

The selling point of SimPy, in my limited view, is that it can easily "plug in" to
standard Python through its reliance on generators. SimPy processes are
constructed around pure Python generatorss. This means that you don't need a lot
of knowledge about the internal syntax of SimPy in order to write simulations.

## Motivating example

Let's work through the basic structure of a SimPy simulation with a simple
example: a Poisson process. I think that the simplest description of a Poisson
process is as counting the number of arrivals that are spaced by intervals of
iid exponential random lengths. Formally, given $$\lambda > 0$$, set $$X_0 :=
0$$, and let $$X_n \sim
\mathsf{Exponential}(\lambda)$$ be drawn independently for each $$n = 1, 2,
\dots$$ The Poisson process
$$N(t) \sim \mathsf{PoissonProcess}(\lambda)$$ is defined by

$$
N(t) = \max \left\{ n : \sum_{k=0}^{n} X_k \leq t \right\},
$$

In particular, we observe that $$N(0) = 0$$.
The parameter $$\lambda$$ is the *rate* of the process. It measures the average
number of arrivals over a unit of time.[^2]

Because the interarrival times of a Poisson process are iid exponential, we can
implement it in a very straightforward way in Python. To demonstrate that this
can all be done in pure (standard library) Python, we'll only use core libaries.

{% gist cf95d5be4b14da8b786ae937ab732799 simple_example_imports.py %}

The `bisect` module is a standard library implementation of a very general
bisection search, which we will use instead of reinventing the wheel. That's the
spirit of this whole post anyways.

Next, we can implement the arrival process.

{% gist cf95d5be4b14da8b786ae937ab732799 simple_example_arrival_process_no_simpy.py %}

Notice that we're setting this up as a generator (hence the `yield` keyword).
Each time `next()` is called, it produces the next arrival time. These arrivals
are computed using `random.expovariate`, which takes as the parameter the rate
of the exponential random variable.[^3]

Finally, we can write an implementation of the Poisson process, which keeps an
internal tracker of the arrival process.

{% gist cf95d5be4b14da8b786ae937ab732799 simple_example_poisson_process_no_simpy.py %}

The `poisson_process` function returns a Poisson process, i.e., a function
$$N(t)$$. It's a random function, so every time you create a new process you
will get a different "instance" of the Poisson process. But on any *given*
instance, the resulting function $$N(t)$$ is deterministic in time.

The only interesting implementation detail here is that the kernel `pp` is
"smart" in that it both (i) dynamically computes the values of the process as
specified by the parameter `time`, and that it (ii) memoizes the arrival times
so that the computation only occurs once. So eventually, `pp` is just a table
lookup function.

Let's analogize the Poisson process here to a discrete event simulation. First
off, the Poisson process itself is not really relevant---the arrival process is
what we care about. Viewed as a sequence of discrete events, the arrival process
is very simple. Each time an event (i.e., arrival) is processed, a new arrival
event is scheduled. This means there is always only one event in the (presently
nonexistent) queue at each step of the simulation. Also, the simulation clock
progresses by incorporating the interarrival information from the previous
event. And that's basically all there is to it.

## Incorporating SimPy

In view of the preceding discussion, the Poisson process---and in particular its
associated arrival process---is the simplest kind of sequence of discrete events
that would even justify being called a "simulation". If all we want to do is
study Poisson processes, then we don't really need to worry about event queues
and the like. Using SimPy here would be overkill.

On the other hand, there are a number of situations where even though we start
with a simple Poisson process, life quickly gets more complicated. For example,
in the standard [M/M/1 queueing system][mm1], the customer arrivals follow a Poisson
process. But once a customer arrives, she either (i) awakens the server and
begins processing  or (ii) waits in the queue until the server is free. This
means that the next event could be 

* a new customer arriving to the service queue (this is the Poisson process element)
* an earlier customer finishing service, causing the service queue to move
* our customer finishing service, emptying the service queue

Note that the service queue is *not* the event queue. With this in mind, it's
easier to appreciate how the complexity of discrete event simulation can
explode.

I want to write another post about modeling the M/M/1 queue in SimPy. This takes
advantage of a very useful feature built into the library: the "resource". For
now, let's just convert the arrival process into SimPy speak. We have to import
the library.

{% gist cf95d5be4b14da8b786ae937ab732799 simpy_example_imports.py %}

Now we turn to the arrival process with the SimPy ecosystem in mind. The first
change is that we customarily include the underlying SimPy `Environment` object
as a parameter to the process.

{% gist cf95d5be4b14da8b786ae937ab732799 simpy_example_arrival_process.py %}

Most importantly, the process no longer yields a simple value corresponding to
the next arrival time. Instead, it yields (in line 9) a `Timeout` object, which
is one of SimPy's core `Event` subclasses. The `Timeout` object is an `Event`
that, when executed, moves the simulation clock forward by a specified amount
(in our case, `interarrival`).

In addition, I added a `count` variable which tracks the total number of
arrivals. This isn't strictly necessary, but it's useful for the other novelty I
included. There is a `print` statement after the `yield` line. It gives the
arrival count as well as the arrival time at each step.[^4] Finally, notice that
the simulation clock can be accessed by `env.now`.

To see the code in action, we use the standard boilerplate for SimPy
simulations. 

{% gist cf95d5be4b14da8b786ae937ab732799 simpy_example_simulation_flow.py %}

Let's walk through this line by line. First, we instantiate a new SimPy
`Environment` object. This is what will handle all of the new events which are
created in the simulation. Next, we instantiate an arrival process connected to
this `Environment` object. The connection is explicit because we want to know
where the arrival process sends its new `Event` objects as it creates them.
Next, we create a preliminary `Process` `Event`. A `Process` is itself an
`Event`, although it amounts to the `Environment` running some arbitrary
procedure. More on this in a later post. In our case, we need a way to
jump-start the arrival process, which is why we do so explicitly here.[^5]
Finally, the main simulation is executed with the `env.run` call. This processes
the event queue until no more events remain. However, since in our case the
arrival process goes on forever, we can include a hard stopping time by
specifying an alternative `until` keyword parameter. Here we are saying, "if the
event queue isn't empty by time 20, terminate anyways."

Here's some sample output of the simulation:

```
arrival   1 at time  2.75
arrival   2 at time  3.11
arrival   3 at time  5.34
arrival   4 at time  5.60
arrival   5 at time  6.72
arrival   6 at time  8.18
arrival   7 at time  8.50
arrival   8 at time  8.82
arrival   9 at time 10.25
arrival  10 at time 10.49
arrival  11 at time 11.29
arrival  12 at time 12.64
arrival  13 at time 17.39
arrival  14 at time 17.77
arrival  15 at time 18.34
arrival  16 at time 18.40
arrival  17 at time 18.71
arrival  18 at time 19.40
arrival  19 at time 19.42
arrival  20 at time 19.77

```

This is simply the output of the `print` statement included in the
`simpy_arrival_process` definition. Notice that the last arrival occurs at
time 19.77, which is a good indication that the event queue is interrupted at
time 20, as we requested.[^6]

The point of this example is to show that, at least for simple simulation
problems, porting to SimPy is pretty straightforward. There's a little bit of
boilerplate code, and there is one important change to the underlying process
generator, but otherwise it's basically pure Python.

A little bit about the `Timeout` object (created in line 9 of
`simpy_example_arrival_process.py`): SimPy `Event` subclasses have a number of
different functions. The `Timeout` *suspends* the execution of the Python
generator in which it is yielded, and it *schedules* the generator's resumption
to a moment in the future. This is specified by the `delay` paramater, which
tells the `Environment` when it will be executed (that is, where it is placed in
the event queue). If the underlying generator has a natural finite termination
(e.g., a generator for all primes less than 100), then eventually this "loop" of
`Timeout` constructors will stop on its own. In our case, the generator never
terminates, so each round of execution schedules a new `Timeout`.

There is a lot more to say, and a lot more to show, regarding SimPy. But since
we've gotten a (very) minimal example working, I'll leave it here.

#### Notes


[SimPy URL]: https://pypi.org/project/simpy/
[mm1]: https://en.wikipedia.org/wiki/M/M/1_queue
[^1]: It even has its own [Wiki](https://en.wikipedia.org/wiki/Discrete-event_simulation).
[^2]: This can be seen by the interpretation of $$\lambda$$ as the rate parameter of the exponential random variable. In that case, since $$E[X_n] = \lambda^{-1}$$, we can say "on average, one lifetime is $$\lambda^{-1}$$ units". The inversion of this statement is a rate interpretation.
[^3]: Be warned, NumPy users: `np.random.exponential` uses the *scale*, not the rate, parameter in its definition. To go from one to the other simply take reciprocals.
[^4]: Why does the `print` happen after the `yield`? It's a bit of a hack, I agree. Basically, it avoids printing the "0th arrival" by waiting until the *second* arrival event before printing anything at all. I would be more careful about this in real-life code.
[^5]: An alternative implementation using classes can avoid this line in the simulation flow by including it in the class `__init__` method. I will try to show this in a later post.
[^6]: Also note that 20 arrivals in 20 units of time is exactly $$E[N(20)]$$ when $$\lambda = 1$$, which is a neat coincidence.
