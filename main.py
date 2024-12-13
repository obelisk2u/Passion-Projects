import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
M_earth = 5.972e24  # Mass of Earth (kg)
M_moon = 7.342e22  # Mass of Moon (kg)
R_earth_moon = 384400e3  # Distance between Earth and Moon (m)
T_orbit = 27.3 * 24 * 3600  # Orbital period of the Moon (seconds)

# Initial conditions
r_earth = np.array([0.0, 0.0])  # Earth at the origin
r_moon = np.array([R_earth_moon, 0.0])  # Moon's initial position
v_earth = np.array([0.0, 0.0], dtype=np.float64)  # Earth initially stationary (as float64)
v_moon = np.array([0.0, 1022.0], dtype=np.float64)  # Moon's velocity (approx. in m/s) (as float64)

# Time parameters
dt = 1000  # Time step (seconds)
steps = 10000  # Number of simulation steps

# Function to compute the gravitational force between the Earth and Moon
def gravitational_force(r1, r2, m1, m2):
    r = r2 - r1
    dist = np.linalg.norm(r)
    F = G * m1 * m2 / dist**2
    return F * r / dist

# Initialize arrays for storing the positions
earth_positions = [r_earth]
moon_positions = [r_moon]

# Simulation loop
for _ in range(steps):
    # Calculate forces
    F = gravitational_force(r_earth, r_moon, M_earth, M_moon)
    
    # Update velocities
    a_earth = F / M_earth
    a_moon = -F / M_moon
    
    v_earth += a_earth * dt
    v_moon += a_moon * dt
    
    # Update positions
    r_earth += v_earth * dt
    r_moon += v_moon * dt
    
    earth_positions.append(r_earth.copy())
    moon_positions.append(r_moon.copy())

earth_positions = np.array(earth_positions)
moon_positions = np.array(moon_positions)

# Plotting the simulation using matplotlib
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-500e6, 500e6)
ax.set_ylim(-500e6, 500e6)
ax.set_xlabel('X position (m)')
ax.set_ylabel('Y position (m)')

# Earth and Moon plots
earth_dot, = ax.plot([], [], 'go', markersize=10)  # Earth in green
moon_dot, = ax.plot([], [], 'bo', markersize=5)   # Moon in blue

# Function to update the plot in the animation
def update(frame):
    earth_dot.set_data((earth_positions[frame, 0], earth_positions[frame, 1]))
    moon_dot.set_data((moon_positions[frame, 0], moon_positions[frame, 1]))
    return earth_dot, moon_dot

# Create the animation
ani = FuncAnimation(fig, update, frames=range(0, steps, 10), interval=50, blit=True)

# Save the animation to a file (e.g., MP4)
ani.save('earth_moon_orbit.mp4', writer='ffmpeg', fps=30)

