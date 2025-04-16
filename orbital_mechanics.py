import numpy as np

def compute_position(t, a, b, omega):
    """
    Compute the position of the gravity anchor in an elliptical orbit.
    
    Args:
        t (float): Time (s)
        a (float): Semi-major axis (m)
        b (float): Semi-minor axis (m)
        omega (float): Angular velocity (rad/s)
    
    Returns:
        tuple: (x, y, z) coordinates (m)
    """
    x = a * np.cos(omega * t)
    y = b * np.sin(omega * t)
    z = 0
    return x, y, z

def compute_potential(x, y, z, M, G):
    """
    Compute the gravitational potential at the center due to the anchor.
    
    Args:
        x, y, z (float): Position of the anchor (m)
        M (float): Mass of the anchor (kg)
        G (float): Gravitational constant (m^3 kg^-1 s^-2)
    
    Returns:
        float: Gravitational potential (m^2 s^-2)
    """
    r = np.sqrt(x**2 + y**2 + z**2)
    return -G * M / r if r > 0 else 0

def compute_time_dilation(Phi, c):
    """
    Compute the gravitational time dilation factor.
    
    Args:
        Phi (float): Gravitational potential (m^2 s^-2)
        c (float): Speed of light (m/s)
    
    Returns:
        float: Time dilation factor
    """
    return np.sqrt(1 + 2 * Phi / c**2)
