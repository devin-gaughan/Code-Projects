import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def plot_2d_lattice(ax, x, y, a, b, title="2D Lattice", colors=None, marker_sizes=50, elements="Unknown", bond_threshold=2.0):
    """Plots a 2D lattice on the given Matplotlib axes."""
    ax.clear()  # Clear the axes before plotting

    if colors is None:
        colors = ['blue'] * len(x) if isinstance(x, list) else 'blue'

    if isinstance(x, list) and isinstance(y, list):
        for i, (x_i, y_i) in enumerate(zip(x, y)):
            ax.scatter(x_i, y_i, c=colors[i], s=marker_sizes[i], label=f"{elements[i]} ({colors[i]})")
            draw_2d_bonds(ax, x_i, y_i, bond_threshold)
    else:
        ax.scatter(x, y, c=colors, s=marker_sizes, label=f"{elements} ({colors})")
        draw_2d_bonds(ax, x, y, bond_threshold)

    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()
    plt.tight_layout()

def draw_2d_bonds(ax, x, y, bond_threshold):
    """Draws bonds between atoms in a 2D lattice that are within the bond_threshold distance."""
    if len(x) == 0 or len(y) == 0:
        return  # No atoms to bond

    coords = np.column_stack((x.ravel(), y.ravel()))
    dist_mat = np.linalg.norm(coords[:, None] - coords, axis=-1)

    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            distance = dist_mat[i, j]
            if distance <= bond_threshold:
                ax.plot([coords[i, 0], coords[j, 0]], [coords[i, 1], coords[j, 1]], 'k-', lw=1)

def plot_3d_lattice(ax, x, y, z, a, b, c, title="3D Lattice", colors=None, marker_sizes=50, elements="Unknown", bond_threshold=2.0):
    """Plots a 3D lattice on the given Matplotlib 3D axes."""
    ax.clear()  # Clear the axes before plotting

    if colors is None:
        colors = ['blue'] * len(x) if isinstance(x, list) else 'blue'

    if isinstance(x, list) and isinstance(y, list) and isinstance(z, list):
        for i, (x_i, y_i, z_i) in enumerate(zip(x, y, z)):
            ax.scatter(x_i, y_i, z_i, c=colors[i], s=marker_sizes[i], label=f"{elements[i]} ({colors[i]})")
            draw_3d_bonds(ax, x_i, y_i, z_i, bond_threshold)
    else:
        ax.scatter(x, y, z, c=colors, s=marker_sizes, label=f"{elements} ({colors})")
        draw_3d_bonds(ax, x, y, z, bond_threshold)

    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend()
    plt.tight_layout()

def draw_3d_bonds(ax, x, y, z, bond_threshold):
    """Draws bonds between atoms in a 3D lattice that are within the bond_threshold distance."""
    if len(x) == 0 or len(y) == 0 or len(z) == 0:
        return  # No atoms to bond

    coords = np.column_stack((x.ravel(), y.ravel(), z.ravel()))
    dist_mat = np.linalg.norm(coords[:, None] - coords, axis=-1)

    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            distance = dist_mat[i, j]
            if distance <= bond_threshold:
                ax.plot([coords[i, 0], coords[j, 0]], [coords[i, 1], coords[j, 1]], [coords[i, 2], coords[j, 2]], 'k-', lw=1)
