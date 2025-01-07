import tkinter as tk
from tkinter import ttk
from lattice import generate_2d_simple_cubic, generate_2d_triangular, generate_2d_hexagonal
from visualization import plot_2d_lattice
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Phase 2
# 2D Simple Cubic Lattice
# Default Parameters
grid_size = 5
a = 1.0
lattice_type = "simple_cubic"

# Plotting Function
def update_plot(*args):
    global grid_size, a, lattice_type
    grid_size = int(grid_size_slider.get())
    a = lattice_constant_slider.get()

    ax.clear()  # Clear previous plot

    # Generate and plot based on lattice type
    if lattice_type == "simple_cubic":
        x, y = generate_2d_simple_cubic(grid_size, a)
        plot_2d_lattice(ax, x, y, "Simple Cubic")
    elif lattice_type == "triangular":
        x, y = generate_2d_triangular(grid_size, a)
        plot_2d_lattice(ax, x, y, "Triangular")


    # Redraw the canvas
    canvas.draw()

# Switch Lattice Type
def set_lattice_type(lattice):
    global lattice_type
    lattice_type = lattice
    update_plot()

# GUI Setup
root = tk.Tk()
root.title("2D Lattice Generator")

# Lattice Type Selection Buttons
label = tk.Label(root, text="Select Lattice Type:")
label.pack(pady=10)

tk.Button(root, text="Simple Cubic", command=lambda: set_lattice_type("simple_cubic")).pack(pady=5)
tk.Button(root, text="Triangular", command=lambda: set_lattice_type("triangular")).pack(pady=5)
# Grid Size Slider
tk.Label(root, text="Grid Size (Number of Atoms per Side):").pack(pady=10)
grid_size_slider = ttk.Scale(root, from_=3, to=20, orient='horizontal', length=300, command=update_plot)
grid_size_slider.set(grid_size)
grid_size_slider.pack(pady=5)

# Lattice Constant Slider
tk.Label(root, text="Lattice Constant (Å):").pack(pady=10)
lattice_constant_slider = ttk.Scale(root, from_=0.5, to=5.0, orient='horizontal', length=300, command=update_plot)
lattice_constant_slider.set(a)
lattice_constant_slider.pack(pady=5)

# Matplotlib Canvas for Live Plot
fig, ax = plt.subplots(figsize=(6, 6))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(pady=20)

# Initial Plot
update_plot()

# Start GUI Loop
root.mainloop()


# Phase 3
# 3D Simple Cubic Lattice
"""
from lattice import generate_3d_simple_cubic
from visualization import plot_3d_lattice

x, y, z = generate_3d_simple_cubic(grid_size, a)
plot_3d_lattice(x, y, z)

"""

# Phase 4
# 2D Body-Centered Cubic Lattice
"""
    from lattice import generate_bcc
from visualization import plot_bcc_lattice

x, y, z, x_bcc, y_bcc, z_bcc = generate_bcc(grid_size, a)
plot_bcc_lattice(x, y, z, x_bcc, y_bcc, z_bcc)

"""

# Phase 5
# 3D Simple Cubic Lattice (pyVista)
"""
    from lattice import generate_3d_simple_cubic
from visualization import plot_3d_interactive

x, y, z = generate_3d_simple_cubic(grid_size, a)
plot_3d_interactive(x, y, z)

"""
