import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Initialize figures and axes for 2D and 3D lattice plots
fig_2d, ax_2d = None, None
fig_3d, ax_3d = None, None

# 2D LATTICE VISUALIZATION FUNCTION
def plot_2d_lattice(x, y, title="2D Lattice", colors="blue", marker_size=50, elements="Unknown"):
    """Plots a 2D lattice with multi-element support and ensures the legend is placed outside the plot without skewing."""
    global fig_2d, ax_2d

    # Close 3D figure if it exists
    if plt.fignum_exists(fig_3d) and fig_3d is not None:
        plt.close(fig_3d)

    # Create new figure with extra width for the legend
    fig_2d, ax_2d = plt.subplots(figsize=(8, 6))  # Increase figure width
    fig_2d.subplots_adjust(right=0.75)  # Shift the plot left to make space for legend
    ax_2d.clear() # Clear the plot

    # Plot the lattice with multi-element support
    if isinstance(colors, list) and isinstance(elements, list) and isinstance(x, list):
        for i in range(len(colors)):
            ax_2d.scatter(x[i], y[i], c=colors[i], s=marker_size[i], label=f"{elements[i]} ({colors[i]})")
    else:
        ax_2d.scatter(x, y, c=colors, s=marker_size, label=f"{elements} ({colors})")

    # Set plot title and axis labels
    ax_2d.set_title(title)
    ax_2d.set_xlabel("X (Å)")
    ax_2d.set_ylabel("Y (Å)")

    # Move legend outside of the plot but keep proper scaling
    ax_2d.legend(loc="center left", bbox_to_anchor=(1, 0.5))

    # Draw the plot and show it
    fig_2d.canvas.draw_idle()
    plt.show(block=False)  # Keep the window interactive

# 3D LATTICE VISUALIZATION FUNCTION
def plot_3d_lattice(x, y, z, title="3D Lattice", colors="blue", marker_sizes=50, elements="Unknown"):
    """Plots a 3D lattice """
    global fig_3d, ax_3d

    # Close 2D figure if it exists
    if plt.fignum_exists(fig_2d) and fig_2d is not None:
        plt.close(fig_2d)

    # Create a new figure with additional width for the legend
    fig_3d = plt.figure(figsize=(9, 6))  # Increase figure width
    ax_3d = fig_3d.add_subplot(111, projection='3d')
    fig_3d.subplots_adjust(right=0.75)  # Shift the plot left

    # Clear the plot
    ax_3d.clear()

    # Plot the lattice with multi-element support
    if isinstance(colors, list) and isinstance(marker_sizes, list) and isinstance(elements, list):
        if isinstance(x[0], np.ndarray):
            for i in range(len(colors)):
                ax_3d.scatter(x[i], y[i], z[i], c=colors[i], s=marker_sizes[i], label=f"{elements[i]} ({colors[i]})")
    else:
        ax_3d.scatter(x, y, z, c=colors, s=marker_sizes, label=f"{elements} ({colors})")

    # Set plot title and axis labels
    ax_3d.set_title(title)
    ax_3d.set_xlabel("X (Å)")
    ax_3d.set_ylabel("Y (Å)")
    ax_3d.set_zlabel("Z (Å)")

    # Move legend outside of the plot while keeping proper scaling
    ax_3d.legend(loc="center left", bbox_to_anchor=(1, 0.5))

    # Draw the plot and show it
    fig_3d.canvas.draw_idle()
    plt.show(block=False)  # Keep the window interactive
