---
description: 'Introduction'
sidebar: 'docs'
prev: '/docs/3d/example/'
next: '/docs/2d/science/'
---

# Advance N-Body Simulation

In this simulation, we model the universe using *Dark Matter* only universe, where we consider the DM particles to be collisonless fluid. This simulation uses incorporate Friedmann's Equation and is a more realistics simulation then the previous. This implementation will use Particle mesh method which is faster than calculating individual force pairs, although there are other better optimization like *tree*, *tree-particle-mesh* etc.
The codes for this located in the directory `nbody2d`

## Simulation
The code is structured in the following manner:   

- **Cosmology** : This is for getting the Hubble's Constant and other pramters such as $a$, $\dot{a}$, and $\Omega_i~'s$      
- **Mass deposition** : Particle mesh codes need densiy as a function of the mesh rather the particle mass.      
- **Interpolation** : We need to interpolate back grid quantities onto the particle coordinates.      
- **Integrator** : The evoultion is described by a Hamiltonian System of equation. We will use leap-frog integrator which is agenric solver for such system.        
- **Poisson Solver** :  For solving the Poisson equation governing the evoulution of density.     
- **Intitalization** : The inital perturbation is given by *Zeldovich Apporximation*      
- **Main** : For stiching everything together.

Move to the next section to know how things work.