---
layout: post
title: "Reflections on the first year of graduate school"
author: "David Kraemer"
categories: ln 
tags: [math,school,introspective]
---

## Courses

Probably the biggest transition from the undergraduate (and particularly,
liberal arts) experience and graduate work became apparent in the courses I
took. Generally speaking, I never had a class with more than 30 students in
college. Here, the norm has been (with one exception) *at least* that many. 

I've found it harder to engage with the professors in larger environments. I
discovered that, as the class size increases, the barriers to participating
become stronger. I think barriers come in two forms. First, it simply is harder
to get your question asked, given that there are many more students who may also
have questions. More nefariously, I felt that with more students, the "stakes"
were somehow higher. If I asked my question, the interruption would affect more
students. And if, after the fact, it didn't have the relevance or urgency that I
believed it did, then I would feel guilty for having wasted the other folks'
time.

I think the essential difference is that with a small class, there is a much
stronger potential for having a collegial experience. That is, when you are with
the professor and a handful of other students, the social dynamic requires that
you behave differently: somewhat informal, participatory, and with more
sustained back-and-forth discussions. Moreover, these behaviors are *productive*
in that they facilitate learning. 

When the class becomes larger, however, these same behaviors suddenly feel
emphatically unproductive. Your best strategy seems to devolve into soaking
every moment of the lecture up like a sponge and process it all much later. By
the way, this *really* doesn't work when the lecturer is awful, which was my
experience in two separate classes.

## Professors

The professors at a research university are here to do research. Some also
believe in the importance of their roles as teachers, but not all. This is not a
new insight, but it is strongly supported by my experience. I have much stronger
admiration for the professors who make an effort in their lectures, even when
they don't fully succeed, than the many who visibly put negligible thought into
pedagogy.

I also find that the experience of talking to professors is a bit of a roulette
game, depending on how they receive your interests and ideas. Whereas in
college, the underlying concern is for my curricular success, this is not always
true in graduate school. This is not necessarily bad, but it is certainly
different.

## Research

Starting in a new field is very intimidating. Research articles are not written
for initiates, and frequently the topic's textbook does not exist (because
otherwise would it truly constitute research?). Reading and rereading, taking
notes, and keeping a healthy sleep cycle have been my best tools in scaling this
hill. But I can't speak to research much after this year's work,
because course work simply dominated the bulk of my mental effort.

## Projects

I had a couple of small software projects in my first semester, none of which
were (designed to be) particularly challenging. In the second semester, I worked
on two substantial projects in computational geometry and convex optimization
which came to a somewhat reasonable conclusion.

Besides the interpersonal fun that is always involved in a nontrivial group
project, I found it interesting to discover what distinguished the "easy" and
the "hard" parts of a project. Essentially, the "easy" part is the part you've
done before, and the "hard" part is the part you've never encountered.

That sounds obvious. But what I mean is the parts that actually take up most of
the effort of the project may have nothing to do with what is difficult or
simple in the abstract. Two examples illustrate this. 

In computational geometry, I implemented certain measures of simple polygons in
C++. I expected that implementing the measures would be the most challenging
part, since they were new ideas and since I couldn't know for certain that the
implementations were working. But, relative to the total time spent working on
the project, I spent very little time writing the code for the measures. (I
proved some basic results about the measures and checked that the
implementations conformed, so I was reasonably happy with their correctness.)
But I spent the vast majority of my work time dealing with the intricacies of
the floating point arithmetic kernels provided by the CGAL project, futzing with
Makefiles, and linking external dependencies.

In convex optimization, I implemented a new optimization algorithm so to be
compatible with a major machine learning library. I expected that the algorithm
itself would be the biggest obstacle. (To be fair, it was quite hard writing it.
But it was "correct" and still failing for far longer than we had realized.)
Actually, our work time was dominated by reading shoddy documentation and sparse
discussion threads, studying existing library code, and periodically scrapping
everything we had compiled so far.

For both cases, the project involved learning a component of a new library so
that our code would properly interact with it. Unlike writing pure software,
which I now have a few years' experience with, working inside (and extending)
existing projects was a brand new problem for me. As a consequence, it ate up
the vast majority of my time.

## Work-life balance

I commuted to school all of first year, but because my girlfriend and I share a
car, this ended up meaning I had rigid drop-off and pick-up times. In one
respect this was great: it forced me to adopt the discipline of getting up early
(circa 6:25am). In other respects, it was very challenging. In college I could
use the campus to work far into the morning hours as the coursework demanded.
But this year I was very much constrained by a 7am-4pm cycle. 

Now that I live within walking distance to campus, I expect this cycle to relax
a bit. I can attend more talks and workshops without any major scheduling
crisis, and I can use the libraries or work with colleagues as needed. 

The upside to this year's schedule was in forcing a better work-life balance. I
ate dinners at reasonable times. I took breaks from studying. I interacted with
other human beings (i.e. my girlfriend) socially. I don't want to lose these
things, although I think the future demands of my program may require I scale
them back from time to time.

## What is applied math

Coming into this year, my working definition of applied math was: *mathematical
answers to questions arising outside of math*. By contrast, I defined pure math
as: *mathematical answers to questions arising inside of math*. 

I really like this definition, but I suspect this is not quite accurate. Applied
math, as I have learned this year, is a broader field than the definition
permits. In the fall, I started out studying numerical solutions to differential
equations. Of course there is mathematics at play here, but there is just as
much physics motivating the solutions. High performance computing is classified
by some as an applied math field. It's not obvious to me that the
theorem-proving, which lies at the heart of pure mathematics, is as central in
these areas.

Though I haven't been able to revise the definition in light of these new
experiences, I hope to stay *personally* in an area of applied math that meets
my old criterion. It's still early, but so far it seems like a good possibility.

