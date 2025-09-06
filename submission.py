import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(7,7))
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor("#a8d08d")

def draw_ring(radius, count, colors):
    angles = np.linspace(0, 2*np.pi, count, endpoint=False)
    for i, theta in enumerate(angles):
        r = [radius, radius+25, radius, radius-25]
        a = [theta-0.15, theta, theta+0.15, theta]
        x = np.array(r) * np.cos(a)
        y = np.array(r) * np.sin(a)
        ax.fill(x, y, colors[i % len(colors)], edgecolor='black')

ax.add_patch(plt.Circle((0,0), 40, color="yellow", zorder=5))
ax.add_patch(plt.Circle((0,0), 25, color="green", zorder=6))
ax.add_patch(plt.Circle((0,0), 10, color="yellow", zorder=7))

draw_ring(70, 12, ["white","orange"])
draw_ring(120, 24, ["yellow","red"])
draw_ring(180, 36, ["#fffacd","orange","#ffd700"])
draw_ring(240, 48, ["red","yellow","orange","white"])

ax.text(0, -310, "🌸 Happy Onam 🌸", ha='center', va='center', fontsize=24, fontweight='bold', color="darkgreen")

plt.show()
