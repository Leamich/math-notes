---
type: concept
kind: theorem
status: done
up: "[[Криволинейные интегралы]]"
tags: []
---
$\omega=f_{1}dx_{1}+\dots+f_{n}dx_{n}$ (см. [[Дифференциальная форма 1-го порядка]]), $\gamma:[a,b]\to \mathbb{R}^{n}$
$\int\limits_{\gamma} \omega:=\int\limits_{a}^{b}\sum\limits_{k=1}^{n}f_{k}(\gamma(t))\gamma'_{k}(t)\,dt$ (см. [[Криволинейный интеграл II рода]])

1. не зависит от параметризации
2. при смене направления меняет знак
>[!note]- Док-во 1-2
> Возьмём $\gamma:[a,b]\to \mathbb{R}^{n},\ \tilde{\gamma}:[c, d]\to \mathbb{R}^{n}$
> $\gamma=\tilde{\gamma}\circ \tau$, где $\tau:[a, b]\to [c, d]$ строг. возр. биекц.
> 
> $$
> \int\limits _{\tilde{\gamma}}\omega=\int\limits_{c}^{d} \sum\limits_{k=1}^{n} f_{k}(\tilde{\gamma}(t))\tilde{\gamma}'_{k}(t)\,dt=[t=\tau(u)]=\int\limits_{a}^{b} \sum\limits_{k=1}^{n} f_{k}(\tilde{\gamma}(\tau(u)))\tilde{\gamma}'_{k}(\tau(u))\tau'(u)\,du=\int\limits _{\gamma}\omega
> $$
> (прич. если $\gamma=\tilde{\gamma}$, но в обр. порядке, то там поменяется порядок, так что вылезет минус).
3. $\vec{f}=\begin{pmatrix}f_{1}\\\dots\\f_{n}\end{pmatrix}\implies \int\limits_{\gamma} \omega=\int\limits_{\gamma} \langle \vec{f}, \vec{\sigma} \rangle\,ds$, где $\vec{\sigma}$ — един. касат. вектор (идущ. по напр. движения)
>[!note]- Док-во
> $$
> \int\limits _{\gamma}\omega=\int\limits_{a}^{b} \sum\limits_{k=1}^{n}f_{k}(\gamma(t))\gamma_{k}'(t)\,dt
> $$
> $$
> \int\limits _{\gamma}\langle \vec{f}, \vec{\sigma} \rangle\,ds=\int\limits_{a}^{b} \langle \vec{f}(\gamma(t)),\vec{\sigma}(\gamma(t)) \rangle \lVert \gamma'(t) \rVert\,dt= 
> $$
> $\vec{\sigma}(\gamma(t))=\frac{\gamma'(t)}{\lVert \gamma'(t) \rVert}$
> $$
> =\int\limits_{a}^{b} \langle \vec{f}(\gamma(t)),\gamma'(t) \rangle\,dt 
> $$
4. (линейность) $\alpha, \beta \in \mathbb{R};\omega_{1}, \omega_{2}$ — дифф. ф. $\implies \int\limits_{\gamma} (\alpha\omega_{1}+\beta\omega_{2})=\alpha \int\limits_{\gamma}\omega_{1}+\beta \int\limits\omega_{2}$
5. (аддитивность по крив.) $\gamma_{1}:=\gamma \bigg|_{[a, c]}^{},\ \gamma_{2}:=\gamma \bigg|_{[c, b]}^{}$, $\int\limits_{\gamma} f\,ds=\int\limits_{\gamma_{1}} \omega+\int\limits_{\gamma_2} \omega$
>[!note] Док-во 4-5 из (3) + [[Свойства интеграла по длине дуги]]
6. $\left\lvert  \int\limits_{\gamma}\omega  \right\rvert\leqslant \int\limits_{\gamma}\lVert \vec{f} \rVert\,ds\leqslant\text{длина }\gamma\cdot \max\lVert \vec{f} \rVert$
>[!note]- Док-во
> $$
> \left\lvert  \int\limits _{\gamma}\omega  \right\rvert=\left\lvert  \int\limits _{\gamma}\langle \vec{f}, \vec{\sigma} \rangle \,ds  \right\rvert\leqslant \int\limits _{\gamma}\lvert \langle \vec{f}, \vec{\sigma} \rangle  \rvert \,ds\leqslant \int\limits_{\gamma} \lVert \vec{f} \rVert \cdot \underbrace{ \lVert \vec{\sigma} \rVert }_{ =1 } \,ds  
> $$

