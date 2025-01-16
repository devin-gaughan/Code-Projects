import matplotlib.pyplot as plt
import numpy as np

def plot_2d_lattice(x, y, title="2D Lattice"):
    """ plots a 2D lattice using a scatter plot in matplotlib """
    plt.figure(figsize=(6, 6))
    plt.scatter(x, y, c='blue', s=50)
    plt.title(title)
    plt.xlabel('X (Å)')
    plt.ylabel('Y (Å)')
    plt.grid(True)
    plt.show()
    
        