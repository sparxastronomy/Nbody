# Nbody
This is a repository for N-Body simulation.     
The goal of this simultion to study large scale structures in the universe.     
The code is written entirely in *Python*.       


As of now it is a simple NBody simulation, and Friedmann's Equation and Other optimizations like Particle Mesh, CIC are not implemented yet. You can run this code for having some baasic understanding.        

A dedicated webpage will come soon describing all the steps and working of the code.

## Install
Running this code requires the following dependencies:

- Python3
- Python Libraries
    - **numpy** (For doing computation)
    - **scipy** (For doing computation)
    - **astropy**
    - **numba** (For speeding up computation)
    - **tqdm**  (For keeping track of iterations)
- `pip install -r requirements.txt` will install the dependencies

## Run
For running simple nbody code run this:

    python -m nbody3d.nbody


### Upcoming
- [x] simple Nbody implementation
  - [x] 2D Plots
  - [X] 3D Plots

- [ ] Large scale Nbody simulation
  - [ ] Implementing Cosmology
  - [ ] Implementing Integration Step (Leap-frog)
  - [ ] Implementing Poission solver
  - [ ] Implementing Intial Perturbation
  - [ ] Implementing additional constraints
