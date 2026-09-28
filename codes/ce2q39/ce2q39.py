import matplotlib.pyplot as plt
import numpy as np

sigma_0 = 1.0
sigma_1 = 3 * sigma_0
sigma_2 = -3 * sigma_0
max_compressive = abs(sigma_2)
k = max_compressive / sigma_0
print(f"k = {k:.1f} (Option A: 3.0)")

plt.figure(figsize=(5, 5))
angles = np.linspace(0, 2 * np.pi, 100)
plt.plot(sigma_1 * np.cos(angles), sigma_2 * np.sin(angles), label='Mohr Circle')
plt.title('Principal Stress State Analysis')
plt.savefig('/home/nehan-mohammad/GATE-CE2-2025/figs/stress_state_mohr.png', bbox_inches='tight')
plt.close()
