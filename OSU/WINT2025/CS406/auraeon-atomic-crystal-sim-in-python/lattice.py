import numpy as np

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