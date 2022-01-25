import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


from GRF import fftpoints, gaussian_random_field
n = 256
x, y, z = np.mgrid[:n, :n, :n]
grid = []
for i in tqdm(range(n), "Iteration:"):
    grf = gaussian_random_field(alpha=1.7, size=n, Normalize=True)
    grid = np.append(grid, grf)

fig = plt.figure(figsize=(7, 7), dpi=100)
ax = plt.axes(projection="3d")

ax.scatter(x, y, z,
           c=grid.flatten(), s=1, alpha=0.3)

plt.show()
