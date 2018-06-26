---
layout: post
title: "Understanding semi-continuity of multifunctions"
author: "David Kraemer"
categories: ln 
tags: [research, games, topology, optimization]
---

Let $$ X $$ and $$ Y $$ be topological spaces. One of the basic objects of study
in topology are the continuous functions $$ f : X \to Y $$. Continuity in its
pure form is a topological characterization: if $$ V \subseteq Y $$ is an open
set, then continuity is equivalent to the openness of $$ f^{-1}[V] \subseteq X
$$. The same concept is useful for multifunctions in addition to regular
functions, though we need to clarify $$ f^{-1} [V] $$ in this context. First,
however, we need to disaggregate continuity into two weaker properties.

## Lower semi-continuity

Let $$ \Gamma : X \twoheadrightarrow Y $$ be a multifunction. We say that $$
\Gamma $$ is *lower semi-continuous* at $$ x_0 \in X $$ if,  for any open $$ V
\subseteq Y $$ with 

$$
\Gamma x_0 \cap V  \ne \emptyset ,
$$

there exists an open neighborhood $$ U(x_0) \subseteq X $$ such that if $$ x \in
U(x_0) $$, then

$$
\Gamma x \cap V \ne \emptyset.
$$

We will say that $$ \Gamma $$ is lower semi-continuous on $$ X $$ if it is lower
semi-continuous at all $$ x \in X $$.

Here's a visual depiction of lower semi-continuity:

![](/files/ipe-graphics/2018-06-12-lower-semicontinuous-general.png)

You can see above that $$\Gamma x_0 $$ and $$\Gamma x $$ need not intersect to
satisfy lower semi-continuity. 

<!--
To think through this concept further, let's work it out for the special case of
when $$ X $$ and $$ Y $$ are metric spaces. Let $$ \varepsilon > 0 $$ be
arbitrary, and select $$ y_0 \in \Gamma x_0 $$ and $$ y \in Y $$ such that $$
d_Y(y_0, y) < \varepsilon $$. (That is, $$ y_0 $$ is a member of the ball $$
B(y, \varepsilon) $$.) Then lower semi-continuity means that we can fix $$
\delta > 0 $$ so that if $$ d_X(x_0, x) < \delta $$ for $$ x \in X $$, then
there exists $$z \in \Gamma x$$ such that $$d_Y(y,z) < \varepsilon$$.

![](/files/ipe-graphics/2018-06-12-lower-semicontinuous-metric.png)

It's evident from the picture that $$d_Y(y_0, z) < 2\varepsilon$$, which also
implies that 

$$ 
\begin{align}
d_Y(\Gamma x_0, \Gamma x) &= \inf \{ d_Y(\nu_0, \nu) : \nu_0 \in \Gamma x_0, \nu
\in \Gamma x \} \\
&< 2\varepsilon.
\end{align}
$$

This motivates a sequential construction. Suppose in addition that $$ Y $$ is
complete. For $$ \varepsilon_n = \frac{1}{n} $$, choose $$ x_n \in X $$ such
that $$ \Gamma x_n \cap B(x_0, \varepsilon_n) \ne \emptyset$$, and take $$ y_n
$$ to be in this intersection arbitrarily. Then $$ d_Y(y_0, y_n) < 2
\varepsilon_n $$, and hence the sequence $$ (y_n) $$ converges to $$ y_0 $$.
Importantly, it need not be that $$ x_n \to x_0 $$, though we can establish that
$$ (x_n) $$ is a bounded sequence (with a convergent subsequence).
-->


## Upper semi-continuity

Now let's consider a parallel notion of semi-continuity. We say that $$ \Gamma
$$ is *upper semi-continuous* at $$ x_0 \in X $$ if, for any open $$ V \subseteq
Y $$ with

$$
\Gamma x_0 \subseteq V,
$$

there exists an open neighborhood $$ U(x_0) \subseteq X $$ such that if $$ x \in
U(x_0) $$, then

$$
\Gamma x \subseteq V.
$$

Equivalently, this last containment is equivalent to $$ \Gamma U(x_0) \subseteq
V $$. We will say that $$\Gamma$$ is upper semi-continuous on $$ X $$ if it is
upper semi-continuous at all $$ x \in X $$.[^1]

Here's a visual depiction of upper semi-continuity:

![](/files/ipe-graphics/2018-06-26-upper-semicontinuous-general.png)

In the above case, $$ \Gamma x_0 $$ and $$ \Gamma x $$ meet, but this is not
strictly necessary for $$ \Gamma $$ to be upper semi-continuous. 

The definition I have given here for global upper semi-continuity, according to
Professor Feinberg, is controversial. In *Topological Spaces*, Berge requires
that in addition to being upper semi-continuous at every $$ x \in X $$, global
upper semi-continuous multifunctions need also be compactly valued; that is, $$
\Gamma x $$ is a compact subset of $$ Y $$ for every $$ x \in X $$.  I didn't
find this obviously crucial, but if you want to have the standard continuity
property that $$ \Gamma K $$ is compact whenever $$ K $$ is compact, or if more
basically you want to have a continuous multifunction be equivalent to both
lower and upper semi-continuity, you need to throw this in. But for applications
in decision theory, global compactness guarantees are *really* difficult in general.

The immediate distinction between lower and upper semi-continuity is clear: with
lower semi-continuity we're interested in preserving a "nonempty intersection"
property, but with upper semi-continuity we're interested in preserving a
"covering" property. Okay, great. But what are we actually getting at by
defining these concepts as such?

That is, I think, a challenging question in general. Nevertheless, there is one
important, initial way to clarify the distinction between lower and upper
semi-continuity. Namely, we can tie them back to our prior definitions of lower
and upper inverses. Recall that a function $$ f : X \to Y $$ is continuous if
and only if $$ f^{-1}[G] $$ is open in $$ X $$ whenever $$ G $$ is open in $$ Y
$$. Likewise, we have the following characterizations of semi-continuous
multifunctions.

**Theorem**. Let $$ \Gamma : X \twoheadrightarrow Y $$ be a multifunction. Then,

1. $$ \Gamma $$ is lower semi-continuous if and only if $$ \Gamma^- G $$ is
   open in $$ X $$ whenever $$ G $$ is open in $$ Y $$,
2. $$ \Gamma $$ is upper semi-continuous if and only if $$ \Gamma^+ G $$ is
   open in $$ X $$ whenever $$ G $$ is open in $$ Y $$.

*Proof*. (1.) Assume first that $$ \Gamma $$ is lower semi-continuous, and
suppose $$ G \subseteq Y $$ is open. Then whenever $$ x_0 \in \Gamma^- G$$ we
can fix an open neighborhood $$ U(x_0) $$ such that if $$ x \in U(x_0) $$ we
have $$ \Gamma x \cap G \ne \emptyset $$ &mdash; in other words, $$ x \in
\Gamma^- G $$. So $$ U(x_0) \subseteq \Gamma^- G$$, and since $$x_0$$ was
arbitrary we see that $$ \Gamma^- G $$ is an open set. Conversely assume that
$$\Gamma^- G$$ is open. Then, given $$ x_0 \in \Gamma^- G $$, we can fix an open
neighbhorhood $$ U(x_0) \subseteq \Gamma^- G$$. But then the definition of
$$\Gamma^- G $$ gives us lower semi-continuity; for, $$ x \in U(x_0) $$ implies
$$ \Gamma x \cap G \ne \emptyset $$.

The proof of (2.) follows a nearly identical argument to that of (1.), replacing
the lower inverse criterion for the upper inverse criterion. $$ \square $$

