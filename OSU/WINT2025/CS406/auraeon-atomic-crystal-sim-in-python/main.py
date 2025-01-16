import tkinter as tk
from tkinter import ttk
import numpy as np

from lattice import (
    generate_2d_simple_cubic, generate_2d_triangular
)
from visualization import plot_2d_lattice

''' default parameters '''
DIMENSION = "2D"
LATTICE_TYPE = "simple_cubic"

def update_plot(*args):
    """ redraws the plot based on the current parameters """
    grid_size_val = grid_size_slider.get()
    a_val = lattice_constant_slider.get()

    if DIMENSION == "2D":
        if LATTICE_TYPE == "simple_cubic":
            x, y = generate_2d_simple_cubic(int(grid_size_val), a_val)
            plot_2d_lattice(x, y, title="2D Simple Cubic Lattice")   
        elif LATTICE_TYPE == "triangular" and DIMENSION == "2D":
            x, y = generate_2d_triangular(int(grid_size_val), a_val)
            plot_2d_lattice(x, y, title="2D Triangular Lattice")  
        else:
            print("Invalid dimension or lattice type selected.")
        

def set_dimension(dim):
    global DIMENSION
    DIMENSION = dim
    update_plot()
    
def set_lattice_type(lattice):
    global LATTICE_TYPE
    LATTICE_TYPE = lattice
    update_plot()
    
''' creates the main window '''
root = tk.Tk()
root.title("Auraeon - Atomic Crystal Lattice Simulation")

''' lattice type selection frame '''
frame_lattice =tk.Frame(root)
frame_lattice.pack(pady=10)
tk.Label(frame_lattice, text="Select Lattice Type: ").pack(side=tk.LEFT, padx=5)
tk.Button(frame_lattice, text="Simple Cubic", command=lambda: set_lattice_type("simple_cubic")).pack(side=tk.LEFT, padx=5)
tk.Button(frame_lattice, text="Triangular", command=lambda: set_lattice_type("triangular")).pack(side=tk.LEFT, padx=5)

''' sliders for grid size and lattice constant '''
tk.Label(root, text="Grid Size: ").pack()
grid_size_slider = ttk.Scale(root, from_=2, to=20, orient='horizontal', length=300, command=update_plot)
grid_size_slider.set(5)
grid_size_slider.pack(pady=5)

tk.Label(root, text="Lattice Constant (Å): ").pack()
lattice_constant_slider = ttk.Scale(root, from_=0.5, to=5.0, orient='horizontal', length=300, command=update_plot)
lattice_constant_slider.set(1.0)
lattice_constant_slider.pack(pady=5)


root.mainloop()
