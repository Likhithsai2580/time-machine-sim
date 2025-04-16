import numpy as np
import matplotlib.pyplot as plt

mu0 = 4 * np.pi * 1e-7  # Magnetic constant (T m / A)
m = np.array([0, 0, 1e6])  # Magnetic moment (A m^2)

def magnetic_field(x, y, z, anchor_x, anchor_y, anchor_z):
    """
    Compute magnetic field due to the anchor's magnetic moment.
    
    Args:
        x, y, z (float): Field point coordinates (m)
        anchor_x, anchor_y, anchor_z (float): Anchor position (m)
    
    Returns:
        array: Magnetic field vector (T)
    """
    r_vec = np.array([x - anchor_x, y - anchor_y, z - anchor_z])
    r = np.linalg.norm(r_vec)
    if r < 1e-6:  # Avoid singularity
        return np.array([0, 0, 0])
    B = (mu0 / (4 * np.pi)) * (3 * np.dot(m, r_vec) * r_vec / r**5 - m / r**3)
    return B

def plot_magnetic_field(t0, anchor_x, anchor_y, anchor_z, grid_size=20):
    """
    Plot the magnetic field in the xy-plane at a given time.
    
    Args:
        t0 (float): Time for anchor position (s)
        anchor_x, anchor_y, anchor_z (float): Anchor position (m)
        grid_size (int): Number of grid points
    """
    x_grid = np.linspace(-2e6, 2e6, grid_size)
    y_grid = np.linspace(-1e6, 1e6, grid_size)
    X, Y = np.meshgrid(x_grid, y_grid)
    Bx = np.zeros_like(X)
    By = np.zeros_like(X)
    
    for i in range(grid_size):
        for j in range(grid_size):
            B = magnetic_field(X[i,j], Y[i,j], 0, anchor_x, anchor_y, anchor_z)
            Bx[i,j] = B[0]
            By[i,j] = B[1]
    
    plt.figure(figsize=(10, 6))
    plt.quiver(X, Y, Bx, By)
    plt.title(f'Magnetic Field at t={t0} s')
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.savefig(f'magnetic_field_t{t0}.png')
