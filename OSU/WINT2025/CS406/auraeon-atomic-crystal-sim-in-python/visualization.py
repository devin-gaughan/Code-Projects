import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Global references for figures and axes
fig_2d, ax_2d = None, None
fig_3d, ax_3d = None, None

# Store user camera angles globally
camera_elev, camera_azim = 25, 40

def on_mouse_release(event):
    """Capture 3D camera angles when the user releases the mouse."""
    global camera_elev, camera_azim
    if ax_3d is not None and event.inaxes == ax_3d:
        camera_elev = ax_3d.elev
        camera_azim = ax_3d.azim

def plot_2d_lattice(x, y, a, b, title="2D Lattice", colors="blue", marker_sizes=50, elements="Unknown"):
    """Plots a 2D lattice with fixed legend positioning."""
    global fig_2d, ax_2d
    
    if fig_2d is None or not plt.fignum_exists(fig_2d.number):
        fig_2d, ax_2d = plt.subplots(figsize=(10, 6))  # Increased width

    ax_2d.clear()

    # Multi-element scatter
    if isinstance(x, list) and isinstance(y, list):
        for i in range(len(x)):
            s_val = marker_sizes[i] if isinstance(marker_sizes, list) else marker_sizes
            ax_2d.scatter(np.ravel(x[i]), np.ravel(y[i]), c=colors[i], s=s_val,
                          label=f"{elements[i]} ({colors[i]})")
    else:
        ax_2d.scatter(np.ravel(x), np.ravel(y), c=colors, s=marker_sizes,
                      label=f"{elements} ({colors})")

    # Adjust plot limits
    ax_2d.set_xlim([np.min(x) - a, np.max(x) + a])
    ax_2d.set_ylim([np.min(y) - b, np.max(y) + b])

    # Shift the plot to the left to make space for the legend
    fig_2d.subplots_adjust(right=0.75)  # Reserve space for legend
    ax_2d.legend(loc="center left", bbox_to_anchor=(1, 0.5))  # Move outside

    ax_2d.set_title(title)
    ax_2d.set_xlabel(f"X (Å), a={a:.2f}")
    ax_2d.set_ylabel(f"Y (Å), b={b:.2f}")

    fig_2d.canvas.draw_idle()
    plt.show(block=False)

def plot_3d_lattice(x, y, z, a, b, c, title="3D Lattice", colors="blue", marker_sizes=50, elements="Unknown"):
    """Plots a 3D lattice while preserving the user's camera angles."""
    global fig_3d, ax_3d, camera_elev, camera_azim

    if fig_3d is None or not plt.fignum_exists(fig_3d.number):
        fig_3d = plt.figure(figsize=(10, 6))
        ax_3d = fig_3d.add_subplot(111, projection='3d')

        # Capture mouse release event to update camera angles
        fig_3d.canvas.mpl_connect("button_release_event", on_mouse_release)

    ax_3d.clear()

    # Restore the previously stored camera angles
    ax_3d.view_init(elev=camera_elev, azim=camera_azim)

    # Multi-element scatter
    if isinstance(x, list) and isinstance(y, list) and isinstance(z, list):
        for i in range(len(x)):
            s_val = marker_sizes[i] if isinstance(marker_sizes, list) else marker_sizes
            ax_3d.scatter(np.ravel(x[i]), np.ravel(y[i]), np.ravel(z[i]),
                          c=colors[i], s=s_val, label=f"{elements[i]} ({colors[i]})")

        x_all = np.concatenate([np.ravel(arr) for arr in x])
        y_all = np.concatenate([np.ravel(arr) for arr in y])
        z_all = np.concatenate([np.ravel(arr) for arr in z])
    else:
        ax_3d.scatter(np.ravel(x), np.ravel(y), np.ravel(z),
                      c=colors, s=marker_sizes, label=f"{elements} ({colors})")

        x_all, y_all, z_all = np.ravel(x), np.ravel(y), np.ravel(z)

    # Adjust plot limits
    ax_3d.set_xlim([np.min(x_all) - a, np.max(x_all) + a])
    ax_3d.set_ylim([np.min(y_all) - b, np.max(y_all) + b])
    ax_3d.set_zlim([np.min(z_all) - c, np.max(z_all) + c])

    # Adjust layout to fit legend
    fig_3d.subplots_adjust(right=0.75)
    ax_3d.legend(loc="center left", bbox_to_anchor=(1, 0.5))  # Move legend outside

    ax_3d.set_title(title)
    ax_3d.set_xlabel(f"X (Å), a={a:.2f}")
    ax_3d.set_ylabel(f"Y (Å), b={b:.2f}")
    ax_3d.set_zlabel(f"Z (Å), c={c:.2f}")

    fig_3d.canvas.draw_idle()
    plt.show(block=False)
