---
layout: post
title: "Gradients for Grown-Ups (Part 3)"
author: "David Kraemer"
categories: ln 
tags: [math,gradient]
---

This is the third posts in a series of posts, "Gradients for Grown-Ups". You can
see the previous post [here](gradients-for-grownups-part-02).

Last time, we used the general procedure to compute the gradients of the
ubiquitous linear algebra functions $$ x^T x $$ and $$ x^T A x $$. This time,
we'll get used to the standard calculus tools that come with the gradient:
linearity, the product rule, and the chain rule. In many respects, these are
simple analogues of our simple friend $$ \frac{d}{dx} $$, but we shall see how
the generality adds new complexity as well.

# Theoretical aside

We'll take a moment to address the gradient as an abstract mathematical
operator. The theory here won't be necessary for later, so feel free to skip
this section if you are so inclined. Let 

$$ 
\newcommand{\FF}{\mathscr{F}}
\newcommand{\RR}{\mathbb{R}}
\newcommand{\set}[1]{\{#1\}}
\FF_n^m = \set{f : \RR^n \to \RR^m : \frac{\partial f_i}{\partial x_j} \text{
exists for all } i = 1, \ldots, m, j = 1, \ldots, n }.
$$

In English, $$\FF_n^m$$ is a function space whose elements map from $$\RR^n$$
to $$\RR^m$$ and have all of their corresponding partial derivatives defined.
So, for example, the function $$ f : \RR^2 \to \RR^3 $$ given by

$$
f(x,y)
=
\begin{bmatrix}
2x + 3y \\
-y^2 \\
e^{-x} \sin y
\end{bmatrix}
$$

is a member of $$ \FF_2^3$$, since every coordinate of $$ f(x,y) $$ has partial
derivatives with respect to both $$ x $$ and $$ y $$. Importantly, $$ \FF_n^m $$
is a *vector space* as a particular subset of all functions from $$\RR^n \to
\RR^m $$. We define the gradient to be the operator $$\nabla : \FF_n^1 \to \FF_n^n $$
given by

$$
\nabla f = 
\begin{bmatrix}
 \partial f / \partial x_1 \\
 \partial f / \partial x_2 \\ \vdots \\
 \partial f / \partial x_{n-1} \\
 \partial f / \partial x_n \\
\end{bmatrix}
$$

Of course this is not a new idea: we've always worked with the gradient as
taking a function $$ f : \RR^n \to \RR $$ and returning a vector function $$
\nabla f : \RR^n \to \RR^n $$. What is useful about this formalism is that it
indicates that $$ \nabla $$ is a mapping between vector spaces. In fact, as we
shall see, it is a linear transformation!

# Linearity

The first thing we will show is that the gradient preserves linear combinations.
(For the theorists, this is how we prove that the $$ \nabla $$ operator is a
linear transformation.) Practically speaking, this property is of great
importance, as we frequently construct functions through these linear
combinations. It therefore allows us to evaluate the gradient "piecewise", which
is often far simpler than all at once.

Given two functions $$ f $$ and $$ g $$, suppose we want to compute $$ \nabla
(f+g) $$. So, take an arbitrary index $$ k = 1, \ldots, n $$ and compute $$
\partial_k (f + g) $$. Now, since the partial derivative operator is linear, we
have 

$$
\partial_k (f + g) = \partial_k f + \partial_k g,
$$

and putting this into vector form we obtain

$$
\begin{align}
\nabla (f + g) &= 
\begin{bmatrix}
\partial_1 ( f + g) \\
\partial_2 ( f + g) \\
\vdots \\
\partial_{n-1} ( f + g) \\
\partial_n ( f + g)
\end{bmatrix} \\
&= 
\begin{bmatrix}
\partial_1 f \\
\partial_2 f \\
\vdots \\
\partial_{n-1} f \\
\partial_n f
\end{bmatrix} + 
\begin{bmatrix}
\partial_1 g \\
\partial_2 g \\
\vdots \\
\partial_{n-1} g \\
\partial_n g
\end{bmatrix} \\
&= \nabla f + \nabla g.
\end{align}
$$

Similarly, for a given constant $$ \alpha $$, since $$ \partial_k (\alpha \cdot
f) = \alpha \cdot \partial_k f $$, we conclude that $$ \nabla (\alpha  \cdot f)
= \alpha \cdot \nabla f $$. Together, these two properties are combined and
called *linearity*:

$$
\boxed{
\nabla (\alpha \cdot f + \beta \cdot g) = \alpha \cdot \nabla f + \beta \cdot
\nabla g.}
$$

As a very standard example, suppose our function was a quadratic form $$ f(x) =
\frac{1}{2} x^T A x + b^T x + c $$ where $$ A $$ is symmetric. Then we can
compute $$ \nabla f(x) $$ painlessly by using linearity:

$$
\begin{align}
\nabla f(x) &= \nabla ( \frac{1}{2} x^T A x + b^T x + c ) \\
&= \nabla ( \frac{1}{2} x^T A x ) + \nabla (b^T x) + \nabla c \\
&= \frac{1}{2} \nabla (x^T A x) + \nabla (b^T x) + \nabla c \\
&= \frac{1}{2} \cdot 2 A x + b \\
&= Ax + b.
\end{align}
$$

# Product rule

For computing the derivative of a product of two functions, we have the
following rule:

$$
(f \cdot g)' = f \cdot g' + g \cdot f'.
$$

As luck would have it, there is an analogous product rule for gradients!

# Composition and the chain rule

After linearity, the chain rule is probably the most important property from
derivatives, but is the trickiest to state. If $$ f $$ and $$ g $$ are
functions, and we take the composition $$ h = f \circ g$$ defined as $$ h(x) =
f(g(x)) $$, then the chain rule for derivatives states that

$$
h'(x) = f'(g(x)) \cdot g(x).
$$

There is a chain rule for gradients, and it has similar practical importance to
the simple chain rule. However, there are added wrinkles involved which we will
tread carefully through.
