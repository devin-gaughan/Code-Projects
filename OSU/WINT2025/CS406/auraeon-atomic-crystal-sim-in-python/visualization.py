import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def plot_2d_lattice(x, y, title="2D Lattice", color='blue', marker_size=50):
    # plots a 2D lattice using a scatter plot in matplotlib 
    plt.figure(figsize=(6, 6))
    plt.scatter(x, y, c=color, s=marker_size)
    plt.title(title)
    plt.xlabel('X (Å)')
    plt.ylabel('Y (Å)')
    plt.grid(True)
    plt.show()
    
def plot_3d_lattice(x, y, z, title="3D Lattice", color='blue', marker_size=50):
    # plots a 3D lattice using a scatter plot in matplotlib 
    fig = plt.figure(figsize=(7, 5))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c=color, s=marker_size)
    ax.set_title(title)
    ax.set_xlabel("X (Å)")
    ax.set_ylabel("Y (Å)")
    ax.set_zlabel("Z (Å)")
    plt.show()