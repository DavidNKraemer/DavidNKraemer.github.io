---
layout: post
title: "A neat proof of the Cauchy criterion"
author: "David Kraemer"
categories: ln 
tags: [math,proofs,analysis]
---

I took introductory analysis with *Understanding Analysis* by Stephen Abbott,
and I think it is great for the purpose of a first course in real analysis.
However, now that I've done a bit more in analysis, I've started to revisit some
of the important proofs of the textbook with simpler (albeit more developed)
alternatives. 

Here is a proof of the Cauchy criterion on $$\mathbb{R}$$, which I am sure
exists elsewhere. Note that we are still using the completeness axiom that
Abbott formulates (that $$\sup A$$ exists for bounded above $$ A $$), but now
it's buried inside of the definitions of $$\limsup$$ and $$\liminf$$.

**Theorem** (Cauchy criterion). Let $$(x_n) \in \mathbb{R}$$ be a Cauchy
sequence. Then $$(x_n)$$ converges; i.e., $$\lim_{n \to \infty} x_n$$ exists.

*Proof*. Denote

$$
\begin{align*}
\overline{x} &= \limsup_{n \to \infty} x_n \\
\underline{x} &= \liminf_{n \to \infty} x_n.
\end{align*}
$$

We show that $$|\overline{x} - \underline{x}| < \varepsilon$$ for every
$$\varepsilon > 0$$. This suffices to show that $$\lim x_n$$ exists.

Both $$\overline{x}$$ and $$\underline{x}$$ are cluster points of the sequence
$$(x_n)$$. We will show how to get $$| x_n - \overline{x} | < \delta$$ for
judiciously chosen $$\delta > 0$$ and sufficiently large $$n$$, and use the
parallel fact for $$\underline{x}$$ to establish the claim.

Fix $$ \overline{N} \in \mathbb{N} $$ such that $$| x_{\overline{N}} -
\overline{x} | < \frac{\varepsilon}{4}$$ and such that $$ | x_n -
x_{\overline{N}} \ < \frac{\varepsilon}{4} $$ for all $$n \geq \overline{N}$$.
The former condition can be satisfied by virtue of $$\overline{x}$$ being a
cluster point of $$(x_n)$$, and the latter by the fact that $$(x_n)$$ is Cauchy.
Then

$$
\begin{align*}
  | x_n - \overline{x}| &\leq | x_n - x_{\overline{N}} | + \ x_{\overline{N}} -
  \overline{x} | \\
  &< \frac{\varepsilon}{2}.
\end{align*}
$$

We can find an analogous $$\underline{N} \in \mathbb{N}$$ for $$\underline{x}$$.
Taking $$ N = \max(\overline{N}, \underline{N})$$, we have that

$$
\begin{align*}
  | \overline{x} - \underline{x} | & \leq | \overline{x} - x_n | + | x_n - \underline{x} | \\
  &< \frac{\varepsilon}{2} + \frac{\varepsilon}{2} \\
  &= \varepsilon,
\end{align*}
$$

for all $$n \geq N$$. This is what we needed. $$ \square $$
