---
layout: post
title: "Gradients for Grown-Ups (Part 2)"
author: "David Kraemer"
categories: ln 
tags: [math,gradient]
---

This is the second in a series of posts, "Gradients for Grown-Ups". You can see
the previous post [here](gradients-for-grownups-part-01).

Last time, we got started with the example $$ f(x) = c^T x $$ to showcase the
general procedure for computing gradients:

1. Express $$ f(x) $$ in "coordinate form" (e.g. with explicit summations).
2. Compute $$ \frac{\partial f}{\partial x_k} $$ over the coordinate form.
3. Collect the partial derivatives into the gradient vector.
4. Simplify and interpret the result.

This time, we'll cover two more examples, $$ x^T x $$ and $$ x^T A x $$. The
goal is to get more familiar with the general setting of commmon linear algebra
functions.

# Example: $$ f(x) = x^T x $$

You will see the objective function $$ f(x) = x^T x $$ in *many* places in
optimization, because this is another way of writing $$\| x \|_2^2$$. If you
ever plan on analyzing distance minimization, least squares, or other similar
problems, you will end up taking the gradient of $$\| x \|_2^2$$ sooner rather
than later.

Luckily, this is a relatively straightforward computation. First, let's
represent $$ f(x) $$ in coordinate form:

$$
x^T x = \sum_{i=1}^{n} x_i x_i = \sum_{i=1}^{n} x_i^2.
$$

Remember, if the compact summand notation is still too dense, feel free to write
out $$ x_1^2 + x_2^2 + \cdots + x_{n-1}^2 + x_n^2$$. Next, we take the $$k$$th
partial derivative:

$$
\begin{align}
\frac{\partial}{\partial x_k} x^T x &= 
\frac{\partial}{\partial x_k} \sum_{i=1}^{n} x_i x_i \\
&= \sum_{i=1}^{n} \frac{\partial}{\partial x_k}x_i^2.
\end{align}
$$

If $$ i = k $$, then $$\frac{\partial }{\partial x_k} x_k^2 = 2 x_k $$ by the
power rule. Otherwise, as in the previous case, $$\frac{\partial }{\partial x_k} x_i^2 = 0 $$. Therefore,

$$
\sum_{i=1}^{n} \frac{\partial}{\partial x_k}x_i^2 = 2 x_k.
$$

Now, we put the gradient vector together as before:

$$
\begin{align}
\nabla f(x) &= \nabla x^T x \\
&= \begin{bmatrix} 2 x_1 \\ 2 x_2 \\ \vdots \\ 2 x_{n-1} \\ 2 x_{n}
\end{bmatrix}.
\end{align}
$$

Finally, we notice that this column vector is simply $$2x$$. So $$ \nabla x^T x
= 2x$$, which is a generalization of the familiar quadratic rule: $$
\frac{d}{dx} x^2 = 2x$$.

Nice, we're done!

# Example: $$f(x) = x^T A x$$

This example is significantly more tricky, so we will take our time in getting
through it.

Let's think through what $$ x^T A x$$ translates to. First, let's consider the
product $$ A x $$. Now, there are two ways to picture the matrix-vector
multiplication: 

$$
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn} \\
\end{bmatrix}
\begin{bmatrix}
x_1 \\ x_2 \\ \vdots \\ x_n
\end{bmatrix}.
$$

First, matrix-vector multiplication is defined so that the $$k$$th entry of the
result is a dot product of the $$k$$th row of $$A$$ with $$x$$: 

$$
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn} \\
\end{bmatrix}
\begin{bmatrix}
x_1 \\ x_2 \\ \vdots \\ x_n
\end{bmatrix} = 
\begin{bmatrix}
a_{11} x_1 + a_{12} x_2 + \cdots + a_{1n} x_n \\
a_{21} x_1 + a_{22} x_2 + \cdots + a_{2n} x_n \\
\vdots \\
a_{n1} x_1 + a_{n2} x_2 + \cdots + a_{nn} x_n
\end{bmatrix}.
$$

Alternatively, matrix-vector multiplication is defined to be a linear
combination of the columns of $$A$$:

$$
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn} \\
\end{bmatrix}
\begin{bmatrix}
x_1 \\ x_2 \\ \vdots \\ x_n
\end{bmatrix} = 
x_1 
\begin{bmatrix}
a_{11} \\ a_{21} \\ \vdots \\ a_{n1}
\end{bmatrix} + 
x_2 
\begin{bmatrix}
a_{12} \\ a_{22} \\ \vdots \\ a_{n2}
\end{bmatrix} + \cdots +
x_n 
\begin{bmatrix}
a_{1n} \\ a_{2n} \\ \vdots \\ a_{nn}
\end{bmatrix}.
$$

This last interpretation is going to be more helpful for our purposes. Writing
compactly in coordinate form, this is

$$
Ax = \sum_{j=1}^{n} x_j 
\begin{bmatrix} a_{1j} \\ a_{2j} \\ \vdots \\ a_{nj} \end{bmatrix}.
$$

Now we can simply take the inner product $$ x^T (Ax) $$ and put it in coordinate
form:

$$
\begin{align}
x^T(Ax) &= x^T \left( \sum_{j=1}^{n} x_j 
\begin{bmatrix} a_{1j} \\ a_{2j} \\ \vdots \\ a_{nj} \end{bmatrix} \right) \\
&= \sum_{j=1}^{n} x_j \cdot 
\begin{bmatrix} x_1 & x_2 & \cdots & x_n \end{bmatrix}
\begin{bmatrix} a_{1j} \\ a_{2j} \\ \vdots \\ a_{nj} \end{bmatrix} \\
&= \sum_{j=1}^{n} x_j \sum_{i=1}^{n} x_i a_{ij} \\
&= \sum_{i=1}^{n} \sum_{j=1}^{n} a_{ij} x_i x_j.
\end{align}
$$

The trickiness ultimately boils down to the fact that there are two separate
summations going on. When we work with multiple summations, we have to take more
care with the calculations.

Next, we take the partial derivative with respect to $$x_k$$. Let's simplify
notation a bit and use $$\partial_k$$ to mean $$\frac{\partial}{\partial x_k}$$.
We have

$$
\begin{align}
\partial_k (x^T Ax) &= \partial_k \sum_{i=1}^{n} \sum_{j=1}^{n} a_{ij} x_i x_j
\\
&= \sum_{i=1}^{n} \partial_k \sum_{j=1}^{n} a_{ij} x_i x_j.
\end{align}
$$

Let's compute $$ \partial_k \sum_{j=1}^{n} a_{ij} x_i x_j $$ in two cases.
Suppose first that $$ i \ne k $$. Then this is the very simple case of

$$
\partial_k \sum_{j=1}^{n} a_{ij} x_i x_j = a_{ik} x_i.
$$

Now, suppose that $$ i = k $$. Then we have to take a bit more care, but the
computation still goes through (relatively) simply:

$$
\partial_k \sum_{j=1}^{n} a_{ij} x_i x_j = 
2a_{kk} x_k + \sum_{j \ne k} a_{kj} x_j.
$$

Combining these two cases (and noticing that we can replace $$j$$ by $$i$$) in
one sum, we get the very nicely laid out: 

$$
\begin{align}
\partial_k (x^T Ax) &= \sum_{i=1}^{n} \partial_k \sum_{j=1}^{n} a_{ij} x_i x_j
\\
&= \sum_{i=1}^{n} (a_{ik} + a_{ki}) x_i
\end{align}
$$

What does this correspond to for the gradient? Notice that

$$
\begin{align}
(A + A^T)x &= 
\begin{bmatrix} \sum_{i=1}^{n} (a_{ik} + a_{ki}) x_i \end{bmatrix}
\end{align}.
$$

This is exactly $$\nabla (x^T Ax)$$! So

$$
\nabla(x^T Ax) = (A + A^T) x,
$$

and notice that in the special case of $$ A = A^T $$, we have $$\nabla(x^T Ax)
= 2Ax$$. This actually generalizes our work from last time: 

$$
\begin{align}
\nabla(x^T x) &= \nabla( x^T I x) \\
&= 2I x \\
&= 2x
\end{align}.
$$

So far, we have been using the component-based approach outlined above. We take
the $$k$$th partial derivative and put the gradient together from the bottom up.
Next time, we will start to incorporate actual *properties* of the gradient to
make our lives easier.
