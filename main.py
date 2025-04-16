import numpy as np
from scipy.integrate import cumtrapz
import matplotlib.pyplot as plt
from orbital_mechanics import compute_position, compute_potential, compute_time_dilation
from time_dilation import plot_time_dilation, plot_dilation_factor, plot_orbit
from em_plasma_sim import plot_magnetic_field
from energy_controller import PIDController
from utils import G, c

# Simulation parameters
M = 1e24  # kg, mass of anchor
a0 = 1e6  # m, initial semi-major axis
b0 = 5e5  # m, initial semi-minor axis
T = 3600  # s, orbital period
omega = 2 * np.pi / T
total_time = 10 * T  # s, total simulation time
dt = 1  # s, time step
t = np.arange(0, total_time, dt)

# PID controller parameters
target_dilation = 0.999  # Target time dilation factor
K_p = 0.1
K_i = 0.01
K_d = 0.05

# Initialize simulation variables
s = 1.0  # Orbit scale factor
controller = PIDController(K_p, K_i, K_d, target_dilation)
tau_you = 0
tau_you_list = []
s_list = []
dilation_list = []
x_list = []
y_list = []

# Simulation loop
for ti in t:
    a_current = s * a0
    b_current = s * b0
    x, y, z = compute_position(ti, a_current, b_current, omega)
    Phi = compute_potential(x, y, z, M, G)
    dilation_factor = compute_time_dilation(Phi, c)
    
    # Update proper time
    tau_you += dilation_factor * dt
    tau_you_list.append(tau_you)
    dilation_list.append(dilation_factor)
    x_list.append(x)
    y_list.append(y)
    
    # Update controller
    ds_dt = controller.update(dilation_factor, dt)
    s += ds_dt * dt
    s_list.append(s)

# Convert lists to arrays for plotting
tau_you_array = np.array(tau_you_list)
s_array = np.array(s_list)
dilation_array = np.array(dilation_list)
x_array = np.array(x_list)
y_array = np.array(y_list)

# Generate plots
plt.figure(figsize=(10, 6))
plt.plot(t, tau_you_array, label='Proper time at center')
plt.plot(t, t, label='Coordinate time')
plt.xlabel('Coordinate time t (s)')
plt.ylabel('Proper time τ (s)')
plt.legend()
plt.savefig('proper_time.png')

plt.figure(figsize=(10, 6))
plt.plot(t, s_array)
plt.xlabel('Time t (s)')
plt.ylabel('Scale factor s')
plt.savefig('scale_factor.png')

plt.figure(figsize=(10, 6))
plt.plot(t, dilation_array)
plt.xlabel('Time t (s)')
plt.ylabel('Time dilation factor')
plt.savefig('dilation_factor.png')

plt.figure(figsize=(10, 6))
plt.plot(x_array, y_array)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Anchor Orbit')
plt.savefig('orbit.png')

# Plot magnetic field at t=0
plot_magnetic_field(t[0], x_array[0], y_array[0], z)
