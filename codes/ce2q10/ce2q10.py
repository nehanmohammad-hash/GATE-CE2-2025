import matplotlib.pyplot as plt
import numpy as np

# Triangle PQR with sides a=14 (QR), b=15 (RP), c=13 (PQ)
a, b, c = 14, 15, 13
s = (a + b + c) / 2
area = np.sqrt(s * (s - a) * (s - b) * (s - c))
h_a = (2 * area) / a

print(f"Area of Triangle: {area} sq km")
print(f"Minimum connecting road length (Altitude): {h_a} km")

# Generate and save triangle geometry figure
plt.figure(figsize=(6, 5))
plt.plot([0, 14, 5, 0], [0, 0, 12, 0], 'bo-', linewidth=2)
plt.plot([5, 5], [0, 12], 'r--', label=f'Altitude = {h_a} km')
plt.text(-0.8, -0.5, 'Q (0,0)', fontsize=10)
plt.text(14.2, -0.5, 'R (14,0)', fontsize=10)
plt.text(4.7, 12.5, 'P (5,12)', fontsize=10)
plt.legend()
plt.title('Village Triangle PQR and Connecting Road')
plt.savefig('/home/nehan-mohammad/GATE-CE2-2025/figs/village_triangle.png', bbox_inches='tight')
plt.close()