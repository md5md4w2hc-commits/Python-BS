import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- 1. Simulation Configuration ---
POINTS_PER_FRAME = 25   # Increase to 50 or 100 for faster convergence
TOTAL_FRAMES = 200      # Total animation frames (25 * 200 = 5,000 darts)

# --- 2. Set Up the Dual-Panel Figure ---
plt.style.use('dark_background')
fig, (ax_board, ax_curve) = plt.subplots(1, 2, figsize=(12, 5.5))
fig.canvas.manager.set_window_title("IITM BS Foundation - Live Monte Carlo Simulation")

# Left Panel: Dartboard (Unit Circle inside a 2x2 Square)
ax_board.set_xlim(-1.05, 1.05)
ax_board.set_ylim(-1.05, 1.05)
ax_board.set_aspect('equal')
ax_board.set_title("Random Darts on Unit Circle", fontsize=12, pad=10)

# Draw the reference circle boundary (x^2 + y^2 = 1)
theta = np.linspace(0, 2 * np.pi, 300)
ax_board.plot(np.cos(theta), np.sin(theta), color='white', lw=1.5, ls='--')
scatter = ax_board.scatter([], [], s=8, alpha=0.75)

# Right Panel: Live Convergence Curve
ax_curve.set_xlim(0, POINTS_PER_FRAME * TOTAL_FRAMES)
ax_curve.set_ylim(2.7, 3.6)
ax_curve.set_title("Live Convergence to π", fontsize=12, pad=10)
ax_curve.set_xlabel("Total Darts Thrown (N)")
ax_curve.set_ylabel("Estimated Value of π")
ax_curve.axhline(np.pi, color='#facc15', lw=1.5, ls='--', label=f"True π ({np.pi:.5f})")
conv_line, = ax_curve.plot([], [], color='#38bdf8', lw=2, label="Monte Carlo Estimate")
ax_curve.legend(loc="upper right")
ax_curve.grid(alpha=0.2)

# Readout text box for live metrics
stats_text = ax_curve.text(
    0.04, 0.18, "", transform=ax_curve.transAxes, fontsize=10,
    family="monospace", bbox=dict(boxstyle="round,pad=0.5", facecolor="#1e293b", edgecolor="#475569")
)

# --- 3. State Storage ---
all_x, all_y, all_colors = [], [], []
sample_counts, pi_estimates = [], []
inside_count = 0

# --- 4. Frame-by-Frame Update Function ---
def update(frame):
    global inside_count

    # Generate a new batch of random (x, y) coordinates in [-1, 1]
    x_new = np.random.uniform(-1, 1, POINTS_PER_FRAME)
    y_new = np.random.uniform(-1, 1, POINTS_PER_FRAME)

    # Check circle equation: x^2 + y^2 <= 1
    inside_mask = (x_new**2 + y_new**2) <= 1.0
    inside_count += np.sum(inside_mask)

    # Store coordinates and colors (#10b981 = emerald hit, #f43f5e = coral miss)
    all_x.extend(x_new)
    all_y.extend(y_new)
    all_colors.extend(np.where(inside_mask, '#10b981', '#f43f5e'))

    # Compute current Pi estimate: 4 * (inside / total)
    total_n = len(all_x)
    current_pi = 4.0 * inside_count / total_n
    error = abs(current_pi - np.pi)

    sample_counts.append(total_n)
    pi_estimates.append(current_pi)

    # Update Left Panel (Scatter Plot)
    scatter.set_offsets(np.column_stack([all_x, all_y]))
    scatter.set_color(all_colors)

    # Update Right Panel (Convergence Line & Metrics)
    conv_line.set_data(sample_counts, pi_estimates)
    stats_text.set_text(
        f"Darts (N) : {total_n:>5}\n"
        f"Inside    : {inside_count:>5}\n"
        f"Est. π    : {current_pi:.5f}\n"
        f"Abs Error : {error:.5f}"
    )

    return scatter, conv_line, stats_text

# --- 5. Launch Animation (interval=30ms -> ~33 FPS) ---
ani = FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=30, blit=False, repeat=False)

plt.tight_layout()
plt.show()
