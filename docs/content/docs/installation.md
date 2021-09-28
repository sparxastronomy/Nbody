---
description: ''
sidebar: 'docs'
prev: '/docs/'
next: '/docs/3d/intro/'
---

# Installation

Getting started with it is really simple. All you need to do is clone this repository 

```bash
gh repo clone sparxastronomy/Nbody
```

and make sure that you have the following python libraries installed:
- Python 3.8
- Numpy (For doing computation)
- Numba (For speeding up computation)
- Matplolib
- Astropy 
- tqdm (For keeping track of iterations)

You can easily install them all at once using
```bash
pip install -r requirements.txt
```

The following list of features are implemented and some are yet to be implemented:
### Implemented
- [x] simple Nbody implementation
  - [x] 2D Plots
  - [X] 3D Plots

### Upcoming
- [ ] Large scale Nbody simulation
  - [ ] Implementing Cosmology
  - [ ] Implementing Integration Step (Leap-frog)
  - [ ] Implementing Poission solver
  - [ ] Implementing Intial Perturbation
  - [ ] Implementing additional constraints

Now you can navigate to Simple 3D Nbody simulation or more advance 2D Nbody simulation to learn more.
