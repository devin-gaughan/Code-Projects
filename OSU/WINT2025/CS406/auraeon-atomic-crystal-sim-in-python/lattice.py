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
