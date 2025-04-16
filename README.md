# Time Machine Simulation

This repository contains a collection of Python scripts for simulating time dilation and orbital mechanics. The main purpose of this repository is to provide a simulation environment for studying the effects of gravitational time dilation and magnetic fields on an orbiting anchor.

## Features

- Simulate gravitational time dilation for an orbiting anchor
- Compute and plot magnetic fields
- Implement a PID controller for managing the simulation
- Generate various plots for visualization

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/anony45-everywhere/time-machine-sim.git
   cd time-machine-sim
   ```

## Running the Simulation

To run the simulation, execute the `main.py` script:
```bash
python main.py
```

This will generate several plots, including proper time, scale factor, time dilation factor, and the orbit of the anchor.

## Scripts Overview

- `main.py`: The main entry point for the simulation, integrating various modules.
- `em_plasma_sim.py`: Handles magnetic field calculations and plotting.
- `energy_controller.py`: Defines a PID controller for managing the simulation.
- `orbital_mechanics.py`: Contains functions for computing positions and gravitational potential.
- `time_dilation.py`: Provides plotting functions for time dilation and orbits.
- `utils.py`: Defines physical constants used in the simulation.

## License

This repository is licensed under the MIT License. See the `LICENSE` file for more details.
