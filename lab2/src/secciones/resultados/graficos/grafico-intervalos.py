import matplotlib.pyplot as plt

data = [
    {"nombre": "Bronce (Cu, Sn)", "min": 8.7, "max": 8.9},
    {"nombre": "Pesas de latón", "min": 8.4, "max": 8.4},
    {"nombre": "Latón ordinario", "min": 8.4, "max": 8.7},
    {"nombre": "Probeta graduada", "min": 7.4, "max": 9.22},
    {"nombre": "Regla milimetrada", "min": 7.61, "max": 9.11},
    {"nombre": "Calibre", "min": 8.275, "max": 8.40},
]

spacing = 1
y_pos = [i * spacing for i in range(len(data))]

labels = [d["nombre"] for d in data]
centers = [(d["min"] + d["max"]) / 2 for d in data]
errors = [(d["max"] - d["min"]) / 2 for d in data]

fig, ax = plt.subplots()

ax.errorbar(
    centers,
    y_pos,
    xerr=errors,
    fmt='none',
    ecolor='black',
    capsize=3
)

half_height = spacing * 0.07
for y, c in zip(y_pos, centers):
    ax.vlines(c, y - half_height, y + half_height, color='black', linewidth=1.3)

label_offset = spacing * 0.12
for y, d in zip(y_pos, data):
    ax.text(d["min"], y - label_offset, f'{d["min"]:.2f}',
            ha='center', va='top', fontsize=8)
    ax.text(d["max"], y - label_offset, f'{d["max"]:.2f}',
            ha='center', va='top', fontsize=8)

ax.axvline(8.40, color='red', linestyle='dotted', linewidth=1, zorder=0)

ax.set_yticks(y_pos)
ax.set_yticklabels(labels)
ax.set_xlabel("ρ (g/cm³)")

for spine in ax.spines.values():
    spine.set_visible(False)

ax.grid(True)

plt.tight_layout()
plt.savefig("grafico-intervalos.pdf", dpi=150)
plt.show()

# env/bin/python grafico-intervalos.py