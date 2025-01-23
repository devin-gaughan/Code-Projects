import tkinter as tk
from lattice import (
    generate_2d_simple_cubic,
    generate_2d_triangular,
    generate_2d_hexagonal,
    generate_3d_simple_cubic,
    generate_bcc,
    generate_fcc
)
from visualization import plot_2d_lattice, plot_3d_lattice

def main():
    root = tk.Tk()
    root.title("2D Lattice Generator")

    def generate_and_plot(lattice_type):
        import numpy as np
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
        elif lattice_type =="3d_sc":
            x, y, z = generate_3d_simple_cubic(grid_size, a)
            plot_3d_lattice(x, y, z, "3D Simple Cubic")
        elif lattice_type == "3d_bcc":
            (x_c, y_c, z_c), (x_b, y_b, z_b) = generate_bcc(grid_size, a)
            ''' Combining corner and center atoms into one scatter plot '''
            all_x = np.concatenate([x_c.ravel(), x_b.ravel()])
            all_y = np.concatenate([y_c.ravel(), y_b.ravel()])
            all_z = np.concatenate([z_c.ravel(), z_b.ravel()])
            plot_3d_lattice(all_x, all_y, all_z, "3D BCC")
            
        elif lattice_type == "3d_fcc":
            (x_c, y_c, z_c), fcc_offsets = generate_fcc(grid_size, a)
            all_x = [x_c.ravel()]
            all_y = [y_c.ravel()]
            all_z = [z_c.ravel()]
            for (ox, oy, oz) in fcc_offsets:
                all_x.append(ox.ravel())
                all_y.append(oy.ravel())
                all_z.append(oz.ravel())
            
            plot_3d_lattice(
                np.concatenate(all_x),
                np.concatenate(all_y),
                np.concatenate(all_z),
                "3D FCC"
            )


    tk.Button(root, text="Simple Cubic",
              command=lambda: generate_and_plot("sc")).pack(pady=5)
    tk.Button(root, text="Triangular",
              command=lambda: generate_and_plot("tri")).pack(pady=5)
    tk.Button(root, text="Hexagonal",
              command=lambda: generate_and_plot("hex")).pack(pady=5)
    tk.Button(root, text="3D Simple Cubic", command=lambda: generate_and_plot("3d_sc")).pack(pady=5)
    tk.Button(root, text="3D BCC", command=lambda: generate_and_plot("3d_bcc")).pack(pady=5)
    tk.Button(root, text="3D FCC", command=lambda: generate_and_plot("3d_fcc")).pack(pady=5)




    root.mainloop()

if __name__ == "__main__":
    main()
