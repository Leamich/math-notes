---
title: "Лемма о линеаризации bias"
tags:
  - понятие
---

[[courses/hse/matstat/Математическая статистика|Математическая статистика]] › [[knowledge/math/matstat/Дельта-методы|Дельта-методы]]

Пусть $a_{n}\to 0$, $a_{n}\geqslant 0$ и с.в. $Y_{n}=y+\mathcal{O}_{\mathbb{P}}(a_{n})$ (см. [[knowledge/math/matstat/Символы Ландау для случайных величин|Символы Ландау для случайных величин]])

$h:\mathbb{R}\to \mathbb{R}$ дифф. в т. $y$.

Тогда 
$$
h(Y_{n})-h(y)=h'(y)(Y_{n}-y)+o_{\mathbb{P}}(a_{n})
$$

В частности, $h'(y)=0\implies h(Y_{n})-h(y)=o_{\mathbb{P}}(a_{n})$.

## Док-во

Заметим, что $Y_{n}\overset{\mathbb{P}}{\to} y$ (по св-вам [[knowledge/math/matstat/Символы Ландау для случайных величин|отсюда]]).

Введем ф-ю
$$
r(x):= \frac{h(x)-h(y) - h'(y)(x-y)}{x-y} \cdot \mathbb{1}[x \neq y]
$$

Тогда $r(x)\overset{x\to y}{\to} 0$ (по опр. [[knowledge/math/analysis/Дифференцируемость функции|Дифференцируемость функции]]), т.е. $r$ непр. в $x=y$. Тогда
$$
h(x)-h(y) = h'(y)(x-y)+r(x)(x-y)
$$

При подстановке $x=Y_{n}$: $r(Y_{n})\overset{\mathbb{P}}{\to} r(y)=0\iff r(Y_{n})=o_{\mathbb{P}}(1)$. Тогда 
$$
r(Y_{n})(Y_{n}-y)=o_{\mathbb{P}}(1)\cdot \mathcal{O}_{\mathbb{P}}(a_{n})=o_{\mathbb{P}}(a_{n})
$$


## Опирается на

- [[knowledge/math/matstat/Символы Ландау для случайных величин|Символы Ландау для случайных величин]]

## Используется в

- [[knowledge/math/matstat/Дельта-метод|Дельта-метод]]
