---
layout: post
title: "Investigating the stability of linear programs"
author: "David Kraemer"
categories: ln 
tags: [research, games, topology, optimization, linear programming]
---

I have been posting lately about the theory of multifunctions, which has so far
only tenuously related to possible applications. So for a break (actually, it's
because I've been thinking about it in the last few days), we can explore how
the theory of multifunctions and semi-continuity inform a very practical
problem. 

Let $$ 
\newcommand{\RR}{\mathbb{R}}
\newcommand{\set}[1]{\{#1\}}
\newcommand{\norm}[1]{\|#1\|}
\renewcommand{\bar}{\overline}
\DeclareMathOperator*{\argmin}{\mathrm{arg}\,\mathrm{min}}
\DeclareMathOperator*{\subjectto}{\mathrm{subject}\ \mathrm{to}}
A \in \RR^{m \times n}
$$ 
($$ m \geq n $$), let $$ b \in \RR^m$$, and $$ c \in \RR^n $$. In *linear
programming*, we want to solve a "linear program" (LP):

$$
\begin{align}
\argmin_{x \in \RR^n} \quad &c^T x \\
\subjectto \quad &Ax \leq b.
\end{align}
$$ <!-- _-->

The constraints $$ A x \leq b $$ determines a feasible region which has
considerably nice structure. In particular, this region is a closed convex
polytope&mdash;whether bounded or not&mdash;defined as a subset of $$\RR^n$$.
The objective function $$ c^T x $$ is simply a weighted sum of the coordinates
of the vector $$ x $$. For a given $$ \lambda $$, the set of points $$ \set{ x :
c^T x = \lambda }$$ determines a hyperplane in $$\RR^n$$. This is most clearly
understood in $$\RR^2$$, which we can see from the following figure:

![](/files/ipe-graphics/2018-06-26-linear-program-1.png)

The red line indicates the objective function, and the blue region is the
feasible region of points satisfying $$ Ax \leq b $$. The particular problem
that the figure is based off is

$$
\begin{align}
\argmin_{x,y \in \RR} \quad & 2 x + y \\
\subjectto \quad & -x - y & \leq 1 \\
& -x + 0y &\leq 0 \\
& 0x -y &\leq 0 \\
&  x + 0y &\leq 2 \\
&  0x + y &\leq 2
\end{align}
$$ <!-- _-->

To minimize $$ c^T x $$, we simply sweep the red line leftward. We go as far to
the left until we are about to exit the feasible region. At this place, any
feasible point on the line minimizes the objective. In the particular case for
above, the point $$ x^* = (0,1) $$ <!-- *--> is the only such minimizer. 

It's important to note that, in general as well as in this case, the minimizers
always reside on the boundary of the polytope. Sometimes, an entire segment (or
face in $$\RR^3$$, etc.) minimizes the objective, but sometimes only the
vertices of the polytope are the minimizers. 

The applications of linear programming are immense and widely studied. For
example, one might use an LP to model linear production constraints and
price/cost bundles. In applications, $$A, b,$$ and $$c$$ are usually determined
empirically, which invariably means that measurement uncertainty exists in the
model. This could be bad, because with sufficient uncertainty the solution to
the model LP could be completely different than the solution of the error-free
model. In a situation like this, formulating the model as an LP would be
useless.

So we would like to characterize the effect of changing the model parameters
(e.g., $$ A, b, c $$) on the solution $$ x^* $$, <!-- *--> and we hope (dearly)
that small changes to the parameters only produce similarly small changes to the
solution. If our hope is fulfilled, then we are in the enviable position of
quarantining the problem of model uncertainty to the actual observations.  The
alternative would be that our LP actually magnifies uncertainty, which would be
pretty awful.

## Parametric formulation of the LP

We've been working through some important theoretical concepts surrounding
multifunctions, and we now have the opportunity to put them into practice.
*Note:* I'm ditching the notation $$ \Gamma : X \twoheadrightarrow Y$$ for $$
\Gamma : X \to 2^Y $$ as the indicator for multifunctions. It's what Professor
Feinberg and others use in papers, and it makes more explicit the notion of
mapping from points to sets. (Here $$ 2^Y $$ is the power set of $$Y$$.)

For our first investigation, we will concern ourselves with the parameter $$ c
$$ and examine the effect of perturbations to it on the solution set. So, let $$
u : \RR^n \times \RR^n \to \RR$$ be the objective function $$ u(x,c) = c^T x $$.
We have total flexibility with our choice of $$ c $$ in theory, but $$ x $$
needs to be constrained to the feasible region. Thus, let $$ \Phi : \RR^n \to
2^{\RR^n}$$ be given by $$ \Phi c = \set{ x  \in \RR^n : Ax \leq b }$$. In other
words, $$ \Phi c $$ is the feasible region corresponding to the parameter $$ c
$$. In linear programming, $$ c $$ doesn't affect feasibility, so we see that $$
\Phi $$ is a constant multifunction. This immediately tells us that $$ \Phi $$
is upper and lower semi-continuous (hence continuous).

### Stability of the optimum value

A useful theoretical tool for studying optimization problems is the so-called
*extreme value function*, which in our case is $$ v : \RR^n \to
\bar{\RR} $$ defined by

$$
v(c) = \inf \set{ u(x, c) : x \in \Phi c }
$$

For general problems $$ v $$ has to remain theoretical, and this is the
case when the available computational techniques are only able to approximate
the infimum. For linear programming, the simplex method is one way to achieve
$$v(c)$$ in finite time, so considering the extreme value function has
immediate practical implications.

The stability of $$ v $$ is the first subject of our investigation. Since
$$ v $$ is a numerical function, we can begin by asking questions about
continuity. In this pursuit, Berge's theorem is the standard tool. In order to
apply Berge's theorem, we need to verify three things:

* $$ u $$ needs to be continuous,
* $$ \Phi $$ needs to be continuous,
* $$ \Phi $$ needs to be compactly valued, i.e. $$ \Phi c $$ is compact for
  every $$ c \in \RR^n $$.

We'll start by showing that $$ u $$ is continuous. To see this, we will show
that $$ u $$ is lower semi-continuous (upper semi-continuity traces a similar
argument, and continuity follows from both).  Let $$ \lambda \in \RR $$, and
consider the set 

$$ 
S(u, \lambda ) = \set{(x,c) : u(x,c) \leq \lambda }.
$$

We show that $$ S(u, \lambda) $$ is closed. Suppose $$(x_k, c_k) \in S(u,
\lambda) $$ converges to $$ x_0 $$. Let $$ \varepsilon > 0 $$ be arbitrary, and
fix $$ K \in \mathbb{N} $$ such that if $$ k \geq K $$ we have $$ \norm{x_0 -
x_k} < \sqrt{\varepsilon} $$ and $$ \norm{c_0 - c_k} < \sqrt{\varepsilon} $$.
Then

$$
\begin{align}
c_0^Tx_0 &= (c_0 - c_k)^T(x_0 - x_k) + c_k^T x_k \\
&\leq \norm{c_0 - c_k} \norm{x_0 - x_k} + c_0^T x_k \\
&\leq \norm{c_0 - c_k} \norm{x_0 - x_k} + \lambda \\
&< \varepsilon + \lambda.
\end{align}
$$

Since $$\varepsilon > 0 $$ was arbitrary, we conclude that $$ c_0^T x_0 \leq
\lambda $$ and hence that $$ S(u, \lambda) $$ is closed, which implies the lower
semi-continuity of $$ u $$.

Now, as we've already noted, $$ \Phi $$ is a constant multifunction, which
implies that $$ \Phi $$ is continuous. Whether $$ \Phi $$ is compact is
independent of our choice of $$ c $$, however, and depends exclusively on the
selection of $$A$$ and $$b$$. More can be discussed on this topic, but for now
we will operate under the assumptions that $$A$$ and $$b$$ are chosen so that $$
\Phi c $$ is compact. With this giant caveat in mind, we can apply Berge's
theorem to conclude that $$ v $$ is a continuous function of $$ c $$,
which provides the desired stability guarantee.

### Stability of the optimal points

From the above discussion we have established that $$ v $$ is continuous, which
has immediate stability implications. Now we turn to another important
investigation: namely, the stability of the multifunction $$ \Phi^* : \RR^n \to
2^{\RR^n} $$ by

$$
\Phi^* c = \set{x \in \Phi c : u(x,c) = v(c)},
$$

which identifies the set of optimal points of the LP. In previous posts, I
introduced the notions of semi-continuity for multifunctions. Here we will see
how to characterize $$ \Phi^* $$ according to these properties.

