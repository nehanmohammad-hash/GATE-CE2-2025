import numpy as np
import matplotlib.pyplot as plt

# --- Problem 65 Data ---
fb_ab = 60.0  # Fore bearing of line AB in degrees
fb_bc = 122.0 # Fore bearing of line BC in degrees

# Convert bearings to math angles (from +x axis, counter-clockwise)
theta_AB = np.deg2rad(90 - fb_ab)
theta_BC = np.deg2rad(90 - fb_bc)

# Length of the plotted rays
L = 5.0

# Point B (origin)
Bx, By = 0.0, 0.0

# Coordinates of points A and C along bearings from B
Ax = Bx + L * np.cos(theta_AB)
Ay = By + L * np.sin(theta_AB)

Cx = Bx + L * np.cos(theta_BC)
Cy = By + L * np.sin(theta_BC)

# Compute interior angle at B using vector dot product
BA = np.array([Ax - Bx, Ay - By])  # vector from B to A
BC = np.array([Cx - Bx, Cy - By])  # vector from B to C

cos_angle = np.dot(BA, BC) / (np.linalg.norm(BA) * np.linalg.norm(BC))
angle_rad = np.arccos(np.clip(cos_angle, -1.0, 1.0))
angle_deg = np.rad2deg(angle_rad)

print(f"Fore Bearing AB: {fb_ab}°")
print(f"Fore Bearing BC: {fb_bc}°")
print(f"Interior angle ABC: {int(round(angle_deg))} degrees (Exact: {angle_deg:.2f}°)")

# --- Plotting ---
fig, ax = plt.subplots(figsize=(6, 6))

# Plot lines BA and BC
ax.plot([Bx, Ax], [By, Ay], 'b-', label='Line AB')
ax.plot([Bx, Cx], [By, Cy], 'g-', label='Line BC')

# Mark points A, B, C
ax.scatter([Ax, Bx, Cx], [Ay, By, Cy], color='k')
ax.text(Ax, Ay, ' A', fontsize=12, va='bottom', ha='left')
ax.text(Bx, By, ' B', fontsize=12, va='top', ha='right')
ax.text(Cx, Cy, ' C', fontsize=12, va='bottom', ha='left')

# Small arc to show interior angle at B
arc_radius = 1.2
arc_t = np.linspace(theta_BC, theta_AB, 100)  # span between the two rays
arc_x = Bx + arc_radius * np.cos(arc_t)
arc_y = By + arc_radius * np.sin(arc_t)
ax.plot(arc_x, arc_y, 'r-')

# Angle text near the arc
mid_angle = (theta_AB + theta_BC) / 2
tx = Bx + (arc_radius + 0.3) * np.cos(mid_angle)
ty = By + (arc_radius + 0.3) * np.sin(mid_angle)
ax.text(tx, ty, rf'$ \angle ABC \approx {int(round(angle_deg))}^\circ $',
        color='r', fontsize=12, ha='center', va='center')

# Axes formatting
ax.set_aspect('equal', 'box')
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Problem 65: Interior Angle ∠ABC')
ax.legend(loc='upper right')

plt.savefig('/home/nehan-mohammad/GATE-CE2-2025/figs/interior_angle.png', dpi=300, bbox_inches='tight')
plt.close()
