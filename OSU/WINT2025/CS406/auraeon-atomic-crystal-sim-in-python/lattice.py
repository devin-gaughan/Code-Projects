import numpy as np

""" 2D GENERATORS """
""" 2D Simple Cubic """
def generate_2d_simple_cubic(grid_size, a):
    """ Generate (x, y) points for a 2D simple cubic lattice. 
    grid_size: number of atoms along one axis
    a: lattice constant (spacing between atoms)
    """
    x, y = np.meshgrid(
        np.arange(0, grid_size * a, a),
        np.arange(0, grid_size * a, a)
    )
    return x, y


""" 2D Triangular """
def generate_2d_triangular(grid_size, a):
    """ Generate (x, y) points for a 2D triangular lattice. """
    x, y = np.meshgrid(
        np.arange(0, grid_size * a, a),
        np.arange(0, grid_size * a, a)
    )
    ''' Shift every other row by half of the lattice constant '''
    x[1::2] += a / 2
    return x, y

""" 2D Hexagonal """
def generate_2d_hexagonal(grid_size, a):
    x, y = generate_2d_triangular(grid_size, a)
    y *= np.sqrt(3) / 2 #Scale for hex geometry
    return x, y

""" 3D GENERATORS """
""" 3D Simple Cubic """
def generate_3d_simple_cubic(grid_size, a):
    import numpy as np
    x_vals = np.arange(0, grid_size * a, a)
    y_vals = np.arange(0, grid_size * a, a)
    z_vals = np.arange(0, grid_size * a, a)
    x, y, z = np.meshgrid(x_vals, y_vals, z_vals)
    return x, y, z

""" 3D BCC """
def generate_bcc(grid_size, a):
    x, y, z = generate_3d_simple_cubic(grid_size, a)
    x_bcc = x + a / 2
    y_bcc = y + a / 2
    z_bcc = z + a / 2
    return (x, y, z), (x_bcc, y_bcc, z_bcc)

""" 3D FCC """
def generate_fcc(grid_size, a):
    x, y, z = generate_3d_simple_cubic(grid_size, a)
    ''' Offsets for face centers '''
    fcc_offsets = [
        (0, a/2, a/2), (a, a/2, a/2),
        (a/2, 0, a/2), (a/2, a, a/2),
        (a/2, a/2, 0), (a/2, a/2, a)
    ]
    offset_arrays = []
    for (ox, oy, oz) in fcc_offsets:
        offset_arrays.append((x + ox, y + oy, z + oz))
        
    return (x, y, z), offset_arrays