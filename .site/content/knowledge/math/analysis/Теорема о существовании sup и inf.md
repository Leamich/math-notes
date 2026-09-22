---
title: "Теорема о существовании sup и inf"
---

[[courses/hse/matan/Мат. анализ|Мат. анализ]] › [[knowledge/math/analysis/Основания|Основания]] › [[knowledge/math/analysis/Вещественные числа|Вещественные числа]]

$\forall A \ne \varnothing, A \subset \mathbb{R}, A \text{— огр. сверху (снизу)}\ \exists ! \sup A (\inf A)$

# Д-во

1. единственность — очевидно из [[knowledge/math/analysis/Супремум (инфинум)|опр.]]
2. сущ-ние:
Пусть $A\ne \varnothing, A \subset \mathbb{R}$
$B$ — м-во всех верхних границ $A$, $B \ne \varnothing$ (из огр. сверху $A$), $B \subset \varnothing$.
$$
\begin{gathered}
\forall a \in A,\ \forall b \in B,\ a \leq b \implies\\ \implies \text{A левее B} \xRightarrow{акс. полноты} \exists c \in \mathbb{R}:\ \forall a \in A, \forall b \in B: a\leq c \leq b \implies\\\implies c\text{ — верхняя граница } A \implies c \in B;\ c = \min B \implies c = \sup A
\end{gathered}
$$

**ч.т.д.**
