---
layout: post
title: "Sliding down pyramids in Python"
author: "David Kraemer"
categories: ln 
tags: [programming,recursion,Python]
---

When I studied computer science in college, I often enjoyed thinking about
algorithms and data structures in quite "abstract" settings. To be clear, I
don't mean that I particularly preferred problems on arcane objects over those
with more immediate practical relevance. Rather, I was quite happy to work above
the level of concern for the implementation details involved in converting my
solutions into code. There's a simple&mdash;if embarrassing&mdash;reason for
this: I come up with ideas in "natural language," which absolves me from having
to describe their contours precisely and, as a result, grapple with and fix
their ambiguities. It's a kind of lazy mental evaluation that is useful when
brainstorming for the high level insights but useless when it's time to sit down
and actually write some code. I know I'm not alone here.[^1] 

On the other hand, I do enjoy working through the details of a problem I think I
have solved "abstractly". I'm just not very good at it.

Nowadays, when the majority of my time is spent on mathematics research, I have
very little to give to programming. It's understandable, but still a shame. One
of my grad school goals is to remain a reasonably competent programmer, so I try
to keep a foot in the algorithms world. As I've said, however, the problem is
not simply staying engaged in algorithms problems but getting involved in
writing code. 

In one ideal world, I would find an open source project to contribute to. But
that world ignores the start up costs involved with getting started there, let
alone a few healthy (well, unhealthy) doses of imposter syndrome that comes a la
carte with them. The other world would involve coming up with my own projects
and seeing them to fruition, but that requires a level of discipline and a trove
of good ideas which are not at my disposal.

Enter [Codewars](https://codewars.com), a free site for programmers to practice
their skills on a wide range of problems. Codewars follows the philosophy of
code kata[^2], which borrows from a concept in many Japanese martial arts that
emphasizes repeated practice of patterns of movement. A code kata begins with a
programming prompt, usually with open-ended solutions. The solutions themselves
are differentiated along two different axes. The first, broadly speaking, is
algorithmic complexity (e.g., does your solution require exponential running
time when a quadratic time alternative exists?). The second, which can subtly
interact with the first, is language and idiom tools (e.g., Pythonic versus
Julian, functional versus iterative). By repeatedly solving the same problem in
different languages using different approaches with different complexities, you
gain an appreciation for the best ways to solve problems in different language
or paradigms.

I've found Codewars to be a good compromise between these two worlds, as I am
solving self-contained but challenging problems provided by the community. They
are self-paced and relatively free form, and after solving a given problem in a
specific language, you can compare your approach with others in the community.
I've learned many important Python standard library features by studying the
best-voted solutions to a problem I've solved, for example.

The other day I encountered a lovely kata whose solution involved a neat trick
to avoid awful runtime complexity but also required some subtle use of data
structures to implement. I ended up solving it in Python, and wanted to describe
my process for developing a solution. There were many hiccups along the way!

## Pyramid Slide Down ##

I've copied the text of the kata prompt in full. The original is available 
[here](https://www.codewars.com/kata/pyramid-slide-down`).

## Lyrics... Pyramids are amazing! Both in architectural and mathematical sense.

If you have a computer, you can mess with pyramids even if you are not in Egypt
at the time. For example, let's consider the following problem. Imagine that you
have a plane pyramid built of numbers, like this one here:

       /3/
      \7\ 4 
     2 \4\ 6  
    8 5 \9\ 3

### Here comes the task...
Let's say that the '*slide down*' is a sum of consecutive numbers from the
top to the bottom of the pyramid. As you can see, the longest '*slide down*'
is 3 + 7 + 4 + 9 = 23

Your task is to write a function `longest_slide_down` that takes a pyramid
representation as argument and returns its' longest '*slide down*'. For example,

    longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]])
    # => 23

### By the way... 

My tests include some extraordinarily high pyramides so as you can guess,
brute-force method is a bad idea unless you have a few centuries to waste. You
must come up with something more clever than that.

(c) This task is a lyrical version of the Problem 18 and/or Problem 67 on
ProjectEuler.

# My first try

The data type of `pyramid` is simply a list of lists, albeit a special one. In
particular, the first list in `pyramid` is a singleton, and each subsequent list
contains one more element than before. For consistent terminology, let's call each
list in `pyramid` a "tier" and each element in a tier a "brick". Now, a "slide"
is a selection of one brick in every tier according to a certain movement
constraint&mdash;the slide can't "jump" across bricks. Let's revisit the
original diagram:

       /3/
      \7\ 4 
     2 \4\ 6  
    8 5 \9\ 3

Here, it's permissible for `3` to slide down to `7`, which we understand is a
"left turn." It's also permissible for `7` to slide down to `4`, which we
understand is a "right turn." How does this translate to our model with lists?
Let's rewrite the diagram so that each entry is the brick's index in its tier,
rather than its value:

        0 
       0  1 
     0  1  2  
    0 1  2  3

From here, we can see that the index of the "left turn child" is exactly the
same as the parent index, whereas the "right turn child" index is exactly one
more than the parent index.

Okay, let's think about solving the actual problem now. The diagram strongly
resembles a tree, so thinking recursively could be a good bet. (Full disclosure:
I strongly prefer recursive solutions, so while it is true that recursion and
trees pair well together, it's *also* true that I decided to pursue a recursive
solution before I began to analyze the problem. What I'm trying to say is that I
like recursion and motivated reasoning :wink:). 

Suppose we found ourselves with a pyramid that looks like this:

         9

This is a great pyramid. It's very easy to say what the longest slide down is.
So if we manage to get to the bottom of the pyramid, our recursion should just
return the value of the brick we land on.

If we're not on the bottom of the pyramid, we have to make a decision. Do we
choose our left child or our right child? To answer that, we can descend both
children, determine their longest slide downs respectively, and select the
bigger one to follow. Indeed, this will be our recursive step. After we've
selected, we add the value of the brick we are currently occupying and return
the result.

Here's the gist of what I've just discussed:

{% gist  bb52b7245e6335900e5db08a41e2fca9 naive_slide_down.py %}

Introducing the helper function `kernel` is a useful trick I learned from way
back when in my Scheme days.[^3] It's far more convenient to search through the
pyramid with explicit access to the current tier and brick, so if we use
`kernel` to track these values while simultaneously computing the longest slide,
we're hitting two birds with one stone. The drawback, as far as I can tell, is
that helper functions are not particularly Pythonic. Python is not, after all,
the most recursive friendly language, and helper functions of this sort are part
and parcel of the recursive paradigm. Nevertheless, they offer elegant
solutions, and our problem is not so critically important to merit a rewrite.

How does `longest_slide_down` perform? Let's test that by implementing some
auxiliary functions.

{% gist  bb52b7245e6335900e5db08a41e2fca9 print_pyramid.py %}

This function takes a `pyramid` and prints it out nicely enough to read. The
inside of the `print` call is an important Pythonic pattern: `" ".join(lst)`
takes a list of elements and produces a string of every element separated by the
`" "` string. In particular, we pass it a list of string formats. The string
`"{:4d}"` can be formatted by an integer with four leading padding digits. After
the string is formed, we use the tier itself to fill in all of these formats
with brick values.

As an example, we have 

```Python
In[1]: print_pyramid([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]])
Out[1]: 
   3
   7    4
   2    4    6
   8    5    9    3
```
using the pyramid provided by the problem. Let's call this `pyramid1`. It has
a longest slide down value of 23. The kata also specifies the pyramid

    75
    95   64
    17   47   82
    18   35   87   10
    20    4   82   47   65
    19    1   23   75    3   34
    88    2   77   73    7   63   67
    99   65    4   28    6   16   70   92
    41   41   26   56   83   40   80   70   33
    41   48   72   33   47   32   37   16   94   29
    53   71   44   65   25   43   91   52   97   51   14
    70   11   33   28   77   73   17   78   39   68   17   57
    91   71   52   38   17   14   91   43   58   50   27   29   48
    63   66    4   68   89   53   67   30   73   16   69   87   40   31
     4   62   98   27   23    9   70   98   73   93   38   53   60    4   23

which has a longest slide down value of 1074. Let's call this `pyramid2`.  We
can also generate random pyramids with the following function.

{% gist  bb52b7245e6335900e5db08a41e2fca9 generate_random_pyramid.py %}

The downside with randomly generated pyramids is we don't know *a priori* what
the correct answer should be. Nevertheless, we will find it useful later on when
evaluating performance. 

After running `longest_slide_down` on `pyramid1` and `pyramid2`, we do indeed
obtain 23 and 1074. But I was disheartened to watch it slow down like crazy on
`pyramid2`. I mean, it's only 15 tiers tall. Anyways, it's giving correct
answers, so let's see what happens when I run it on the hidden test set for the
kata...

...and the server times out before completing. 

Okay, the hidden tests must be using bigger pyramids, and the solution we have
at the moment is not scaling well. Hmm.

# Complexity pains 

I like to imagine that the kata prompt is laughing at me right now:

> My tests include some extraordinarily high pyramides so as you can guess,
> brute-force method is a bad idea unless you have a few centuries to waste. You
> must come up with something more clever than that.

Clearly, they expected us to fall in this trap and tried to warn against it. But
in our hubris we thought we could get away with a naive solution!

Just how naive is our `longest_slide_down` implementation? Suppose we have a
pyramid of height $$ n $$, and denote $$ f(n) $$ the execution time of
`longest_slide_down`. If $$ n = 1 $$, we have a singleton pyramid, and our
execution time is a constant $$ O(1) $$ process. Otherwise, we perform two
recursions and an extra computation. That's summed up in this recursive formula:

$$
f(n) = 2f(n-1) + O(1)
$$

If you squint very hard, you will see that this recursion unfolds into the
following explicit expression:

$$
\begin{align}
f(n) &= \sum_{k=1}^{n-1} 2^{k} O(1) \\
&= O(1) \cdot (2^n - 1).
\end{align}
$$ 

<!--_ -->

Wow, so the naive approach outlined above has exponential time complexity. That
explains a lot.

We'll have to do better than exponential if we want any hope of scaling up the
solution to any reasonably-sized problem. Back to the drawing board...

# Bottoms-up, greedily

The problem, as I see it, is that we don't have good information when we are at
the top of the pyramid. By contrast, we can speak concretely about the best
choice&mdash;the only choice&mdash;on the bottom. Currently, we're starting at
the top and waiting (very patiently) for the best choice to bubble up. But each
step down the pyramid is like another mini-pyramid. In order to get the best
choice for the top, we have to wait for the best information about all of the
second tier's bricks, and so forth. It would be great if we could instead
propagate our best choice information upwards.

Okay, so suppose we're on a slide that has brought us to a particular brick of
the penultimate tier. Let's imagine that every move we've made so far has been
optimal, and now we want to decide how to finish the slide. Our choice is either
to go left or go right. How do we proceed? Well, if the left child brick has a
bigger value than the right child, we would be wasting valuable bricks if we
went right! We definitely should choose left. 

That was for an arbitrary brick on the penultimate tier, but this idea certainly
works for *all* of the penultimate bricks. If we've made it this far, no matter
where we've landed, we can make an optimal decision by simply picking the
greatest-valued child brick.

We've just improved from having optimal information about the bottom tier to
having optimal information about the penultimate tier, but can we keep going? 

Yes: suppose we're on any tier. We now know the optimal slide (and as such, the
longest slide score) possible for every brick on the proceeding tier.  Our
choice is now the same. Given that we are on a particular brick, and given that
we have full knowledge about the proceeding tiers, we look at the slide down
scores available by the brick's children. Choosing the child with the higher
score ensures that the slide will be optimal *from our brick onward*. 

Propagating this fact upwards, we can select the longest slide down by simply
choosing whichever child from the top of the pyramid has a bigger score. Neat!

I think this qualifies as a greedy algorithm in the sense that every step in the
procedure is making decisions about local optima. But by our above discussion,
all of the local optima accumulate upwards into one global optimum.

Best of all, we've just made an enormous performance improvement. Our new
approach visits each brick in the pyramid to perform constant time processing.
On a pyramid of height $$n$$, that corresponds to $$O(n^2)$$ complexity.

# Implementation fun

We now have a substantially better algorithm for finding the longest slide down
of a pyramid. Are we on the home stretch yet? I guess it depends how capable we
are at converting our ideas into formal language. Let's find out!

Our new approach starts at the bottom, which means that the base case of our
recursion is at the top. If we play our recursion cards right, the longest slide
down information should propagate upwards. We'll accomplish this by imagining
that we can "look up" and decide the longest slide down for the parent bricks of
our current tier. But in the base case, there are no parents of our tier, so the
longest slide down should be known already. In that case, we can just return the
information we have.

As before, we'll write a helper function called `kernel` that tracks the current
tier we are processing. But we'll also need to track all of the available
longest slide down slides as well. More on that later. For now, we'll just assume
that `kernel(tier, slides)` is our signature. The data structure we use for
`slides` can be decided once we have more info about our needs.

We've just described what we need to do in the base case. If we're at the top
tier, return the only available slide down. So our snippet should resemble 

{% gist  bb52b7245e6335900e5db08a41e2fca9 kernel_base_case.py %}

Even though there's only one possible slide remaining, it seems reasonable to
assume that `slides` will have `__getitem__` implemented. After all, the lower
tiers will all have a collection of slide down values, not just one. We don't
know what data structure `slides` will need to be to account for the rest of the
tiers yet, but we've just narrowed it down a bunch.

Okay, next let's do the recursive step. We need to imagine that we've just
arrived at a new tier, and that we know the longest slide down from every brick
of our tier. Then our remaining work is to compute the longest slide down
for our parent tier. 

Before proceeding any further, we have to resolve a potential problem: do we
know that the children paths are accessible?

# Retrospective


[^1]: Relevant [xkcd](https://xkcd.com/568/)
[^2]: Wikipedia [reports](https://en.wikipedia.org/wiki/Kata_(programming)) that the origins of the term are ambiguous, with the first known usage in Andrew Hunt and David Thomas' *Pragmatic Programmer* (1999). Thomas has a whole [site](http://codekata.com) dedicated to code kata, with an explanation of its utility [here](http://codekata.com/kata/kata-kumite-koan-and-dreyfus/).
[^3]: The introduction to computer science course I took at Grinnell has an interesting [article](https://www.cs.grinnell.edu/~weinman/courses/CSC151/2014S/readings/helper-recursion-reading.html) on helper procedures, if you can stomach all of the LISP parentheses. Which you should, by the way, LISP languages are beautiful.
