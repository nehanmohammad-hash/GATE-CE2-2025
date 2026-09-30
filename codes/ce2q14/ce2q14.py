import matplotlib.pyplot as plt
import numpy as np

# Bottom chord joint positions (assuming equal panel spacing, e.g., 6 meters per panel for 6 panels total = 36m span)
# Joints: A(0), D(6), G(12), I(18), L(24), O(30), P(36)
x = np.array([0, 6, 12, 18, 24, 30, 36])

# Corresponding influence line ordinates for member G-I calculated using the section cutting method
# Peak is at G (1.33), with linear variation to zero at supports A and P
y = np.array([0, 0.33, 1.33, 1.00, 0.67, 0.33, 0])

# Enlarge figure width so point P is clearly positioned at the end of the x-axis
plt.figure(figsize=(10, 4))
plt.plot(x, y, marker='o', color='red', linewidth=2, markersize=6)

# Annotate each joint point
joints = ['A', 'D', 'G', 'I', 'L', 'O', 'P']
for xi, yi, joint in zip(x, y, joints):
    plt.text(xi, yi + 0.08, f'{joint}\n({yi:.2f})' if yi > 0 else f'{joint}\n(0)', 
             ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.title('Influence Line Diagram for Member G-I', fontsize=12, fontweight='bold')
plt.xlabel('Position of Unit Load Along Bottom Chord (m)', fontsize=10)
plt.ylabel('Influence Ordinate (Force)', fontsize=10)
plt.xticks(x, [f'{j}\n({pos}m)' for j, pos in zip(joints, x)])
plt.ylim(-0.1, 1.6)
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(0, color='black', linewidth=1)

plt.savefig('/home/nehan-mohammad/GATE-CE2-2025/figs/influence_line_gi.png', bbox_inches='tight')
plt.close()

print("Generated and saved successfully.")
