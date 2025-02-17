import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig_2d, ax_2d = None, None
fig_3d, ax_3d = None, None

def plot_2d_lattice(x, y, a, b, title="2D Lattice", colors="blue", marker_sizes=50, elements="Unknown"):
    """Plots a 2D lattice with multi-element support, ensuring the correct match of arrays."""
    global fig_2d, ax_2d
    
    if fig_2d is None or not plt.fignum_exists(fig_2d.number):
        fig_2d, ax_2d = plt.subplots(figsize=(10, 8))

    ax_2d.clear()

    # If x, y are lists => multi-element. Each list item is one element's coordinates
    if isinstance(x, list) and isinstance(y, list):
        for i in range(len(x)):
            # s_val must be a scalar OR match x[i].size
            if isinstance(marker_sizes, list):
                s_val = marker_sizes[i]
            else:
                s_val = marker_sizes
            ax_2d.scatter(
                np.ravel(x[i]),
                np.ravel(y[i]),
                c=colors[i],
                s=s_val,
                label=f"{elements[i]} ({colors[i]})"
            )
    else:
        # Single array for single-element
        ax_2d.scatter(np.ravel(x), np.ravel(y), c=colors, s=marker_sizes, label=f"{elements} ({colors})")

    ax_2d.set_xlim([np.min(x) - a, np.max(x) + a])
    ax_2d.set_ylim([np.min(y) - b, np.max(y) + b])
    ax_2d.set_title(title)
    ax_2d.set_xlabel(f"X (Å), a={a:.2f}")
    ax_2d.set_ylabel(f"Y (Å), b={b:.2f}")
    ax_2d.legend(loc="upper right")
    fig_2d.canvas.draw_idle()
    plt.show(block=False)

def plot_3d_lattice(x, y, z, a, b, c, title="3D Lattice", colors="blue", marker_sizes=50, elements="Unknown"):
    """Plots a 3D lattice with correct multi-element formatting."""
    global fig_3d, ax_3d

    if fig_3d is None or not plt.fignum_exists(fig_3d.number):
        fig_3d = plt.figure(figsize=(10, 8))
        ax_3d = fig_3d.add_subplot(111, projection='3d')

    ax_3d.clear()

    # If x, y, z are lists => multi-element
    if isinstance(x, list) and isinstance(y, list) and isinstance(z, list):
        for i in range(len(x)):
            s_val = marker_sizes[i] if isinstance(marker_sizes, list) else marker_sizes
            ax_3d.scatter(
                np.ravel(x[i]),
                np.ravel(y[i]),
                np.ravel(z[i]),
                c=colors[i],
                s=s_val,
                label=f"{elements[i]} ({colors[i]})"
            )

        # Consolidate all for auto-scale
        x_all = np.concatenate([np.ravel(arr) for arr in x])
        y_all = np.concatenate([np.ravel(arr) for arr in y])
        z_all = np.concatenate([np.ravel(arr) for arr in z])
    else:
        ax_3d.scatter(
            np.ravel(x), np.ravel(y), np.ravel(z),
            c=colors, s=marker_sizes,
            label=f"{elements} ({colors})"
        )
        x_all = np.ravel(x)
        y_all = np.ravel(y)
        z_all = np.ravel(z)

    ax_3d.set_xlim([np.min(x_all) - a, np.max(x_all) + a])
    ax_3d.set_ylim([np.min(y_all) - b, np.max(y_all) + b])
    ax_3d.set_zlim([np.min(z_all) - c, np.max(z_all) + c])

    ax_3d.view_init(elev=25, azim=40)
    ax_3d.set_title(title)
    ax_3d.set_xlabel(f"X (Å), a={a:.2f}")
    ax_3d.set_ylabel(f"Y (Å), b={b:.2f}")
    ax_3d.set_zlabel(f"Z (Å), c={c:.2f}")
    ax_3d.legend(loc="upper right")
    fig_3d.canvas.draw_idle()
    plt.show(block=False)
