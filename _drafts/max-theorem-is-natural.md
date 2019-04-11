---
layout: post
title: "Berge's maximum theorem is overpowered (and weak)"
author: "David Kraemer"
categories: ln 
tags: [math,berge,maximum]
---

I've spent some time thinking about the Berge maximum theorem, which is
a classic result in parametric optimization. It relates to some of my work with
Professor Feinberg here at Stony Brook, but we are pushing in a different
direction at the moment. I'm interested in the "classical" theorem, which
appeared in Berge's book *Topological spaces* in 1963. (To be clear, it appears
*in English* in 1963, but the original French edition was in 1959.) To
summarize the result, we usually say that it provides sufficient conditions for
the optimal values of an optimization problem to be continuous in the
parameters of the problem. 

The general setup for the theorem is as follows. There are two (formally,
topological, but for the sake of presentation) metric spaces $$X$$ and $$Y$$
and a set-valued map $$\Phi : X \to 2^Y$$, so that for each $$x \in X$$ we have
$$\Phi(x) \subseteq Y$$[^1]. In addition, we have a real function $$u : X \times
Y \to \newcommand{\RR}{\mathbb{R}}\RR$$ over the product space. Call the pair
$$(\Phi, u)$$ a *maximum problem*, and associate with it two additional objects
$$u^* : X \to \RR$$ and $$\Phi^* : X \to 2^Y$$ defined as

$$
\begin{align}
u^*(x) &= \sup \{u(x,y) : y \in \Phi(x) \} \\
\Phi^*(x) &= \{y \in \Phi(x) : u(x,y) = v(x) \}
\end{align}
$$

We're calling $$(\Phi, u)$$ a maximum problem because we wish to study the
properties of $$u^*$$ and $$\Phi^*$$, which represent for each $$x \in X$$ the
maximum value and set of maximizers in $$\Phi(x)$$ of the function $$u$$.

I want to pause to give some motivation for the theorem. When I was first
getting introduced to the statement, it seemed like a quaint application of
general topology to real functions on product spaces. Indeed that is the math
involved. But this is not a particularly successful way of *reasoning* about
the theorem, and so I want to clarify this point.

## Motivation: parametric optimization

There are two applications I have seen that give a good picture of the result
and why we should care about it. The first arises from "parametric
optimization". Consider, for example, a common optimization problem with the
form

$$
\begin{align}
\max_{y \in Y} f_0(y)& \\
\mathrm{s.t.} f_i(y) &\leq x_i \qquad i = 1, 2, \dots, n.
\end{align}
$$

You can imagine that perhaps each $$f_i$$ ($$i = 0, \dots, n$$) is convex, so
that this problem is to maximize a convex function over a convex set. We have
all sorts of nice theory to tell us when the maximum is achieved and how to
characterize the maximizers.

However, you're not convinced about the correctness of the $$x_i$$ terms. Maybe
you got them from an experiment, or maybe they were estimated from some
previous problem. They're probably in a ballpark of being correct, but there
are error bars. How confident can you be that the maximum and maximizers are
meaningful to your application, given the uncertainty of your measurements?

If we let $$(x_1, \dots, x_n)$$ be our "parameter" $$x$$, and define 

$$\Phi(x) = \{y \in Y : f_i(y) \leq x_i, i = 1, \dots, n\}$$ 

to be the feasible sets associated with the parameter, then we can cast our
convex problem with uncertainty as a parametric optimization problem. So our
formalism treats $$X$$ as a space of parameters, $$Y$$ as the variable space,
and the optimization is done in $$Y$$ over a fixed set of parameters.If it
happens that $$u^*$$ is continuous, then we get a stability guarantee of our
parameter estimate.

## Motivation: control theory

A completely different application arises from control theory. Say you have
a model with state space $$X$$ and action space $$Y$$. At each state $$x$$,
there is some set of feasible actions, which we'll call (wink wink)
$$\Phi(x)$$. Whenever we have the state-action pair $$(x,y)$$, we receive
a reward (wink wink wink) $$u(x,y)$$. Our goal is to maximize reward at every
state, which means choosing the best actions to that effect. Our optimal *value
function*, then, is a map $$u^* : X \to \RR$$ that maximizes $$u(x,y)$$ for
each state $$x$$.

When the state space is not countable, having any ability to speak about the
structure of value function usually requires measurability or continuity
properties on the rewards. In addition, we usually get to the value function by
means of sequential approximation. In this case, the goal is not necessarily
"stability" per say, but rather that the limits involved in such arguments
behave properly.

## Motivation summary 

I want to emphasize that this formalism is applied really differently in
control theory than in parametric optimization. You have to do a mental
jump rope exercise to go from one to the other. On the other hand, continuity
of the function $$u^*$$ has important implications in both domains. To
summarize, we have three interpretations (including the technical math version).  

| | $$X$$ |$$Y$$ | $$\Phi$$ | $$u$$ |
|:--|:----|:----|:-------|:----|
| Math | Metric space | Metric space | Subset[^1] of $$X \times Y$$ | Real function on $$X \times Y$$ |
| Parametric optimization | Parameter space | Variable space | Feasibility regions | Objective function |
| Control theory | State space | Action space | Available actions | Reward function |

# Berge's maximum theorem. Or: How I learned to to stop worrying and love function composition

**Theorem** (Berge). *Let $$(u, \Phi)$$ be a maximization problem. If $$u$$ is
a continuous function, then*

1. *if $$\Phi$$ is upper semi-continuous and compact valued, then $$u^*$$ is upper
   semi-continuous;*
2. *if $$\Phi$$ is lower semi-continuous, then $$u^*$$ is lower semi-continuous;*
3. *if $$\Phi$$ is continuous and compact valued, then $$u^*$$ is continuous.*

The third statement is really just a rephrasing of the previous two, but it is
invoked a lot by applications.

[^1]: $$\Phi$$ defines a subset of $$X \times Y$$ by its graph $$\{(x,y) \in X \times Y : y \in \Phi(x) \}$$. In fact, it is completely determined by its graph, and every subset $$G \subseteq X \times Y$$ determines a unique set-valued map $$\Gamma : X \to 2^Y$$ defined by $$\Gamma(x) = \{y \in Y : (x,y) \in G\}$$.
