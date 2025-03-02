import numpy as np

def generate_2d_simple_cubic(nx, ny, a, b):
    """Generates coordinates for a 2D simple cubic lattice."""
    x = np.arange(nx) * a
    y = np.arange(ny) * b
    x_coords, y_coords = np.meshgrid(x, y)
    return x_coords, y_coords

def generate_2d_triangular(nx, ny, a, b):
    """Generates coordinates for a 2D triangular lattice."""
    x = np.arange(nx) * a
    y = np.arange(ny) * b
    x_coords, y_coords = np.meshgrid(x, y)
    # Offset every other row for triangular lattice
    x_coords[::2, :] += a / 2.0
    return x_coords, y_coords

def generate_2d_hexagonal(nx, ny, a, b):
    """Generates coordinates for a 2D hexagonal lattice."""
    x = np.arange(nx) * a
    y = np.arange(ny) * b * np.sqrt(3) / 2
    x_coords, y_coords = np.meshgrid(x, y)
    # Offset every other row for hexagonal lattice
    x_coords[::2, :] += a / 2.0
    return x_coords, y_coords

def generate_3d_simple_cubic(nx, ny, nz, a, b, c):
    """Generates coordinates for a 3D simple cubic lattice."""
    x = np.arange(nx) * a
    y = np.arange(ny) * b
    z = np.arange(nz) * c
    x_coords, y_coords, z_coords = np.meshgrid(x, y, z)
    return x_coords, y_coords, z_coords

def generate_bcc(nx, ny, nz, a, b, c):
    """Generates coordinates for a 3D body-centered cubic lattice."""
    x = np.arange(nx) * a
    y = np.arange(ny) * b
    z = np.arange(nz) * c
    x_coords, y_coords, z_coords = np.meshgrid(x, y, z)

    # Add atom in the center of each cell
    x_center = x_coords + a / 2
    y_center = y_coords + b / 2
    z_center = z_coords + c / 2

    return (x_coords, y_coords, z_coords), (x_center, y_center, z_center)

def generate_fcc(nx, ny, nz, a, b, c):
    """Generates coordinates for a 3D face-centered cubic lattice."""
    x = np.arange(nx) * a
    y = np.arange(ny) * b
    z = np.arange(nz) * c
    x_coords, y_coords, z_coords = np.meshgrid(x, y, z)

    # Add atoms on the faces of each cell
    x_face1 = x_coords + a / 2
    y_face1 = y_coords + b / 2
    z_face1 = z_coords

    x_face2 = x_coords + a / 2
    y_face2 = y_coords
    z_face2 = z_coords + c / 2

    x_face3 = x_coords
    y_face3 = y_coords + b / 2
    z_face3 = z_coords + c / 2

    return (x_coords, y_coords, z_coords), (x_face1, y_face1, z_face1), (x_face2, y_face2, z_face2), (x_face3, y_face3, z_face3)

def generate_3d_hexagonal(nx, ny, nz, a, b, c):
    """Generates coordinates for a 3D hexagonal lattice."""
    x = np.arange(nx) * a
    y = np.arange(ny) * b
    z = np.arange(nz) * c
    x_coords, y_coords, z_coords = np.meshgrid(x, y, z)
    return x_coords, y_coords, z_coords
