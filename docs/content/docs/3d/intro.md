---
description: 'Simple Nbody Simulation'
sidebar: 'docs'
prev: '/docs/installation/'
next: '/docs/3d/science/'
---

# Introduction
This is a simple Nbody simulation, without any expansion or whatsoever. The code is a simple implementation of particle - pair method, where force is computed for each pair and then summed over for each such pair. After that using the Leapfrog integration we calculate the postion and velocity, and iterate over again. 
You can run this code by        

```bash
cd nbody3d
python -m nbody_optimized
```

The script `nbody_optimzed.py` is optimzed using numba. The script to begin execution may take a couple of seconds, however the rest of the  iterations are very fast. There is one another script in this folder `nbody.py`; this script is not optimized. You can play between these two.         
Navigate to the working page, to know how the script is written.  The script is well commented.