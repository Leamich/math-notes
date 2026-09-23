---
title: "Степень в th Берри-Эссеена"
tags:
  - понятие
---

[[courses/hse/probability/Теория вероятностей|Теория вероятностей]] › [[knowledge/math/probability/Элементарная ТВ|Элементарная ТВ]] › [[knowledge/math/probability/Предельные теоремы|Предельные теоремы]]

(см. [[knowledge/math/probability/Интегральная теорема Муавра-Лапласа|Интегральная теорема Муавра-Лапласа]])

Почему в [[knowledge/math/probability/Теорема Берри-Эссеена|Теорема Берри-Эссеена]] нельзя в оценке степень $n$ в знаменателе $\leqslant \frac{1}{2}$?

$p=\frac{1}{2}$

$$
\begin{gathered}
\mathbb{P}(S_{2n}<n)+\mathbb{P}(S_{2n}=n)+P(S_{2n}>n)=1\\
2\mathbb{P}(S_{2n}<n)+\mathbb{P}(S_{2n}=n)=1\\
2\mathbb{P}(S_{2n}<n)+\binom{2n}{n}\cdot \left( \frac{1}{2} \right)^{2n}\sim \frac{1}{\sqrt{\pi n}}\\
\mathbb{P}(S_{2n}\leqslant n)=\frac{1}{2}+\frac{1}{2\sqrt{\pi n}}+o\left( \frac{1}{\sqrt{n}} \right)\\
\begin{gathered}
\mathbb{P}(S_{2n}\leqslant n) - \underbrace{ \frac{1}{\sqrt{2\pi}}\int\limits_{-\infty}^{0} e^{ -x^{2}/2 }\,dx }_{ =\frac{1}{2} }=\\=\mathbb{P}(S_{2n}\leqslant n)-\frac{1}{2}+o\left( \frac{1}{\sqrt{n}} \right)\sim \frac{1}{2\sqrt{\pi n}}
\end{gathered}
\end{gathered}
$$
(см. [[knowledge/math/analysis/Формула Валлиса#Следствие|Формула Валлиса]])
