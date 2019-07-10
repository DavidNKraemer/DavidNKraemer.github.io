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
$$\Phi(x) \subseteq Y$$. In addition, we have a real function $$u : X \times
Y \to \newcommand{\RR}{\mathbb{R}}\RR$$ over the product space. Call the pair
$$(X, Y, \Phi, u)$$ a *maximization problem*, and associate with it two
additional objects $$u^* : X \to \RR$$ and $$\Phi^* : X \to 2^Y$$ defined as

$$
\begin{align}
u^*(x) &= \sup \{u(x,y) : y \in \Phi(x) \} \\
\Phi^*(x) &= \{y \in \Phi(x) : u(x,y) = v(x) \}
\end{align}
$$

We're calling $$(X, Y, \Phi, u)$$ a maximization problem because we wish to
study the properties of $$u^*$$ and $$\Phi^*$$, which represent for each $$x \in
X$$ the maximum value and set of maximizers in $$\Phi(x)$$ of the function
$$u$$.

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
\max_{y \in Y} \quad &f_0(y) \\
\text{s.t.} \quad &f_i(y) \leq x_i \qquad i = 1, 2, \dots, n.
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

# Berge's maximum theorem. 
**Or: How I learned to to stop worrying and love function composition**

**Theorem** (Berge). *Let $$(X, Y, u, \Phi)$$ be a maximization problem. If $$u$$ is
a continuous function, then*

1. *if $$\Phi$$ is upper semi-continuous and compact valued, then $$u^*$$ is upper
   semi-continuous;*
2. *if $$\Phi$$ is lower semi-continuous, then $$u^*$$ is lower semi-continuous;*
3. *if $$\Phi$$ is continuous and compact valued, then $$u^*$$ is continuous.*

The third statement is really just a rephrasing of the previous two, but it is
invoked a lot by applications.

Now, it's true that the first two statements are independent of each other. For
many applications, it's important to keep these separate. If you want weaker
hypotheses, you also need to attack each component separately. But for the sake
of this post, let's consider the classical case found in the back of every
rigorous economics textbook: continuous $$u$$, continuous $$\Phi$$, compact
values.

In that case, consider the set-valued function $$\Lambda : X \to
2^{\mathbb{R}}$$ defined by

$$
\renewcommand{\bar}{\overline}
\Lambda(x) = \{u(x,y) : y \in \Phi(x)\}.
$$

Informally, $$\Lambda(x)$$ is the set of all values possibly attained when $$x$$
is the parameter. Actually, we can think of $$\Lambda$$ as a kind of "partial"
composition. Given $$x$$, we compose the function $$u_x(y) = u(x,y)$$ over the
set $$\Phi(x)$$. You might write $$\Lambda(x) = u(x, \Phi(x))$$ with only
somewhat abuse of notation. My preference is to write $$\Lambda = u \circ
\Phi$$, because this suggests the partial composition directly. Define the *top*
of $$\Lambda$$ to be the function $$\bar{\Lambda} : X \to \RR$$ satisfying

$$
\bar{\Lambda}(x) = \sup \Lambda(x).
$$

Then the top of $$\Lambda$$ is exactly the maximum function $$u^*$$. By studying
the properties of $$\Lambda$$ we will be able to deduce the continuity of its
top, and thereby prove the maximum theorem. To this end, we have to accomplish
two tasks. The first is "natural" as a result of framing $$\Lambda$$ in terms of
function composition.

**Theorem**. *For the maximization problem $$(X, Y, u, \Phi)$$ with $$\Lambda$$
defined as above, if $$u$$ is continuous, then:*

1. *if $$\Phi$$ is lower semi-continuous, then so is $$\Lambda$$;*
2. *if $$\Phi$$ is upper semi-continuous with compact values, then so is
   $$\Lambda$$.*

*Proof*. Suppose first $$\Phi$$ is lower semi-continuous. Let $$G \subseteq
\RR$$ be an open set, and suppose $$\Lambda(x) \cap G \ne \emptyset$$. Since the
function $$u(x, \:\cdot\:)$$ is continuous, it follows that $$V = \{y \in Y :
u(x, y) \in G\}$$ is open. What's more, 
there is a $$y \in \Phi(x)$$ such that $$u(x,y) \in G$$. In other words,
$$\Phi(x) \cap V \ne \emptyset$$. Since $$\Phi$$ is lower semi-continuous, we
can fix an open neighborhood $$U$$ of $$x$$ such that whenever $$x' \in U$$ we
have $$\Phi(x') \cap V \ne \emptyset$$. But this means that $$\Lambda(x') \cap G
\ne \emptyset$$, which proves lower semi-continuity.

Next, suppose $$\Phi$$ is upper semi-continuous and compact-valued. Let $$G
\subseteq \RR$$ be an open set with $$\Lambda(x) \subseteq G$$. Since $$u$$ is
continuous, for all $$y \in \Phi(x)$$ there are open neighborhoods $$U_y$$ of
$$x$$ and $$V_y$$ of $$y$$ such that $$(x',y') \in U_y \times V_y$$ implies
$$u(x',y') \in G$$. The sets $$\{V_y\}_{y \in \Phi(x)}$$ forms an open cover of
$$\Phi(x)$$, which is compact, so we can fix $$V_{y_1}, \dots, V_{y_n}$$ a
finite subcover with the corresponding $$U_{y_1}, \dots, U_{y_n}$$ neighborhoods
of $$x$$. Let $$U_1 = \bigcap_{j=1}^{n} U_{y_j}$$, so that if $$x' \in U_1$$ and
$$y' \in \bigcup_{j=1}^{n} V_{y_j}$$ we have $$u(x',y') \in G$$. On the other
hand, since $$\Phi$$ is upper semi-continuous, there is an open neighborhood
$$U_2$$ of $$x$$ such that $$\Phi(x') \subseteq \bigcup_{j=1}^{n} V_{y_j}$$ for
all $$x' \in U_2$$. Let $$U = U_1 \cap U_2$$. Then for all $$x' \in U$$ and $$y'
\in \Phi(x')$$, it follows that $$u(x', y') \in G$$; hence, $$\Lambda(x')
\subseteq G$$, which proves upper semi-continuity. Finally, let
$$\{G_\alpha\}_{\alpha \in A}$$ be an open cover of $$\Lambda(x)$$. Since $$u(x,
\:\cdot\:)$$ is continuous, the sets of the form $$V_\alpha = \{y \in Y : u(x,y)
\in G_\alpha\}$$ are themselves an open cover of $$\Phi(x)$$, which is compact.
Hence there are $$V_{\alpha_1}, \dots, V_{\alpha_n}$$ a finite subcover, and
$$G_{\alpha_1}, \dots, G_{\alpha_n}$$ is the corresponding subcover for
$$\Lambda(x)$$. This proves that $$\Lambda$$ is compact-valued. $$\square$$

---

It therefore follows that the conditions of Berge's maximum theorem together
imply that the set-valued function $$\Lambda$$ is continuous and compact-valued.
If we can show that the top of $$\Lambda$$ is a continuous function, the theorem
will be proved. 

Here's another question that has bugged me for a year or so now.  The notion of
semi-continuous real-valued functions is very old (at least as old as Baire's
1895 dissertation), but semi-continuous set-valued functions are more modern. A
lower semi-continuous set-valued function really doesn't have anything to do
with lower semi-continuous real-valued functions. In fact, if you consider a
"singleton" set-valued function $$\Gamma(x) = \{f(x)\}$$, you can show that
lower and upper semi-continuity of $$\Gamma$$ coincide![^2] What's the deal with
the nomenclature?

Maybe there was a deep connection intended by this language. On the other hand,
it's possible that, historically speaking, there was no strong relationship
between these concepts. Perhaps the pioneers of this theory had a different
connection in mind. I can affirm that naming things is hard, so I wouldn't put
it past the pioneers to settle early on slightly wonky terminology.

Regardless, the next theorem sheds some light on a possible relationship. It's
how I personally intuit the language similarities. It may not be worth the
confusion it seems to cause more generally (Rockafellar and Wets, for example,
opt for "inner" and "outer" semi-continuity, albeit "outer" does not mean
"upper" in our case), but at least it's a plausible justification.

**Theorem**. *With $$\Lambda$$ defined as above,*

1. *if $$\Lambda$$ is lower semi-continuous, then $$\bar{\Lambda}$$ is lower
   semi-continuous;*
2. *if $$\Lambda$$ is upper semi-continuous, then $$\bar{\Lambda}$$ is upper
   semi-continuous;*
3. *therefore, if $$\Lambda$$ is a continuous set-valued function, its top is a
   continuous real-valued function.*

*Proof*. First, suppose $$\Lambda$$ is lower semi-continuous. Let $$\varepsilon > 
0$$ be arbitrary, and let $$G = (\bar{\Lambda}(x)-\varepsilon,\infty)$$. Then
$$\Lambda(x) \cap G \ne \emptyset$$, so there exists an open neighborhood
$$U$$ of $$x$$ such that $$\Lambda(x') \cap G \ne \emptyset$$ for all $$x' \in
U$$. So there exists $$\lambda' \in \Lambda(x')$$ such that $$\lambda' >
\bar{\Lambda}(x) - \varepsilon$$, and by definition of $$\bar{\Lambda}$$ it
follows that $$\bar{\Lambda}(x') \geq \lambda' > \bar{\Lambda}(x) -
\varepsilon$$. This confirms that $$\bar{\Lambda}$$ is lower semi-continuous.

Next, suppose $$\Lambda$$ is upper semi-continuous. Let $$\varepsilon > 0$$ be
arbitrary, and let $$G = (-\infty, \bar{\Lambda}(x) + \varepsilon)$$. Then
$$\Lambda(x) \subseteq G$$, so there exists an open neighborhood $$U$$ of $$x$$
such that $$\Lambda(x') \subseteq G$$ for all $$x' \in U$$. So for all
$$\lambda' \in \Lambda(x')$$, we have $$\lambda' < \bar{\Lambda}(x) +
\varepsilon$$. By definition of $$\bar{\Lambda}$$, it follows that
$$\bar{\Lambda}(x') < \bar{\Lambda}(x) + \varepsilon$$, which confirms that
$$\bar{\Lambda}$$ is upper semi-continuous.

Combining these two results implies the third condition. $$\square$$

---

This approach to Berge's maximum theorem combined two simple intuitions. First,
function composition should hopefully preserve continuity. Second, the top of a
real set-valued function is just a normal function, so hopefully semi-continuity
concepts diffuse from one to the other. It turns out that both of these
intuitions are correct. It also means that Berge's maximum theorem is pretty
simple. Its presentation is already elementary in Berge's 1963 text, but here
we've shown that it's merely the consequence of even-more-elementary
observations.

# The weakness within

Say I'm a firm trying to maximize my profits subject to some parametric
constraints. I would love to apply Berge's maximum theorem to guarantee my
profits are continuous. In fact, I go out into the world and observe that they
*look* pretty damn continuous. So I get to work verifying the hypotheses of the
theorem.

This is where I get stuck. It turns out that the profit-maximizing behavior is
very stable, because resource and competition constraints lead to some nice
properties on the "max" operation. But as a firm, I could theoretically behave
really, *really* suboptimally. Just burn cash on useless projects and make no
money at all. If I cared to, I could make my minimum possible profit unboundedly
bad. Not that I would. I have my fiduciary responsibilities, after all. But it's
possible.

In applications, the maximization problem is usually well-posed, but few
applications simultaneously care about both maximizing *and minimizing* the
objective function.  Berge's maximum theorem doesn't account for this
possibility. In fact, if you define the *bottom* of $$\Lambda$$ by
$$\underline{\Lambda}(x) = \inf \Lambda(x)$$, it follows directly that the
conditions of Berge's maximum theorem imply that $$\underline{\Lambda}$$ is
continuous. In other words, the hypotheses are strong enough to give continuity
of the minimum. It's just that we don't care about the minimum! Symmetry has an
aesthetic value, but in this case no practical one.

To refine the theorem is therefore to de-symmetrize it. An important development
in this line of research was the introduction of $$\mathbb{K}$$-inf-compactness
by Professor Feinberg and his collaborators. It explicitly attacks the
compactness assumption on $$\Phi$$, but it also de-symmetrizes the upper
semi-continuity condition. Another development, by Tian and Zhou, de-symmetrizes
the lower semi-continuity condition with a feasible path transfer upper
semi-continuity condition on the objective function. In either case, the maximum
retains its continuity, but for the minimum all bets are off. Progress!

On a related note, it's weird to have been thinking about a single theorem for
the better part of a year. It doesn't feel that impressive, but I suppose that's
just research for you.

# Notes

[^1]: $$\Phi$$ defines a subset of $$X \times Y$$ by its graph $$\{(x,y) \in X \times Y : y \in \Phi(x) \}$$. In fact, it is completely determined by its graph, and every subset $$G \subseteq X \times Y$$ determines a unique set-valued map $$\Gamma : X \to 2^Y$$ defined by $$\Gamma(x) = \{y \in Y : (x,y) \in G\}$$.
[^2]: What *really* bends my noodle is that in the case of the singleton set-valued function $$\Gamma(x) = \{f(x)\}$$, upper and lower semi-continuity of $$\Gamma$$ each imply that $$f$$ is a continuous function. My first reaction: does this contradict our theorem? No. Since $$\bar{\Gamma}(x) = f(x)$$, it is certainly true that $$\bar{\Gamma}$$ is continuous. My second reaction: does this mean that we can say more about the continuity of $$\bar{\Lambda}$$ in general? The answer also appears to be no. The magical case of single-valued $$\Gamma$$ is somehow quite distinct from the general $$\Lambda$$, and nothing more in general can be inferred.
