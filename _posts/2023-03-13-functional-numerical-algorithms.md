---
layout: post
title: "Functional programming for numerical algorithms"
author: "David Kraemer"
categories: ln
tags: [analysis, functional-programming, Python]
---

I've always been attracted to the functional programming (FP) paradigm, in part
because it's how I [started out writing code](https://weinman.cs.grinnell.edu/courses/CSC151/2014S/), in part because of my
mathematical [tendencies](https://xkcd.com/1270/). To be sure, I'm not a FP
purist. I think this is one of the benefits of learning a language like Scheme:
while the language is designed to make you adopt FP ideas, it never *forces*
you to. The more juvenile discussions of FP online tend to devolve into
squabbles over purity, and I think this largely misses the point about the
value of the paradigm.

When I get to write code these days, it's almost always in Python. Python is
a fabulous example of the virtues of pragmatism in language design. For
instance, I doubt there exist high-minded philosophical justifications to make
`len` look like a function instead of a method, but the choice seems to be
a good one! Python abounds with compromises like this, and it has relied on the
good sense of its designers to rise steadily in popularity.

With that said, Python makes writing pure FP pretty difficult. The most famous
obstacle is the [lack of tail-call
elimination](http://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html).
On the other hand, Python treats functions as first-class objects, which means
that the kinds of bread-and-butter abstractions of FP are at least
*expressible* in it. If we're willing to sacrifice purity, then Python does
just fine.

For me, the most attractive conceptual innovation of FP is the *stream*, which
allows a program to evince the same sequential evolution as a more procedural
counterpart while avoiding major pitfalls in mutating state[^1]. There is a lot
to be said about the strength of stream programming, but I will just point out
that it rather elegantly and efficiently handles computation on infinite data
structures without much effort. Streams are so useful that Python lets us build
them natively! Python
[generators](https://realpython.com/introduction-to-python-generators/) are one
of those language features that really should be introduced to students early
on, but in my experience they are usually get skipped.


# Newton's method in procedural style

I took an introductory numerical analysis class in undergrad using MATLAB, and
then another in grad school using C++. We covered a range of topics in no
particular depth, but the algorithms we implemented were always presented in
procedural fashion. To be sure, every standard algorithms class is procedural
first[^2], but it's much harder to find good examples of equivalent FP
implementations of numerical methods. As far as I can tell, this is mostly a custom[^3].

Let's see what a numerical method might look like implemented with FP
principles. Again, I'm not a purist, but I want to see how the stream paradigm
can be leveraged to write clean implementations of classic numerical
algorithms.  Many such algorithms are essentially routines to compute
a sequence

$$
x, \phi(x), \phi(\phi(x)), \phi(\phi(\phi(x))), \phi(\phi(\phi(\phi(x)))), \ldots
$$

where $$\phi$$ represents an iterative step. For example, Newton's method for
finding the minimum of a differentiable function $$f : \mathbb{R} \to
\mathbb{R}$$ amounts to repeating the iteration

$$
x_{k+1} = x_k - f(x_k) / f'(x_k)
$$

until a suitable termination condition has been met. A typical implementation
might look like this:

{% gist 60b36656165ea652b79de7e9141fc2f7 newton_method_v1.py %}

I've seen implementations of Newton's method essentially of this type in the
wild as well as in courses. It's fine, and it's easy to read, but let's
critique the implementation anyways.

* The main iterative step, `x -= f(x) / df(x)`, is a procedural idiom. To be
  sure, there is no ambiguity to what this step does, and unless `f` itself
mutates state somehow, I wouldn't really consider this a problem in a real
algorithm. But it's worth flagging.
* We have a `break` statement to handle the termination condition, which gives
  off a faint code smell.
* We haven't (yet) dealt with the possibility of an infinite loop under
  a situation where the algorithm fails to find a root.
* More seriously, we might question whether putting the iteration and
  termination logic together in the same code block is wise[^0].

Our Newton's method implementation is relatively simple, so the severity of
these criticisms is muted. But, hey, it's a blog post. Let's see what an
improvement might look like, provided that we still adhere to procedural style.

{% gist 60b36656165ea652b79de7e9141fc2f7 newton_method_v2.py %}

The primary difference between versions 1 and 2 is that the latter uses the
control flow of the `while` loop to explicitly monitor the termination
conditions. We have also added the circuit breaker parameter `max_iter`, which
prevents an infinite loop.

In full honesty, this implementation seems pretty nice. While avoiding code
smells, the loop has fully separated the iteration and control components of
the algorithm. We might complain that `f(x)` is computed twice per iteration,
which is needless computation, but for the most part this looks good.

# Newton's method, functional style

Let's see what we can do to apply FP principles to implement Newton's method.
A functional programmer's main design patterns are higher order procedures
(HOPs), such as `map`, `filter`, `apply`, and `reduce`. Now, Newton's method is
a special case of the iterative rule $$x_{k+1} = \phi(x_k)$$ mentioned above.
This scheme is so general that we should instantly recognize the value in
providing a HOP abstraction for it. Our goal is to write a function, `iterate`,
which takes a function and an initial argument and produces a stream of
iterations. Using Python generators, this can be pretty straightforward:

{% gist 60b36656165ea652b79de7e9141fc2f7 iterate_v1.py %}

The trouble is that the line `x = f(x)` is not very functional; rather, it has
the same procedural flavor as above. I would not be against compromising FP
principles here, because the code is readable, serves as a nice application of
the stream concept, and as an HOP, integrating `iterate` into other algorithms
as-is makes separating iteration logic from control logic very straightforward.
But this is a blog post, dammit! Let's go all the way. Here is an
implementation of `iterate` I stole from Joel Grus's PyData 2015 talk,
["Learning data science using functional
Python"](https://www.youtube.com/watch?v=ThS4juptJjQ).

{% gist 60b36656165ea652b79de7e9141fc2f7 iterate_v2.py %}

Let's elaborate on how this works.

1. `itertools.repeat` takes an input and produces a generator that yields the
   input back indefinitely. So `repeat(x)` produces the stream `(x, x, x,
...)`.
2. `itertools.accumulate` takes an input stream and a binary operator (called
   the *accumulator*) and produces the stream of "partial" reductions as we
step through the inputs.  So, for example, `accumulate(repeat(1), lambda sofar,
nextval: sofar + nextval)` produces the stream `(1, 2, 3, ...)`, because the
input stream `(1, 1, 1, ...)` is accumulated by the provided function through
adding the next value (i.e., 1) to the current total so far.
3. In our case, we are performing a clever[^5] trick with our accumulator. We
   are simply *ignoring* the next value of the input stream and
instead apply the function `proc` to the current accumulation.

The result is the sequence `(x, proc(x), proc(proc(x)), ...)` as desired.

To apply our `iterate` HOP to Newton's method, we just need to define
a suitable `proc`. The code is given below:

{% gist 60b36656165ea652b79de7e9141fc2f7 newton_method_v3.py %}

We provide the anonymous function that maps an input `x` to its Newton update
`x - f(x) / df(x)` to the `iterate` function, which allows us to loop directly
through the stream produced by Newton's method. Inside the loop, we check the
termination condition and return when satisfied. Note that we haven't dealt
with the maximum iteration circuit breaker yet. I'm somewhat amused by the fact
that we've flipped the conventional structure of loops upside down. Now, all of
the iteration is happening before the colon, while all of the control is
handled by the body of the loop! But again, I think the crucial observation is
that we have completely separated iteration from control logic. Furthermore, we
now have the ability to reason about the execution of our algorithm from the
stream paradigm, which will pay off handsomely in time.

Let's deal with the circuit breaker now. The main idea is to employ `zip`,
another HOP, to combine our iteration HOP with Python's built-in `range`
function. When combining iterables of different sizes, `zip` will always stop
when the first iterable is exhausted[^6]. This comes in handy if we want to
enforce a maximum iteration condition with an infinite stream: simply `zip` our
stream with `range(max_iter)`. In fact, this kind of circuit breaker pattern is
*so* common that it's worth implementing this idea directly on the `iterate`
HOP. So we get what I call `circuit_breaker`, which returns pairs in the spirit
of the `enumerate` function:

{% gist 60b36656165ea652b79de7e9141fc2f7 circuit_breaker.py %}

Creating compound generators is a really neat idea.  Putting this into our
Newton method gives us a final version of our FP implementation.

{% gist 60b36656165ea652b79de7e9141fc2f7 newton_method_v4.py %}

# Implementation comparison

The downside to FP, from a practical perspective, is efficiency (both runtime
and memory). Very clever people have worked very hard to minimize this reality,
but in any event the Python programming language is not at the vanguard of
optimization tricks to make FP viable as a paradigm. Let's perform a very
simple comparison between our procedural and functional implementations of
Newton's method to see how fast they are at computing $$\pi$$. We know that the
sin function has a root at $$\pi$$, so we'll give Newton's method the inputs

```Python
f = math.sin
df = math.cos 
x0 = 2.
tol = 1e-8
max_iter = 1000
```

and see how each does. I'm not interested in a very thorough analysis of the
difference here, so I'll just pass three different configurations of our
Newton methods to the `%timeit` magic function:

1. the final procedural style implementation,
2. the final FP style implementation with our
   straightforward-but-purity-compromised `iterate` HOP,
3. the final FP style implementation with Joel Grus's `iterate` HOP.

| version | `%timeit` report |
|:--|:--|
| Procedural | 1.39 µs ± 76.3 ns |
| FP, naive `iterate` | 2.35 µs ± 1.35 ns |
| FP, Grus's `iterate` | 2.76 µs ± 25.2 ns |

In short, FP absolutely takes more runtime to perform the same task.
Disappointing!

# Procedural in the streets...

It's not a death knell for FP solutions to numerical problems, however. The
question on whether to use FP in numerical methods revolves around whether the
purported benefits of FP justify the extra runtime cost. What, then, might
count in favor of a functional approach? I can see two offhand:

* **Immutability**. Notice that the FP implementation of `newton`, together with
Joel Grus's fancy `iterate`, involve *zero* mutations of state. This is
a highly enviable situation for a variety of reasons. It bears mention that
debugging a program that adheres to a principle of immutable state is a million
times easier than debugging mutated code[^7]. This is because reasoning about
immutable data allows us to justify mental heuristics such as the "substitution
model" of computation, which repeatedly fails when there is mutated data.
* **Modularity**. In our `newton` implementation, the parts of the code that deal
with the iteration of the algorithm are entirely separate from the bits that
deal with termination. The extent to which we can guarantee this separation is
the extent to which we can delegate work across a team, trust unit tests, or
refactor.

The success of the Python language demonstrates, to some extent, that the
ability to *write* code quickly frequently matters more than the ability to
*execute* code quickly. I don't anticipate Pythonic, FP implementations will
replace state-of-the-art codes in the near future, but as I will continue to
argue in this blog, FP ideas remain underrated in numerical analysis.


[^0]: This is the kind of thing that makes reading deep reinforcement learning code painful. It's hard to tell the difference between the iteration and the control!
[^1]: See Section 3.5 in Abelson et al. *Structure and Interpretation of Computer Programs*, which provides a careful introduction to this topic.
[^2]: My undergraduate algorithms course used Cormen et al. *Introduction to Algorithms*, which was typically blasé about the perils of mutable state. *You* try implementing a red-black tree and tell me I'm exaggerating!
[^3]: To wildly speculate based on anecdata, my guess is that numerical methods are studied by applied mathematicians and engineers, who are far less interested in programming paradigms than other folks.
[^5]: *Too* clever, in Grus's opinion!
[^6]: See [itertools.zip_longest](https://docs.python.org/3/library/itertools.html#itertools.zip_longest) for an implementation of `zip` that cycles through the shorter iterables until the longest is exhausted.
[^7]: Implementations of numerical methods are *notoriously* hard to debug, and academic researchers are *notoriously* bad at reasoning about them.  A mathematics professor once told me that he couldn't be bothered testing his state-of-the-art compressed sensing softare: "it either breaks entirely, or it's right". A Herculean effort prevented me from laughing right in his face. 
