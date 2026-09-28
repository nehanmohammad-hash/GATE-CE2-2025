import matplotlib.pyplot as plt
import numpy as np

# Influence line ordinate for member G-I peak
peak_ordinate = 1.33
x = np.array([0, 6, 12, 36])
y = np.array([0, peak_ordinate, 0, 0])

plt.figure(figsize=(7, 3))
plt.plot(x, y, marker='o', color='red', linewidth=2)
plt.title('Influence Line Diagram for Member G-I')
plt.xlabel('Position of Unit Load (m)')
plt.ylabel('Ordinate')
plt.grid(True)
plt.savefig('/home/nehan-mohammad/GATE-CE2-2025/figs/influence_line_gi.png', bbox_inches='tight')
plt.close()

print("Influence line figure generated and saved successfully.")
