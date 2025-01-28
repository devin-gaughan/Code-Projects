import tkinter as tk
from tkinter import ttk, colorchooser
from elements import ELEMENT_DATA
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
    root.title("Auraeon - Crystal Lattice Simulator v0.2.1")

    # A Tk variable to store the selected element
    selected_element_1 = tk.StringVar(value="Fe")
    selected_element_2 = tk.StringVar(value="C")
    
    # The combobox to select an element
    tk.Label(root, text="Select Element 1 (Example: Corner Atoms):").pack(pady=5)
    element_combo_1 = ttk.Combobox(root, textvariable=selected_element_1, values=list(ELEMENT_DATA.keys()))
    element_combo_1.pack(pady=5)
    
    tk.Label(root, text="Select Element 2 (Example: Center Atoms):").pack(pady=5)
    element_combo_2 = ttk.Combobox(root, textvariable=selected_element_2, values=list(ELEMENT_DATA.keys()))
    element_combo_2.pack(pady=5)
    
    def pick_color():
        element = selected_element_1.get()
        initial_color = ELEMENT_DATA[element]["color"]
        chosen_color = colorchooser.askcolor(color=initial_color, title=f"Pick a color for {element}")
        if chosen_color[1]: # If a color was chosen
            ELEMENT_DATA[element]["color"] = chosen_color[1]
            print(f"Updated color for {element} to {chosen_color[1]}") # Debug log
            
    def generate_and_plot_multi(lattice_type):
        """ Generates a multi element lattice and plots it """
        grid_size = 5
        a = 1.0
        
        # Get user-selected elements
        element_1 = selected_element_1.get() # For sub-lattice A
        element_2 = selected_element_2.get() # For sub-lattice B
        
        # Get their colors and radii
        color_1 = ELEMENT_DATA[element_1]["color"]
        color_2 = ELEMENT_DATA[element_2]["color"]
        radius_1 = ELEMENT_DATA[element_1]["radius"]
        radius_2 = ELEMENT_DATA[element_2]["radius"]
        
        # Plot based on lattice type
        if lattice_type == "3d_bcc":
            # Corner atoms -> element 1, Center atoms -> element 2
            (x_c, y_c, z_c), (x_b, y_b, z_b) = generate_bcc(grid_size, a)
            
            # Plot corner atoms (sub lattice A)
            plot_3d_lattice(
                x_c.ravel(), y_c.ravel(), z_c.ravel(),
                title=f"3D BCC with {element_1} and {element_2}",
                color=color_1, marker_size=radius_1 * 100
            )
            
            # Plot center atoms (sub lattice B)
            plot_3d_lattice(
                x_b.ravel(), y_b.ravel(), z_b.ravel(),
                title=f"3D BCC with {element_1} and {element_2}",
                color=color_2, marker_size=radius_2 * 100
            )
            
        elif lattice_type == "3d_fcc":
            # Corner atoms -> element 1, Face atoms -> element 2
            (x_c, y_c, z_c), fcc_offsets = generate_fcc(grid_size, a)
            
            # Plot corner atoms (sub lattice A)
            plot_3d_lattice(
                x_c.ravel(), y_c.ravel(), z_c.ravel(),
                title=f"3D FCC with {element_1} and {element_2}",
                color=color_1, marker_size=radius_1 * 100
            )
            
            # Plot face centered atoms (sub lattice B)
            for offset in fcc_offsets:
                ox, oy, oz = offset
                plot_3d_lattice(
                    ox.ravel(), oy.ravel(), oz.ravel(),
                    title=f"3D FCC with {element_1} and {element_2}",
                    color=color_2, marker_size=radius_2 * 100
                )
        
    def generate_and_plot(lattice_type):
        """ Generate and plot a lattice based on the selected type, element, and atom color """
        import numpy as np
        grid_size = 5
        a = 1.0
        element = selected_element_1.get()
        color = ELEMENT_DATA[element]["color"]
        radius = ELEMENT_DATA[element]["radius"]
        marker_size = radius * 100 # Scaled for better visibility
        
        if lattice_type == "sc":
            x, y = generate_2d_simple_cubic(grid_size, a)
            plot_2d_lattice(x, y, f"2D Simple Cubic ({element})", color, marker_size)
        elif lattice_type == "tri":
            x, y = generate_2d_triangular(grid_size, a)
            plot_2d_lattice(x, y, f"2D Triangular ({element})", color, marker_size)
        elif lattice_type == "hex":
            x, y = generate_2d_hexagonal(grid_size, a)
            plot_2d_lattice(x, y, f"2D Hexagonal ({element})", color, marker_size)
        elif lattice_type =="3d_sc":
            x, y, z = generate_3d_simple_cubic(grid_size, a)
            plot_3d_lattice(x, y, z, f"3D Simple Cubic ({element})", color, marker_size)
        elif lattice_type == "3d_bcc":
            (x_c, y_c, z_c), (x_b, y_b, z_b) = generate_bcc(grid_size, a)
            ''' Combining corner and center atoms into one scatter plot '''
            all_x = np.concatenate([x_c.ravel(), x_b.ravel()])
            all_y = np.concatenate([y_c.ravel(), y_b.ravel()])
            all_z = np.concatenate([z_c.ravel(), z_b.ravel()])
            plot_3d_lattice(all_x, all_y, all_z, "3D BCC ({element})", color, marker_size)
            
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
                "3D FCC ({element})", 
                color, 
                marker_size
            )

    # Dropdown for Sub Lattice A (Example: Corner Atoms)
    tk.Label(root, text="Select Element for Sub Lattice A (Corners):").pack(pady=5)
    element_combo_1 = ttk.Combobox(root, textvariable=selected_element_1, values=list(ELEMENT_DATA.keys())) 
    element_combo_1.pack(pady=5)
    
    # Dropdown for Sub Lattice B (Example: Center or Face Atoms)
    tk.Label(root, text="Select Element for Sub Lattice B (Centers or Faces):").pack(pady=5)
    element_combo_2 = ttk.Combobox(root, textvariable=selected_element_2, values=list(ELEMENT_DATA.keys()))
    element_combo_2.pack(pady=5)
    
    # Buttons to generate and plot different types of lattices
    tk.Button(root, text="3D BCC (Multi Element)", command=lambda: generate_and_plot_multi("3d_bcc")).pack(pady=5)
    tk.Button(root, text="3D FCC (Multi Element)", command=lambda: generate_and_plot_multi("3d_fcc")).pack(pady=5)
    tk.Button(root, text="Pick Color", command=pick_color).pack(pady=5)
    tk.Button(root, text="Simple Cubic", command=lambda: generate_and_plot("sc")).pack(pady=5)
    tk.Button(root, text="Triangular", command=lambda: generate_and_plot("tri")).pack(pady=5)
    tk.Button(root, text="Hexagonal", command=lambda: generate_and_plot("hex")).pack(pady=5)
    tk.Button(root, text="3D Simple Cubic", command=lambda: generate_and_plot("3d_sc")).pack(pady=5)
    tk.Button(root, text="3D BCC", command=lambda: generate_and_plot("3d_bcc")).pack(pady=5)
    tk.Button(root, text="3D FCC", command=lambda: generate_and_plot("3d_fcc")).pack(pady=5)




    root.mainloop()

if __name__ == "__main__":
    main()
