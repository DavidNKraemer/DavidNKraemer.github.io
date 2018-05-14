---
layout: post
title: "Gradients for Grown-Ups (Part 1)"
author: "David Kraemer"
categories: ln 
tags: [math,gradient]
---

This is the first in a series of posts, "Gradients for Grown-Ups". You can see
the next post [here](gradients-for-grownups-part-02).

Boyd and Vanderberghe's *Convex Optimization*[^1] is an excellent primer for
learning the fundamentals of the subject. I should know, because I just took a
course which featured this book. I didn't always pay attention in class (because
it was my sixth consecutive hour of lectures! Kids, pay attention in school),
and the textbook was always a useful fallback on the course material.

I have one complaint about the book, however, which was a problem I had
throughout. The text assumes that you've had multivariate calculus and seen the
major parts of linear algebra, but I felt that this understates the
prerequisites. To be sure, I've had my share of calculus and analysis. I've sat
in linear algebra lectures more times than I care to admit. So I thought I would
be fine going in, and I was. 

Mostly.

You see, in my calculus classes, a typical question one might encounter is the
following:

*Compute $$\nabla f(x,y)$$, where $$f(x,y) = xy \sin(x^2)$$.*

This is pretty routine. You compute $$\frac{\partial f}{\partial x}$$ and
$$\frac{\partial f}{\partial y}$$, and store them in the form of a vector. After
all, this is what the gradient is.

By contrast, the textbook expects you to be comfortable with questions like
this:

*Compute $$ \nabla f(x)$$, where $$f(x) = x^TAx$$ for $$A \in \mathbb{R}^{n
\times n}$$.*

Of course, this is still computing a gradient, which should be natural. But we
are dealing with very special operations (e.g., matrix-vector products), and the
gradient is ultimately going to be expressed in terms of them. Also, this is
$$\mathbb{R}^{n}$$ world, not the nice $$x$$ and $$y$$ world. The generality is
pretty intimidating!

This post (along with a few successors) will be the *post-prerequisite*
prerequisite for working in this subject, given that you've had a calculus and
linear algebra background similar to mine.


[^1]: The book is freely available on Boyd's [site](http://web.stanford.edu/~boyd/cvxbook/), along with a number of other resources.


# Overview: the example $$ \nabla c^T x $$

Ultimately, the only difference between what we learned in calculus and what is
asked of us here is a level of generality. We simply need to perform the basic
steps from before and we will be done. But instead of being given a parameter
parameters $$(x,y,z,\ldots)$$, we have to interpret $$ x $$ as the list itself.
Get ready for subscripting hell!

Let's start with a relatively easy problem. Let $$ c \in \mathbb{R}^n$$ be fixed
and define $$ f(x) = c^T x $$. In other words $$ f(x) $$ is a weighted linear
combination of the elements of $$ x $$. It's the sort of term which arises
naturally in linear programming contexts. We want to compute $$ \nabla f(x) $$,
so we will start by selecting an arbitrary index of $$ x $$ (I'm partial to $$ k
$$, but go nuts), and compute its derivative. We have

$$
\begin{align}
  \frac{\partial}{\partial x_k} f(x) &= 
  \frac{\partial}{\partial x_k} c^T x \\&= 
  \frac{\partial}{\partial x_k} \sum_{i=1}^{n} c_i x_i.
\end{align}
$$

The above is simply by unpacking the $$ c^T x $$ into its component parts, i.e.
$$ c^T x = c_1 x_1 + c_2 x_2 + \cdots + c_{n-1} x_{n-1} + c_n x_n $$. If you
prefer, start off by writing out the terms "explicitly" like this, to make sure
you keep everything straight. Ideally, as you get more comfortable with these
operations, you will switch to the summation form. It's more compact and
ultimately easier to work with. 

Since differentiation is linear, we can write

$$
\frac{\partial}{\partial x_k} \sum_{i=1}^{n} c_i x_i = \sum_{i=1}^{n}
\frac{\partial}{\partial x_k} c_i x_i.
$$

Now we should note a few things that we need to be careful about. First of all,
the summation index is $$ i $$, not $$ k $$. In general these will be distinct,
because they are referring to differen things. Next, let's think through the
evaluation of $$ \frac{\partial}{\partial x_k} c_i x_i $$. If $$ i = k $$, then
this we should have

$$ 
\begin{align}
\frac{\partial}{\partial x_k} c_i x_i &= 
\frac{\partial}{\partial x_k} c_k x_k \\
&= c_k,
\end{align}
$$

but otherwise, $$ c_i x_i $$ will not depend on $$ x_k $$, and so $$
\frac{\partial}{\partial x_k} c_i x_i = 0 $$ in that case. Putting this all
together, we get

$$
\sum_{i=1}^{n} \frac{\partial}{\partial x_k} c_i x_i = c_k,
$$

since every term is $$ 0 $$ except for when $$ i = k $$. So in total, $$
\frac{\partial}{\partial x_k} c^T x = c_k$$. Now, this was the $$ k$$th entry of
the gradient, so we have

$$
\begin{align}
  \nabla f(x) &= \nabla c^Tx \\
  &= \begin{bmatrix} c_1 \\ c_2 \\ \vdots \\ c_{n-1} \\ c_n \end{bmatrix}.
\end{align}
$$

What is this object? Well, the $$k$$th entry of $$\nabla f(x) $$ is $$c_k$$, so
in fact this is nothing other than $$c$$ itself. So 

$$
\nabla c^Tx = c.
$$

By the way, this correctly generalizes our favorite 1-dimensional result:
$$\frac{d}{d x} c x = c $$.

# Summary: How to take a hard(er) gradient

The general procedure, employed here and throughout later posts, is

1. Express $$ f(x) $$ in "coordinate form" (e.g. with explicit summations).
2. Compute $$ \frac{\partial f}{\partial x_k} $$ over the coordinate form.
3. Collect the partial derivatives into the gradient vector.
4. Simplify and interpret the result.

# Addendum: dimension observations

The weight $$ c $$ was an element of $$ \mathbb{R}^{n} $$, which is usually interpreted
to mean that it was a column vector. To form $$ f(x)$$, we flipped $$ c $$ via
transposing into a row vector, and multiplied it by $$x$$. (Of course, this is
so that the multiplication makes sense.) The gradient operation seems to have
flipped it back to a column vector, $$ \nabla f(x) = c $$. 

As we shall see, this is a common thing to expect from linear algebraic functions.

