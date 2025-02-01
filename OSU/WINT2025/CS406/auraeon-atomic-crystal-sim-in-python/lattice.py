import numpy as np

### 2D Lattice Generation Functions ###
def generate_2d_simple_cubic(grid_size, a):
    """Generate a 2D Simple Cubic lattice structure."""
    x, y = np.meshgrid(np.arange(grid_size) * a, np.arange(grid_size) * a)
    return x, y

def generate_2d_triangular(grid_size, a):
    """Generate a 2D Triangular lattice structure."""
    x, y = np.meshgrid(np.arange(grid_size) * a, np.arange(grid_size) * a)
    x[1::2] += a / 2  # Offset every other row to form a triangular pattern
    return x, y

def generate_2d_hexagonal(grid_size, a):
    """Generate a 2D Hexagonal lattice structure."""
    x, y = generate_2d_triangular(grid_size, a)
    y *= np.sqrt(3) / 2  # Adjust spacing for hexagonal geometry
    return x, y

### 3D Lattice Generation Functions ###
def generate_3d_simple_cubic(grid_size, a):
    """Generate a 3D Simple Cubic lattice structure."""
    x, y, z = np.meshgrid(
        np.arange(grid_size) * a,
        np.arange(grid_size) * a,
        np.arange(grid_size) * a
    )
    return x, y, z

def generate_bcc(grid_size, a):
    """Generate a Body-Centered Cubic (BCC) lattice with multi-element support."""
    x, y, z = generate_3d_simple_cubic(grid_size, a)  # Corner atoms
    x_bcc = x + a / 2
    y_bcc = y + a / 2
    z_bcc = z + a / 2  # Center atoms
    return (x, y, z), (x_bcc, y_bcc, z_bcc)

def generate_fcc(grid_size, a):
    """Generate a Face-Centered Cubic (FCC) lattice with multi-element support."""
    x, y, z = generate_3d_simple_cubic(grid_size, a)  # Corner atoms

    # Face-centered atoms offset from the corners
    fcc_offsets = [
        (0, a/2, a/2), (a, a/2, a/2),
        (a/2, 0, a/2), (a/2, a, a/2),
        (a/2, a/2, 0), (a/2, a/2, a)
    ]
    
    fcc_atoms = []
    for (ox, oy, oz) in fcc_offsets:
        fcc_atoms.append((x + ox, y + oy, z + oz))

    return (x, y, z), fcc_atoms
