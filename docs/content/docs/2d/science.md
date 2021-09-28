---
description: 'Science'
sidebar: 'docs'
prev: '/docs/2d/intro/'
next: '/docs/2d/science/'
---

# Maths Required
Deriving all the thing in great detail won't be possible, however I'll try to write reasonable explations for all the steps. For detailed text one should refer to Barbara Ryden's book "Introduction to Cosmology" and Andrew Liddle's book "Introduction to Modern Cosmology".
</br>
<br>
Since we are considering the universe to be dominated by the darkmatter, the dynamics is governed by the hydrodynamic equations:
$$
\large
\begin{aligned}
    \partial_t(r) + \nabla_r(\rho \vec{u}) &= 0\\
    \partial_t\vec{u} + (\vec{u}\cdot\nabla_r)\vec{u} &= -\nabla_r\phi\\
    \nabla_r^2\Phi &= 4\pi G\rho
\end{aligned}
$$
Now, the comoving coordinate is defined by:      
$$
\large
\vec{r} = a(t)\vec{x}
$$  

where $\vec{r}$ is the real distance and $\vec{x}$ is the co-moving coordinate, and $a(t)$ is called the scale factor of the universe. So on moving from real to comoving coordinates, and considering a densitity perturbation
$$
    \large
    \delta+1 = \frac{\rho}{\rho_b}
$$  

the above equations will change. The equation that we are interested in is the modififed poisson's equation.
$$
    \large
    \nabla\phi = 4\pi Ga^2(\rho - \rho_b)=4\pi Ga^2(\delta\rho_b)
$$
where   
$$
    \large
    \Phi = \underbrace{\frac{2}{3}\pi G\rho_ba^2x^2}_{\substack{\text{background potential}\\\text{of homogenous universe}}} + \underbrace{\phi}_{\text{peculier potential}}
$$
Now the First Friedmann's Equation is 
$$
    \large
    \mathcal{H}^2 = \frac{8\pi G}{3}\rho_ba^2 - k
$$      
So for the flat universe ($k=0$) we can write the poisson equation as:
$$
\large
    \Delta\phi=4\pi Ga^2(\delta\rho_b) = \frac{3}{2}\Omega_m\mathcal{H}^2\delta
$$
Where $\Omega_i$ is a dimensionless quantity defined by 
$$
    \large
    \Omega_i = \dfrac{\rho_i}{\rho_{i,critical}}
$$
