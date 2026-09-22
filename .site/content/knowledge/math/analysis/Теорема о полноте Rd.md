---
title: "Теорема о полноте Rd"
---

[[courses/hse/matan/Мат. анализ|Мат. анализ]] › [[knowledge/math/analysis/Метрические пространства|Метрические пространства]] › [[knowledge/math/analysis/Полнота метрических пространств|Полнота метрических пространств]]

$\mathbb{R}^{d}$ — [[knowledge/math/analysis/Полное метрическое пространство|полное пр-во]]
# Док-во
$x_{n}=(x^{(1)}_{n}, \dots, x_{n}^{(d)})$ — фунд. посл-ть, т.е. $\forall \varepsilon>0: \exists N: \forall m, n\geq N: ||x_{n}-x_{m}||<\varepsilon$ $||x_{n}-x_{m}||=\sqrt{(x_{n}^{(1)}-x_{m}^{(1)})^{2}+\dots+(x_{n}^{(d)}-x_{m}^{(d)})^{2}}\geq |x_{n}^{(k)}-x_{m}^{(k)}|$

Следовательно, числ. посл-ть $x_{n}^{(k)}$ фунд $\implies$ у неё есть предел $a^{(k)}:=\lim\limits_{ n \to \infty }x_{n}^{(k)}\implies$ $x_{n}$ покоорд. сх-ся к $a=(a^{(1)}, \dots, a^{(d)})$ $\implies$ сх-ся по норме.
