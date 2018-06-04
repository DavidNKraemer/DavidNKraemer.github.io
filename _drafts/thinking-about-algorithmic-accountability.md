---
layout: post
title: "Semantics for algorithmic accountability"
author: "David Kraemer"
categories: ln 
tags: [computer science, data, algorithms, news, policy]
---

As someone who uses and, from time to time, designs algorithms for varied
purposes, I am bemused when I read about them in the popular press. A *New York
Times* [opinion piece][1] (author credit: Ellora Israni) is typical.  In it, Ms.
Israni argues that the use of algorithms to aid in criminal sentencing is
dangerously susceptible to abuse:

> Algorithms like COMPAS simply mimic the data with which we train them.
> COMPAS’s authors presumably fed historical recidivism data into their system.
> From that, the program ascertained what factors tend to make a defendant a
> higher risk. It then applied the patterns it gleaned to subsequent defendants,
> like Mr. Loomis, to spit out sentences that comport with existing trends.

Let me preface by saying that I have no substantive disagreement with Ms.
Israni, and I support her overall argument. It is crucial that we have a public
debate on the merits of introducing computational aids (let alone replacements),
and on many important issues we are, frankly, grossly negligent regarding their
downsides.

My objection to Ms. Israni's piece is entirely semantic and concerns her use of
the term "algorithm".  In fact, when the popular press discusses "algorithms",
it is almost always conflating two disjoint classes of computation techniques:
those which are designed to solve problems fully and concretely, and those which
are designed to suggest answers, given some level of uncertainty. 

Let's call the former group *algorithms* and the latter group *estimators*.
Though both classes have strong accountability implications, they are highly
distinct. Consequently, managing their implications will entail different
approaches, and we should consider them separately.

## Algorithms: test, test, test

Here's a simple example. Say you have a roster of teams in a spreadsheet: 

| Name | City | State | Wins | Losses |
|:--|:--|:--|:-:|:-:|
| Vikings | Minneapolis | MN | 13 | 3 |
| Lions | Detroit | MI | 9 | 7 |
| Packers | Green Bay | WI | 7 | 9 | 
| Bears | Chicago | IL | 3 | 13 |

At present, the teams are ordered according to the number of wins accrued during
the season. Suppose we want to reorder the teams according to the name of their
home cities. Typical spreadsheet software makes this very simple. You usually
just select a column and choose a menu option to sort it. In our case, we want
to sort the teams according to the **City** column in ascending order. The
result should be like the following:

| Name | City | State | Wins | Losses |
|:--|:--|:--|:-:|:-:|
| Bears | Chicago | IL | 3 | 13 |
| Lions | Detroit | MI | 9 | 7 |
| Packers | Green Bay | WI | 7 | 9 | 
| Vikings | Minneapolis | MN | 13 | 3 |

Notice that the request we made to the spreadsheet was very carefully
articulated. We wanted to order a series of data by a specified axis according
to a particular ordering scheme. Of course, our ordering scheme (lexicographic,
in this case) would be different had we wanted to order by **Losses**.
Nevertheless, the important thing for a computer is that there is an ordering
scheme of *some* kind.

How does the computer solve this problem? There are many approaches to choose
from. Sorting is a famous problem which is studied by students in an
introduction to algorithms course. The interested reader can check out different
approaches to this task [here][2].

Imagine asking the spreadsheet software to perform a sort by **City**, but after
it sorts you observe that "Packers" precedes "Lions" in the sheet. This
indicates that the sorting algorithm failed because clearly "Detroit" comes
before "Green Bay" in lexicographic order. It is evident to everyone involved
that the sort failed; there is no ambiguity permitted.

These are the characteristics of a problem which an *algorithm* can solve. The
question is clearly defined, leaving no room for confusion in interpretation. We
have a straightforward means of verifying that the result corresponds to our
specification. And from an engineer's perspective, there are procedures which
provide answer the question "correctly".

There are countless examples of common problems which algorithms solve. When I
sign in to a service, an algorithm verifies that my username and password match
an existing account. When I enter a residential address in a Google Maps, an
algorithm searches for the corresponding geographic location. When I query a
database, an algorithm processes keywords and determines which entries
are relevant to my search. When I approach an automatic door, an algorithm
detects my motion and opens the door for me. And when I work on my laptop, an
algorithm prioritizes my key presses and mouse movements with the other programs
running at the same time.

How might an algorithm fail? Since we tightly specify the problem that an
algorithm solves, we leave really only one way for failure: code bugs.
As it happens, bugs are incredibly common. Even when a theorist *proves* that an
algorithm will work, there remains the outside chance that an engineer will err
in implementing it. Bugs are [ubiquitous][3] and fiendishly difficult to
correct: we have seen historically that even high quality systems have failed
due to small programming errors.`




2. Distinguish between algorithms and "learning methods".
3. Problems in accountability for algorithms.
4. Problems in accountability for "learning methods."
5. How the media could improve its coverage.

[1]: https://www.nytimes.com/2017/10/26/opinion/algorithm-compas-sentencing-bias.html
[2]: https://www.toptal.com/developers/sorting-algorithms
