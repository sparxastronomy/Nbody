import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from numba import jit
from tqdm import tqdm


@jit(nopython=False)
def accleration(pos, mass, G, softening):
    """
    Calculate the acceleration on each particle due to Newton's Law 
    parameters:
    ------------------------------------
    pos  :  N x 3 matrix of positions
    mass :  N x 1 vector of masses
    G    :  Newton's Gravitational constant
    softening : softening length

    Returns:
    ------------------------------------
    a    :  N x 3 matrix of accelerations
    """
    # positions r = [x,y,z] for all particles
    x = pos[:, 0:1]
    y = pos[:, 1:2]
    z = pos[:, 2:3]

    # matrix that stores all pairwise particle separations: r_j - r_i
    dx = x.T - x
    dy = y.T - y
    dz = z.T - z

    # matrix that stores 1/r^3 for all particle pairwise particle separations
    inv_r3 = (dx**2 + dy**2 + dz**2 + softening**2)
    inv_r3[inv_r3 > 0] = inv_r3[inv_r3 > 0]**(-1.5)

    ax = G * (dx * inv_r3) @ mass
    ay = G * (dy * inv_r3) @ mass
    az = G * (dz * inv_r3) @ mass

    # pack together the acceleration components
    a = np.hstack((ax, ay, az))

    return a


@jit(nopython=False)
def energy(pos, vel, mass, G):
    """
    Get kinetic energy (KE) and potential energy (PE) of simulation
    pos is N x 3 matrix of positions
    vel is N x 3 matrix of velocities
    mass is an N x 1 vector of masses
    G is Newton's Gravitational constant
    KE is the kinetic energy of the system
    PE is the potential energy of the system
    """
    # Kinetic Energy:
    KE = 0.5 * np.sum(np.sum(mass * vel**2))

    # Potential Energy:

    # positions r = [x,y,z] for all particles
    x = pos[:, 0:1]
    y = pos[:, 1:2]
    z = pos[:, 2:3]

    # matrix that stores all pairwise particle separations: r_j - r_i
    dx = x.T - x
    dy = y.T - y
    dz = z.T - z

    # matrix that stores 1/r for all particle pairwise particle separations
    inv_r = np.sqrt(dx**2 + dy**2 + dz**2)
    inv_r[inv_r > 0] = 1.0/inv_r[inv_r > 0]

    # sum over upper triangle, to count each interaction only once
    PE = G * np.sum(np.sum(np.triu(-(mass*mass.T)*inv_r, 1)))

    return KE, PE


def main(N, tEnd, dt, softening=0.1, energyplot=False, plotRealTime=True):
    """
    N-body simulation main function
    Imput
    ------------------------------- 
    N            : Number of particles to simulate
    time         : Time at which simulation ends
    dt           : time step
    s            : Softening length, default = 0.1
    energyplot   : Switch to plot energy evolution diagram
    plotRealTime : Switch for plotting as the simulation goes along
    """

    # Simulation parameters
    t = 0                # current time of the simulation
    G = 6.674*1e-11      # Newton's Gravitational Constant
    plotRealTime = True  # switch on for plotting as the simulation goes along

    # Generate Initial Conditions

    mass = 100.0*np.ones((N, 1))/N  # total mass of the system is 100
    # randomly selected positions and velocities
    #pos = np.random.randn(N, 3)
    vel = np.random.randn(N, 3)

    # for uniform grid of particles
    pos = np.zeros((N, 3))  # creating a null arry

    # creating uniformly spaced grid
    count = 0
    maxindex = int(np.ceil(np.power(N, 1/3)))  # uniform grid-size
    for z in range(maxindex):
        for y in range(maxindex):
            for x in range(maxindex):
                pos[count] = [x, y, z]  # assigning to array
                count += 1
    # getting perturbations for grid
    a = np.random.randn(N, 3) \
        + np.random.uniform(low=-1.0, high=1.0, size=(N, 3))
    # adding perturbations to the grid
    pos = pos + (a/np.max(np.abs(a)))

    del(a)

    # Convert to Center-of-Mass frame
    vel -= np.mean(mass * vel, 0) / np.mean(mass)

    # calculate initial gravitational accelerations
    acc = accleration(pos, mass, G, softening)

    # calculate initial energy of system
    if energyplot == True:
        KE, PE = energy(pos, vel, mass, G)

    # number of timesteps
    Nt = int(np.ceil(tEnd/dt))

    # save energies, particle orbits for plotting trails
    # array for saving postions
    pos_save = np.zeros((N, 3, Nt+1))
    pos_save[:, :, 0] = pos

    # arrays for saving energyies
    if energyplot == True:
        KE_save = np.zeros(Nt+1)
        KE_save[0] = KE
        PE_save = np.zeros(Nt+1)
        PE_save[0] = PE

    # creating timestamps
    t_all = np.arange(Nt+1)*dt

    # preparing figure
    fig = plt.figure(figsize=(10, 10), dpi=200)
    ax1 = plt.axes(projection="3d")

    # Simulation Main Loop
    for i in range(Nt):
        # (1/2) kick
        vel += acc * dt/2.0

        # drift
        pos += vel * dt

        # update accelerations
        acc = accleration(pos, mass, G, softening)

        # (1/2) kick
        vel += acc * dt/2.0

        # update time
        t += dt

        # get energy of system
        if energyplot == True:
            KE, PE = energy(pos, vel, mass, G)

        # save energies, positions for plotting trail
        pos_save[:, :, i+1] = pos
        if energyplot == True:
            KE_save[i+1] = KE
            PE_save[i+1] = PE

        # plot in real time
        if plotRealTime or (i == Nt-1):
            plt.sca(ax1)
            plt.cla()
            # Next for lines are for plotting trails. Not adviseable for large N
            #xx = pos_save[:, 0, max(i-50, 0):i+1]
            #yy = pos_save[:, 1, max(i-50, 0):i+1]
            #zz = pos_save[:, 2, max(i-50, 0):i+1]
            # ax1.scatter3D(xx, yy, zz, s=5, color=[.3, 0.5, 1, 0.2])    #plotting trail
            ax1.scatter3D(pos[:, 0], pos[:, 1], pos[:, 2],
                          s=5, c=(pos[:, 2]), cmap='nipy_spectral')

            ax1.set_title('time = %5.2f seconds' % t)
            ax1.set_xlabel('x')
            ax1.set_ylabel('y')
            ax1.set_zlabel('z')
            ax1.azim, ax1.elev = 60, 30
            plt.pause(0.000001)

    # adding proper labels to the plot and saving
    plt.sca(ax1)
    ax1.scatter3D(pos[:, 0], pos[:, 1], pos[:, 2], s=5,
                  c=(pos[:, 2]), cmap='nipy_spectral')
    plt.xlabel('x-coordinates', fontsize=8)
    plt.ylabel('y-coordinates', fontsize=8)
    ax1.set_zlabel('z', fontsize=8)

    plt.setp(ax1.get_xticklabels(), fontsize=6)
    plt.setp(ax1.get_yticklabels(), fontsize=6)
    plt.setp(ax1.get_zticklabels(), fontsize=6)

    ax1.azim, ax1.elev = 60, 30  # orientatation of the plot
    plt.title('Nbody Simulation, N='+str(N) +
              ' Time = %5.2f s' % tEnd, fontsize=10)

    # Saving figure
    plt.savefig('nbody'+str(N)+'.png', dpi=200, bbox_inches='tight')
    plt.show()

    # energy evolution
    if energyplot == True:
        # normalizers for  energy diagram
        max1 = np.max(np.abs(KE_save))
        max2 = np.max(np.abs(PE_save))
        max_e = np.max([max1, max2])

        plt.figure(2, figsize=(5, 3), dpi=200)
        plt.scatter(t_all, KE_save/max_e, color='red', s=1,
                    label='KE' if i == Nt-1 else "")
        plt.scatter(t_all, PE_save/max_e, color='blue', s=1,
                    label='PE' if i == Nt-1 else "")
        plt.scatter(t_all, (KE_save+PE_save)/max_e, color='black',
                    s=1, label='Etot' if i == Nt-1 else "")
        plt.xlim((0, tEnd))
        plt.xlabel('Time', fontsize=8)
        plt.ylabel('Energy', fontsize=8)
        plt.title('Energy evolution', fontsize=10)
        plt.legend(loc=1)
        # saving energy diagram
        plt.savefig('nbody'+str(N)+'eng.png', dpi=200, bbox_inches='tight')
        plt.show()

    return 0


if __name__ == "__main__":
    # main()
    main(N=1000, tEnd=4.0, dt=0.1)
    # main_sim(10)
