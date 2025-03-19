import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6,6))
ax.set_xticks(range(10))
ax.set_yticks(range(10))
ax.grid(True, which="both", linestyle='-', linewidth=1)

# Number each cell
for i in range(9):
    for j in range(9):
        num = i * 9 + j  # Calculate number from 0 to 80
        ax.text(j + 0.5, 8 - i + 0.5, str(num), va='center', ha='center', fontsize=12)

ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xlim(0, 9)
ax.set_ylim(0, 9)
ax.set_frame_on(False)

plt.show()
