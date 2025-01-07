import matplotlib.pyplot as plt

# Phase 2
# 2D Simple Cubic Lattice
def plot_2d_lattice(x, y):
    """
    Plot a 2D simple cubic lattice.
    
    Parameters:
    - x, y: Lattice point coordinates (meshgrid).
    """
    plt.figure(figsize=(6, 6))
    plt.scatter(x, y, c='blue', s=100)
    plt.title('2D Simple Cubic Lattice')
    plt.grid(True)
    plt.show()

def plot_2d_lattice(x, y, lattice_type="Simple Cubic"):
    """
    Plot a 2D lattice with a specified type.
    """
    plt.figure(figsize=(6, 6))
    plt.scatter(x, y, c='blue', s=100)  # Blue points for atoms
    plt.title(f'2D {lattice_type} Lattice')
    plt.grid(True)
    plt.xlabel('X-axis (Å)')
    plt.ylabel('Y-axis (Å)')
    plt.show()


# Phase 3
# 3D Simple Cubic Lattice
"""
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_lattice(x, y, z):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c='red', s=50)
    ax.set_title('3D Simple Cubic Lattice')
    plt.show()

"""

# Phase 4
# 2D Body-Centered Cubic Lattice
"""
def plot_bcc_lattice(x, y, z, x_bcc, y_bcc, z_bcc):
    plot_3d_lattice(x, y, z)
    plt.scatter(x_bcc, y_bcc, z_bcc, c='blue', s=50)
    plt.show()

"""

# Phase 5
# 3D Simple Cubic Lattice (pyVista)
"""
import pyvista as pv

def plot_3d_interactive(x, y, z):
    points = np.column_stack([x.ravel(), y.ravel(), z.ravel()])
    cloud = pv.PolyData(points)
    plotter = pv.Plotter()
    plotter.add_mesh(cloud, render_points_as_spheres=True, point_size=10)
    plotter.show()

"""