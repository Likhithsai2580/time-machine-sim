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
    # Set a minimum distance to prevent singularities
    r_min = 1e3  # 1 km minimum distance
    r = max(r, r_min)
    B = (mu0 / (4 * np.pi)) * (3 * np.dot(m, r_vec) * r_vec / r**5 - m / r**3)
    # Check for invalid values
    if not np.all(np.isfinite(B)):
        return np.array([0, 0, 0])
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
    magnitudes = np.zeros_like(X)
    
    for i in range(grid_size):
        for j in range(grid_size):
            B = magnetic_field(X[i,j], Y[i,j], 0, anchor_x, anchor_y, anchor_z)
            Bx[i,j] = B[0]
            By[i,j] = B[1]
            magnitudes[i,j] = np.linalg.norm(B)
    
    # Normalize vectors for plotting
    with np.errstate(divide='ignore', invalid='ignore'):
        Bx_norm = Bx / magnitudes
        By_norm = By / magnitudes
        # Replace NaN with 0 (occurs where magnitude is 0)
        Bx_norm = np.nan_to_num(Bx_norm, nan=0.0)
        By_norm = np.nan_to_num(By_norm, nan=0.0)
    
    plt.figure(figsize=(10, 6))
    plt.quiver(X, Y, Bx_norm, By_norm, magnitudes, scale=50, cmap='viridis')
    plt.colorbar(label='Magnetic Field Magnitude (T)')
    plt.title(f'Magnetic Field at t={t0} s')
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.savefig(f'magnetic_field_t{t0}.png')
    plt.close()
