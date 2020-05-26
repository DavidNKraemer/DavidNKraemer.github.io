---
layout: post
title: "Compactness and measurability: pitfalls"
author: "David Kraemer"
categories: ln
tags: [compact,measurable,analysis,topology]
---

I am an applied math guy. When I think of compactness, my intuition tells me
"closed and nice". When I'm in Euclidean spaces, I fall back quickly on the
interpretation of "nice" as bounded. In more general metric spaces, "nice" means
that I can conjure convergent sequences out of thin air. On the other hand, in
the general setting, compactness roughly translates to "topologically finite."
That *sounds* like a "nice" property at first glance. Instead, it's a classic
trap of terminology of point-set topology.

An interesting fact about Hausdorff topological spaces is that every compact set
is closed. I think the confusion about compactness being "nice" can be traced to
the Hausdorff property. It's a siren song that leads you astray. For you see,
dear reader, without the Hausdorff property compactness is an ugly, dirty word.

Let's start with the basic point. If we take any set $X$ which has at least two
points, and we assign to $X$ the trivial topology $\Omega = \{\emptyset, X\}$,
then every finite subset is compact. (Indeed, these are always so.) In
particular, the singletons are compact. But they *aren't closed*! We already
find that it is easy to construct non-closed compact sets in the absence
proper separability axioms.

It gets worse, of course. Let's be concrete and suppose $X = \mathbb{R}$. Let $A
\subseteq \mathbb{R}$ be an arbitrary subset of the line, and suppose
$\{U_\alpha\}_{\alpha \in I}$ is an open cover for $A$. What could $U_\alpha$
possibly be? In the trivial topology, it's either $\emptyset$ or $X$ itself. If
$A$ is not an empty set, then there must be $U_\alpha = X$ for some $\alpha$. In
that case, $A \subseteq U_\alpha$, so $A$ is compact. *Every subset of
$\mathbb{R}$ is compact in this topology!*

"Okay, David", I hear you say. "The trivial topology only exists so that you can
create tricky counterexamples. If you put more separation structure on your
topological space, this pathology will disappear."

Oh, to be young and naive. 

With $X = \mathbb{R}$ as before, take $\Omega$ to be the topology of cofinite
sets (and $\emptyset$). This space now satisfies $T_1$: if $x, y \in \mathbb{R}$
are distinct, then $\mathbb{R} \setminus \{x\}$ is an open set which misses $x$
and $\mathbb{R} \setminus \{y\}$ is an open set which misses $y$. 
