import matplotlib.pyplot as plt

def plot_time_dilation(t, tau):
    """
    Plot proper time vs coordinate time.
    
    Args:
        t (array): Coordinate time array (s)
        tau (array): Proper time array (s)
    """
    plt.figure(figsize=(10, 6))
    plt.plot(t, tau, label='Proper time at center')
    plt.plot(t, t, label='Coordinate time')
    plt.xlabel('Coordinate time t (s)')
    plt.ylabel('Proper time τ (s)')
    plt.legend()
    plt.savefig('proper_time_plot.png')

def plot_dilation_factor(t, dilation_factor):
    """
    Plot time dilation factor over time.
    
    Args:
        t (array): Time array (s)
        dilation_factor (array): Time dilation factor array
    """
    plt.figure(figsize=(10, 6))
    plt.plot(t, dilation_factor)
    plt.xlabel('Time t (s)')
    plt.ylabel('Time dilation factor')
    plt.savefig('dilation_factor_plot.png')

def plot_orbit(x, y):
    """
    Plot the orbit of the anchor.
    
    Args:
        x (array): x-coordinates (m)
        y (array): y-coordinates (m)
    """
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Anchor Orbit')
    plt.savefig('orbit_plot.png')
