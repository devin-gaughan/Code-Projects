import tkinter as tk
from lattice import (
    generate_2d_simple_cubic,
    generate_2d_triangular,
    generate_2d_hexagonal
)
from visualization import plot_2d_lattice

def main():
    root = tk.Tk()
    root.title("2D Lattice Generator")

    def generate_and_plot(lattice_type):
        grid_size = 5
        a = 1.0
        if lattice_type == "sc":
            x, y = generate_2d_simple_cubic(grid_size, a)
            plot_2d_lattice(x, y, "2D Simple Cubic")
        elif lattice_type == "tri":
            x, y = generate_2d_triangular(grid_size, a)
            plot_2d_lattice(x, y, "2D Triangular")
        elif lattice_type == "hex":
            x, y = generate_2d_hexagonal(grid_size, a)
            plot_2d_lattice(x, y, "2D Hexagonal")

    tk.Button(root, text="Simple Cubic",
              command=lambda: generate_and_plot("sc")).pack(pady=5)
    tk.Button(root, text="Triangular",
              command=lambda: generate_and_plot("tri")).pack(pady=5)
    tk.Button(root, text="Hexagonal",
              command=lambda: generate_and_plot("hex")).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
