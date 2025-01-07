import numpy as np

# Phase 2
# 2D Simple Cubic Lattice
def generate_2d_simple_cubic(grid_size, a):
    """
    Generate a 2D simple cubic lattice.
    
    Parameters:
    - grid_size: Number of atoms along one axis.
    - a: Lattice constant (distance between atoms).
    
    Returns:
    - x, y: Meshgrid arrays representing lattice point coordinates.
    """
    x, y = np.meshgrid(np.arange(0, grid_size * a, a),
                       np.arange(0, grid_size * a, a))
    return x, y

import numpy as np

def generate_2d_simple_cubic(grid_size, a):
    """
    Generate a 2D simple cubic lattice.
    """
    x, y = np.meshgrid(np.arange(0, grid_size * a, a),
                       np.arange(0, grid_size * a, a))
    return x, y

def generate_2d_triangular(grid_size, a):
    """
    Generate a 2D triangular lattice.
    """
    x, y = np.meshgrid(np.arange(0, grid_size * a, a),
                       np.arange(0, grid_size * a * np.sqrt(3) / 2, a * np.sqrt(3) / 2))
    x[1::2,:] += a / 2  # Offset every other row by half the lattice constant
    return x, y

def generate_2d_hexagonal(grid_size, a):
    """
    Generate a 2D hexagonal lattice.
    """
    x, y = generate_2d_triangular(grid_size, a)
    y *= np.sqrt(3) / 2  # Scale y-spacing to match hexagonal geometry
    return x, y


# Phase 3
# 3D Simple Cubic Lattice
    """
def generate_3d_simple_cubic(grid_size, a):
    x, y, z = np.meshgrid(np.arange(0, grid_size * a, a),
                          np.arange(0, grid_size * a, a),
                          np.arange(0, grid_size * a, a))
    return x, y, z
    """

# Phase 4
# 2D Body-Centered Cubic Lattice
    """
def generate_bcc(grid_size, a):
    x, y, z = generate_3d_simple_cubic(grid_size, a)
    x_bcc = x + a / 2
    y_bcc = y + a / 2
    z_bcc = z + a / 2
    return x, y, z, x_bcc, y_bcc, z_bcc

    """
