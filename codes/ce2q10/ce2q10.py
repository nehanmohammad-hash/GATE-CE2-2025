# By Nehan mohammad
# 05-October-26, Monday, question no: village_triangle

import matplotlib.pyplot as plt
import numpy as np
import subprocess
from funcs import *
from params import *

# Triangle PQR with vertices
# Q = (0, 0), R = (14, 0), P = (5, 12)
Q = np.array([[0], [0]])
R = np.array([[14], [0]])
P = np.array([[5], [12]])

# Calculations
a, b, c = 14, 15, 13
s = (a + b + c) / 2
area = np.sqrt(s * (s - a) * (s - b) * (s - c))
h_a = (2 * area) / a

print(f"Area of Triangle: {area} sq km")
print(f"Minimum connecting road length (Altitude): {h_a} km")

# Generate line segments using the custom line_gen function
line_PQ = line_gen(P, Q)
line_QR = line_gen(Q, R)
line_RP = line_gen(R, P)

# Foot of the altitude from P onto QR (Base QR lies on the x-axis, so foot is at (5, 0))
Foot = np.array([[5], [0]])
line_altitude = line_gen(P, Foot)

# Generate and save triangle geometry figure
plt.figure(figsize=(7, 6))

# Plot triangle sides using custom generated points
plt.plot(line_PQ[0, :], line_PQ[1, :], 'b-', linewidth=1.5)
plt.plot(line_QR[0, :], line_QR[1, :], 'b-', linewidth=1.5)
plt.plot(line_RP[0, :], line_RP[1, :], 'b-', linewidth=1.5)

# Plot altitude
plt.plot(line_altitude[0, :], line_altitude[1, :], 'r--', linewidth=0.8, label=f'Altitude = {h_a:.1f} km')

plt.text(-0.8, -0.6, 'Q (0,0)', fontsize=9)
plt.text(13.5, -0.6, 'R (14,0)', fontsize=9)
plt.text(4.5, 12.4, 'P (5,12)', fontsize=9)

plt.xlim(-2, 16)
plt.ylim(-2, 14)
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

plt.legend(fontsize=9)
plt.title('Village Triangle PQR and Connecting Road', fontsize=10)
plt.xlabel('X Coordinate (km)', fontsize=9)
plt.ylabel('Y Coordinate (km)', fontsize=9)

plt.savefig('../../figs/village_triangle.png', dpi=300, bbox_inches='tight')

# subprocess.run(['termux-open', 'village_triangle.png'])

