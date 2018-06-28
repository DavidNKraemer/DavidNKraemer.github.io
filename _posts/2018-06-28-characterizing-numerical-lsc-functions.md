---
layout: post
title: "A characterization of numerical lower semi-continuity"
author: "David Kraemer"
categories: ln 
tags: [research, games, topology, optimization]
---

One can define numerical lower semi-continuity using a sequential criterion: for
$$ 
\newcommand{\RR}{\mathbb{R}}
\renewcommand{\bar}{\overline}
f : X \to \bar{\RR},
$$
we say that $$ f $$ is *lower semi-continuous* at $$ x \in X $$ if for any
sequence $$x_n \to x$$ we have 

$$
f(x) \leq \liminf_{n \to \infty} f(x_n).
$$

The idea is that $$ f(x_n) $$ is eventually bounded below by $$ f(x) $$; that
is, for every $$ \varepsilon > 0 $$ there exists an $$ N \in \mathbb{N} $$ such
that whenever $$ n \geq N $$ we have 

$$ 
f(x_n) - f(x) < \varepsilon. 
$$

Unsurprisingly, if $$ f $$ is lower semi-continuous it follows that for any
convergent sequence $$ x_n \to x $$ we have

$$
f(x) \leq \limsup_{n \to \infty} f(x_n),
$$

since

$$
\begin{align}
f(x) & \leq \liminf_{n \to \infty} f(x_n) \\
&\leq \limsup_{n \to \infty} f(x_n).
\end{align}
$$

What's more surprising is that these conditions are equivalent! 

**Proposition**. *If for any convergent sequence $$ x_n \to x $$ we have*

$$
f(x) \leq \limsup_{n \to \infty} f(x_n)
$$

*then $$ f $$ is lower semi-continuous at $$ x $$.*

I find this surprising because the property above relates to the limiting *upper
bounds* of a sequence. Why should that have any influence on the limiting
behavior of the *lower bounds*? There is sort of a mathematical feint at work
here, because the upper limit is not where the strength of the hypothesis lies.
Instead, it's hidden in the fact that this upper limit bound holds *for every*
convergent sequence. Let's find out why.

*Proof*. By the contrapositive. Suppose $$ f $$ is not lower semi-continuous, so
that there exists a sequence $$ x_n \to x $$ with

$$
\liminf_{n \to \infty} f(x_n) = s < f(x).
$$

Now, $$ s $$ is a limit point of the sequence $$ ( f(x_n) ) $$, which means we
can fix a subsequence $$ x_{n_k} $$ for which $$ \lim _ {k \to \infty}
f(x_{n_k}) = s $$. But since $$( x _ {n_k} )$$ is a subsequence of $$ (x _ n)
$$, it remains true that $$ x _ {n_k} \to x $$. This sequence converges to $$ x
$$ but also has the property that

$$
\begin{align}
\limsup _ {k \to \infty} f(x _ {n_k}) &= \lim _ {k \to \infty} f(n_k) \\
&= s \\
&< f(x) 
\end{align}
$$

which implies that the hypothesis of the proposition is false. By taking the
contrapositive, we obtain the desired result. $$ \square $$

I suspect that this is actually a highly practical result, because it provides
the flexibility of looking at either the upper or lower limits of arbitrary
sequences. That can (and soon will) come in handy for some of my work.
