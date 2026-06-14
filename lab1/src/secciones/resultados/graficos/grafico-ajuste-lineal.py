import matplotlib.pyplot as plt
import numpy as np

data = [
    {"x": 0.517, "y": 2.0620, "dx": 0.045,  "dy": -0.04, "rel_error": 0.0158},
    {"x": 0.730, "y": 2.9036, "dx": 0.015, "dy": -0.13, "rel_error": 0.0131},
    {"x": 0.820, "y": 3.3690, "dx": 0.04, "dy": -0.1, "rel_error": 0.0121},
    {"x": 1.000, "y": 4.0884, "dx": -0.045,  "dy": 0.0, "rel_error": 0.0108},
]

L = np.array([d["x"] for d in data])
T2 = np.array([d["y"] for d in data])
relative_errors = np.array([d["rel_error"] for d in data])
yerr = T2 * relative_errors

fig, ax = plt.subplots()

ax.errorbar(L, T2, yerr=yerr, fmt='none', ecolor='black', elinewidth=1, capsize=3, zorder=5)
ax.scatter(L, T2, color='black', s=10, zorder=10)

for d in data:
    ax.text(
        d["x"] + d["dx"],
        d["y"] + d["dy"],
        f'({d["x"]:.3f}, {d["y"]:.3f})',
        fontsize=7,
        ha='center'
    )

ax.set_xlim(min(L) - 0.05, max(L) + 0.05)

x_line = np.array(ax.get_xlim())
y_line = 4.23 * x_line - 0.135
ax.plot(x_line, y_line, linewidth=1, zorder=0, linestyle='dotted', color='red')

ax.text(0.505, 2.65, r"$a(x) = 4.23 \cdot x − 0.135$", fontsize=9, color='red')
# 0.63, 2.4

ax.set_xlabel("L (m)")
ax.set_ylabel("T² (s²)")
for spine in ax.spines.values():
    spine.set_visible(False)
ax.grid(True)

plt.tight_layout()
plt.savefig("grafico-ajuste-lineal.pdf", dpi=150)
plt.show()

# env/bin/python grafico-ajuste-lineal.py