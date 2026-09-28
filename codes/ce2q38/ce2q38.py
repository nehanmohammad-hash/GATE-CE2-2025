import matplotlib.pyplot as plt
import numpy as np

L = 10.0
M = 50.0
Delta = 0.01
EI = 10000.0

# Upward reaction at propped support B
R_b = (3 * M / (2 * L)) - (3 * EI * Delta / (L**3))
print(f"Upward Reaction at B = {R_b:.2f} N")

x = np.linspace(0, L, 100)
deflection = -(M * x**2) / (2 * EI) + (R_b * x**3) / (6 * EI)

plt.figure(figsize=(6, 3))
plt.plot(x, deflection, color='purple', label='Deflection Curve')
plt.title('Propped Cantilever Deflection Curve')
plt.xlabel('Length (m)')
plt.ylabel('Deflection (m)')
plt.savefig('/home/nehan-mohammad/GATE-CE2-2025/figs/cantilever_deflection.png', bbox_inches='tight')
plt.close()
