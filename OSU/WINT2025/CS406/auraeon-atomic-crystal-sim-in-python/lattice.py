import numpy as np

### 2D Lattice Generation Functions ###
def generate_2d_simple_cubic(grid_size, a, b):
    """Generate a 2D Simple Cubic lattice structure."""
    x, y = np.meshgrid(
        np.linspace(0, (grid_size - 1) * a, grid_size),
        np.linspace(0, (grid_size - 1) * b, grid_size))
    return x, y

def generate_2d_triangular(grid_size, a, b):
    """Generate a 2D Triangular lattice structure."""
    x, y = generate_2d_simple_cubic(grid_size, a, b) # Starts with a basic grid
    x[1::2] += a / 2  # Offset every other row to form a triangular pattern
    return x, y

def generate_2d_hexagonal(grid_size, a, b):
    """Generate a 2D Hexagonal lattice structure."""
    x, y = generate_2d_triangular(grid_size, a, b)
    y *= np.sqrt(3) / 2  # Adjust spacing for hexagonal geometry
    return x, y

### 3D Lattice Generation Functions ###
def generate_3d_simple_cubic(grid_size, a, b, c):
    """Generate a 3D Simple Cubic lattice structure."""
    x, y, z = np.meshgrid(
        np.linspace(0, (grid_size - 1) * a, grid_size),
        np.linspace(0, (grid_size - 1) * b, grid_size),
        np.linspace(0, (grid_size - 1) * c, grid_size)
    )
    return x, y, z

def generate_bcc(grid_size, a, b, c):
    """Generate a Body-Centered Cubic (BCC) lattice with multi-element support."""
    x, y, z = generate_3d_simple_cubic(grid_size, a, b, c)  # Corner atoms
    x_bcc = x + a / 2
    y_bcc = y + b / 2
    z_bcc = z + c / 2  # Center atoms
    return (x, y, z), (x_bcc, y_bcc, z_bcc)

def generate_fcc(grid_size, a, b, c):
    """Generate a Face-Centered Cubic (FCC) lattice with multi-element support."""
    x, y, z = generate_3d_simple_cubic(grid_size, a, b, c)  # Corner atoms

    # Face-centered atoms offset from the corners
    fcc_offsets = [
        (0, b/2, c/2), (a, b/2, c/2),
        (a/2, 0, c/2), (a/2, b, c/2),
        (a/2, b/2, 0), (a/2, b/2, c)
    ]
    fcc_atoms = [(x + ox, y + oy, z + oz) for (ox, oy, oz) in fcc_offsets]
    return (x, y, z), fcc_atoms