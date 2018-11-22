---
layout: post
title: "Accountable countability: an airtight program for counting the rationals."
author: "David Kraemer"
categories: ln
tags: [cardinality,analysis]
---

An introductory course in analysis is incomplete without an examination of the
cardinality of infinite sets, much to the chagrin of the students! The important
points, which are carefully emphasized in such a course, are that while the natural
numbers $$\mathbb{N}$$ and the rational numbers $$\mathbb{Q}$$ have the same
cardinality, the real numbers $$\mathbb{R}$$ has a strictly "larger"
cardinality. If the cardinality of $$\mathbb{N}$$ is labeled *countable*, we say
that the cardinality of $$\mathbb{R}$$ is *uncountable*.

The proof that $$\mathbb{R}$$ is uncountable usually follows Cantor's diagonalization
argument. In particular, it is shown that the unit segment $$[0,1]$$ is
uncountable, and as $$[0,1] \subseteq \mathbb{R}$$ the uncountability of $$\mathbb{R}$$
follows. I actually think the diagonalization argument is sufficiently clear for
an undergraduate to understand, because it involves expressing each number in
$$[0,1]$$ as a sequence of decimals[^1].

However, I haven't really been satisfied with arguments for the countability of
$$\mathbb{Q}$$. Typically, such arguments go as follows: we know that $$\mathbb{N}$$ is
countable by definition, and we can show that $$\mathbb{Z}$$ is countable; this
suggests that a countable set is still countable if we include with it the
set of additive inverses; so considering the positive rationals $$\mathbb{Q}^+$$
suffices; but since a rational $$r \in \mathbb{Q}^+$$ has a unique representation in
lowest terms $$r = a / b$$ ($$a, b \in \mathbb{N}$$), it suffices to show that $$\mathbb{N}
\times \mathbb{N}$$ is countable; from which it follows that $$\mathbb{Q}^+$$ is countable as
well.

Of course, there is nothing wrong with this argument *in theory*. In theory,
every step above can be made rigorous. In theory, there are no holes, no
ambiguities about the multiple ways to represent a rational number. As Homer
says, "in theory, communism works. In theory!"

![s05e17 don't @ me](/files/simpsons/gifs/intheory.gif)

But leaving these steps as "exercises" (that is, a true statement which every
student will henceforth take on fiat) is a cop-out by textbook authors and
professors who don't want to get their hands dirty, and I'm tired of their
nonsense! Is $$\mathbb{Q}$$ countable or not?

In this post, I propose an approach to showing that $$\QQ$$ is countable by means of the following outline:

1. The set of integers $$\mathbb{Z}$$ is countable.
2. If $$A \subseteq \RR$$ is nonnegative, countable, and $$0 \in A$$, then $$A
   \cup -A$$ is also countable.
3. The product $$\NN \times \NN$$ is countable.
4. If $$A_1, A_2, A_3, \dots$$ are a countable union of sets, then
   $$\bigcup_{j=1}^{\infty} A_j$$ is also countable.
5. There exists a countable partition of the set of rational numbers $$\QQ^+$$
   into countable sets.
6. Then $$\QQ$$ is countable.

This approach has two advantages. First, it's completely rigorous, with no gaps
to be filled in by the reader. Second, the first few components of the outline
are conceptually straightforward, while the more complex ideas are distilled
from any unnecessary context.

# Preliminary definitions

Let's begin by formally defining terms. I expect that if you've made it this
far, then you've been introduced to these definitions, but I would like to
imagine that this post can be read in a self-contained fashion. So we proceed:

**Definition 1**. A function $$ f : A \to B $$ is *injective* if whenever $$
f(a_1) = f(a_2)$$ we have $$a_1 = a_2$$. It is *surjective* if for every $$b \in
B$$ there exists an $$a \in A$$ with $$f(a) = b$$. It is *bijective* if it is
both injective and surjective.

**Definition 2**. A set $$A$$ is *finite* if there exists $$ n \in \NN $$ and a
bijective function $$ f : \{0,1,2,\dots, n-1\} \to A$$. It is *countable* if
there exists a bijective function $$ f : \NN \to A$$. It is *uncountable* if it
is neither finite nor countable.

Some people would prefer to include finite sets in the definition of countable,
but for clarity I will impose that these are distinct concepts. Now, I gave an
introductory spiel about why leaving exercises for the reader is an invitation
for neglect. Fully aware of this problem (and the hypocrite it makes me), I will
leave it as an exercise to show that $$\NN$$ is itself a countable set. (*Hint*:
let $$f(n) = n$$ and show that $$f$$ is bijective.) My justification for this
inconsistency is to say that the proof that $$\NN$$ is countable is more of a
comprehension check for the above definitions than an insightful result itself.

# Warmup: showing $$\mathbb{Z}$$ is countable

This is admittedly the easiest part of project. We can even write out an
explicit formula that characterizes a bijection $$f : \mathbb{N} \to \mathbb{Z} $$. In
particular, for $$n \in \mathbb{N}$$, let

$$
f(n) = 
\begin{cases}
\frac{n}{2} & \text{$n$ is even} \\
-\frac{n+1}{2} & \text{$n$ is odd}.
\end{cases}
$$

Let's see how this function starts out on the first few numbers in $$\mathbb{N}$$:

| $$n$$    | 0 | 1  | 2 | 3  | 4 | 5  | 6 | 7 | 8 | 9 | 10 |
| $$f(n)$$ | 0 | -1 |1  | -2 | 2 | -3 | 3 | -4 | 4 | -5 | 5 |

Look's promising! Let's formalize this idea into a proof.

**Proposition 1**. *The set of integers $$\ZZ$$ is countable.*

*Proof*.  We will show that $$f$$ is injective and surjective. First injective.
Suppose $$f(n_1) = f(n_2)$$. In particular, it is either the case that $$f(n_1),
f(n_2) \geq 0$$, or it isn't. Suppose that they are both nonnegative (the
negative case is almost identical). Then we can write $$f(n_1) = \frac{n_1}{2}$$
and $$f(n_2) = \frac{n_2}{2}$$. Since $$\frac{n_1}{2} = \frac{n_2}{2}$$, it
follows that $$n_1 = n_2$$. Hence, $$f$$ is injective.  

Next, we show that $$f$$ is surjective. Fix any $$z \in \mathbb{Z}$$. Now,
either $$z \geq 0$$ or $$z < 0$$. Suppose that $$z < 0$$ (the nonnegative case
is almost identical, as before).  Then it follows that $$-2z - 1 > 0$$, and as
$$f(-2z-1) = z$$, we are done. We conclude that $$f$$ is bijective, and hence
$$\mathbb{Z}$$ is countable. $$\square$$

Alternatively, let $$ g : \mathbb{Z} \to \mathbb{N} $$ be defined by 
$$
g(z) =
\begin{cases}
2z & z \geq 0 \\
-2z-1 & z < 0.
\end{cases}
$$

The corresponding table for $$g$$ starts off as

| $$z$$       | 0 | -1 |1  | -2 | 2 | -3 | 3 | -4 | 4 | -5 | 5 |
| $$g(z)$$    | 0 | 1  | 2 | 3  | 4 | 5  | 6 | 7 | 8 | 9 | 10 |

So looking at the above data, it seems pretty clear that $$f$$ and $$g$$ are
inverses of each other, and you can show that this is the case. However, since
we've already worked out that $$f$$ is bijective, there is no need to do so at
the moment.

# Getting bigger: a nonnegative countable set $$A \subseteq \mathbb{R}$$

The function $$f$$ from the previous section does not actually rely on any
particular properties of the natural numbers besides the fact that they are
nonnegative (and countable, of course). The argument leads to the following
extension, which we will use to simplify the proceeding work. So, let $$A
\subseteq \mathbb{R}$$ be a nonnegative countable set with $$0 \in A$$. We can
therefore impose the enumeration 

$$
A = \{ a_0, a_1, a_2, a_3, a_4, a_5, \dots \}
$$

of $$A$$, and for clarity, assume that $$a_0 = 0$$.  $$A$$ corresponds to all
nonnegative terms, so if by denoting 

$$-A = \{ -a : a \in A \}$$ 

to be the set of all additive inverses of $$A$$, we want to consider the set
$$A' = A \cup (-A)$$. Our goal is to show that $$A'$$ is still countable. The
trick will be that we don't need to care about the values of each $$a_k \in A$$;
rather, we can perform all of the same manipulations on the index $$k$$ instead.
In particular, let $$f : \NN \to A'$$ to be

$$
f(n) =
\begin{cases}
a_{n/2} & \text{$n$ is even} \\
-a_{(n+1)/2} & \text{$k$ is odd}
\end{cases}
$$

This time, our table becomes

| $$n$$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| $$f(n)$$ | $$a_0$$ | $$-a_1$$ | $$a_1$$ | $$-a_2$$ | $$a_2$$ | $$-a_3$$ | $$a_3$$ | $$-a_4$$ | $$a_4$$ | $$-a_5$$ | $$a_5$$ | 

Notice how we've embedded the same idea from the previous section, not in the
terms themselves, but just in the order of the indices. Also, it's important for
our purposes that $$a_0 = 0$$, because this "center" of $$A'$$ is the odd term
out and is therefore "ignored" by $$f$$. Let's proceed as before with the formal
proof. (I'm going to try to preserve the proof to Proposition 1 as much as
possible in the following argument, just to convince you further that these two
cases are basically the same.)

**Proposition 2**. *The set $$A'$$ is countable.*

*Proof*.
We will show that $$f$$ is injective and surjective. First injective.
Suppose $$f(n_1) = f(n_2)$$. In particular, it is either the case that $$f(n_1),
f(n_2) \geq 0$$, or it isn't. Suppose that they are both nonnegative (the
negative case is almost identical). Then we can write $$f(n_1) = a_{\frac{n_1}{2}}$$
and $$f(n_2) = a_{\frac{n_2}{2}}$$. Since $$a_{\frac{n_1}{2}} = a_{\frac{n_2}{2}}$$, it
follows that $$n_1 = n_2$$. Hence, $$f$$ is injective.  

Next, we show that $$f$$ is surjective. Fix any $$a \in A'$$. Now,
either $$a \geq 0$$ or $$a < 0$$. Suppose that $$a < 0$$ (the nonnegative case
is almost identical, as before).  Then it follows that $$-a \in A$$, and since
$$A$$ is countable, we can write $$-a = a_n$$ for some $$n \in \NN$$.
$$f(-2z-1) = z$$, we are done. We conclude that $$f$$ is bijective, and hence
$$\mathbb{Z}$$ is countable. $$\square$$


Was it strictly necessary to include $$0 \in A$$? No, because given a countable
set $$A$$, a point $$a \in A$$, and a point $$b \notin A$$, you can show that
both $$A \setminus \{a \}$$ and $$A \cup \{b\}$$ are themselves countable sets.
(Again, I'm leaving this as an exercise because I don't follow what I preach.
But to think this through, consider the case for $$\NN$$ when we're deciding to
include $$-1$$ or throw away $$0$$. *Hint*: $$f(n) = n-1$$ and $$g(n) = n+1$$
are useful functions here.) We included $$0$$ because $$\NN$$ includes $$0$$,
and in order to make the direct connection from the previous case of showing
$$\ZZ$$ is countable, we needed to treat $$a_0$$ as the "center" of $$A'$$, much
like how $$0$$ is the "center" of $$\ZZ$$.

# Making progress: showing that $$\NN \times \NN$$ is countable

With the previous details worked out, we can comfortably return to the main
thrust of the argument for our program. The essential insight, which will
dictate our future work, is to realize that $$\NN \times \NN$$ is itself a
countable set. Let's see why by writing out the first part of $$\NN \times
\NN$$.

| (m,n) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 0 | (0,0) | (0,1) | (0,2) | (0,3) | (0,4) | (0,5) | (0,6) | (0,7) |
| 1 | (1,0) | (1,1) | (1,2) | (1,3) | (1,4) | (1,5) | (1,6) | (1,7) |
| 2 | (2,0) | (2,1) | (2,2) | (2,3) | (2,4) | (2,5) | (2,6) | (2,7) |
| 3 | (3,0) | (3,1) | (3,2) | (3,3) | (3,4) | (3,5) | (3,6) | (3,7) |
| 4 | (4,0) | (4,1) | (4,2) | (4,3) | (4,4) | (4,5) | (4,6) | (4,7) |
| 5 | (5,0) | (5,1) | (5,2) | (5,3) | (5,4) | (5,5) | (5,6) | (5,7) |
| 6 | (6,0) | (6,1) | (6,2) | (6,3) | (6,4) | (6,5) | (6,6) | (6,7) |
| 7 | (7,0) | (7,1) | (7,2) | (7,3) | (7,4) | (7,5) | (7,6) | (7,7) |



[^1]: This is assuming that such decimal representations are treated with the necessary care, given that many numbers in $$[0,1]$$ have *multiple* decimal representations.
