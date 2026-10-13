"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)

data = np.loadtxt('freefall.csv', delimiter=',', skiprows=1)

t = data[:,0]
y = data[:,1]

# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?
v = np.gradient(y, t)
a = np.gradient(v, t)

mean_a = np.mean(a)
print(f"Mean acceleration: {mean_a:.2f} m/s^2")

# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)

v_rec = cumulative_trapezoid(a, t, initial= 0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial= 0) + y[0]

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png

import matplotlib.pyplot as plt

# Create 3 stacked subplots sharing the same x-axis
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

# Panel 1: Position
ax1.plot(t, y, color='blue', label='Position y(t)')
ax1.set_ylabel('Position (m)')
ax1.legend(loc='upper right')
ax1.grid(True)

# Panel 2: Velocity
ax2.plot(t, v, color='orange', label='Velocity v(t)')
ax2.set_ylabel('Velocity (m/s)')
ax2.legend(loc='upper right')
ax2.grid(True)

# Panel 3: Acceleration
ax3.plot(t, a, color='green', alpha=0.6, label='Acceleration a(t)')
ax3.axhline(-9.81, color='red', linestyle='--', label='Theoretical g (-9.81)')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Acceleration (m/s²)')
ax3.legend(loc='upper right')
ax3.grid(True)

plt.tight_layout()
plt.savefig('motion.png')
plt.show()
