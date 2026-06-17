import numpy as np
import scipy as sp
from matplotlib import pyplot as plt

data_1 = [
    {"A": 0.00, "V": 0.0},
    {"A": 0.00, "V": 1.0},
    {"A": 0.01, "V": 2.0},
    {"A": 0.01, "V": 3.0},
    {"A": 0.02, "V": 4.0},
    {"A": 0.03, "V": 5.0},
    {"A": 0.03, "V": 6.0},
    {"A": 0.04, "V": 7.0},
    {"A": 0.04, "V": 8.0},
    {"A": 0.05, "V": 9.0},
    {"A": 0.05, "V": 10.0},
    {"A": 0.06, "V": 11.0},
    {"A": 0.07, "V": 12.0},
    {"A": 0.07, "V": 13.0},
    {"A": 0.08, "V": 14.0},
    {"A": 0.08, "V": 15.0},
    {"A": 0.08, "V": 16.0},
]

data_2 = [
    {"A": 0.00, "V": 0.0},
    {"A": 0.01, "V": 1.0},
    {"A": 0.02, "V": 2.0},
    {"A": 0.03, "V": 3.0},
    {"A": 0.04, "V": 4.0},
    {"A": 0.05, "V": 5.0},
    {"A": 0.06, "V": 6.0},
    {"A": 0.07, "V": 7.0},
    {"A": 0.08, "V": 8.0},
    {"A": 0.10, "V": 9.0},
    {"A": 0.11, "V": 10.0},
    {"A": 0.12, "V": 11.0},
    {"A": 0.13, "V": 12.0},
    {"A": 0.14, "V": 13.0},
    {"A": 0.15, "V": 14.0},
    {"A": 0.16, "V": 15.0},
    {"A": 0.17, "V": 16.0},
]

def ajuste_lineal(x, m, b):
    return m * x + b

x = np.array([d["A"] for d in data_1])
medicion = np.array([d["V"] for d in data_1])

c, _ = sp.optimize.curve_fit(ajuste_lineal, x, medicion)

ajuste_eval = ajuste_lineal(x, *c)
error = np.abs(ajuste_eval - medicion)
r = np.sum((ajuste_eval - medicion) ** 2)

m_opt, b_opt = c

fig, ax = plt.subplots()

ax.errorbar(x, medicion, yerr=error, fmt='none', ecolor='black', elinewidth=1, capsize=3, zorder=5)
ax.scatter(x, medicion, color='black', s=10, zorder=10)

ax.set_xlim(min(x) - 0.01, max(x) + 0.01)

x_line = np.array(ax.get_xlim())
y_line = ajuste_lineal(x_line, *c)
ax.plot(x_line, y_line, linewidth=1, zorder=0, linestyle='dotted', color='red')

ax.text(0.005, 13.0, fr"$V(I) = {m_opt:.2f} \cdot I - {abs(b_opt):.2f}$", fontsize=9, color='red')

ax.set_xlabel("Corriente I (A)")
ax.set_ylabel("Voltaje V (V)")
for spine in ax.spines.values():
    spine.set_visible(False)
ax.grid(True)

plt.tight_layout()
plt.savefig("grafico-ajuste-lineal.pdf", dpi=150)
plt.show()