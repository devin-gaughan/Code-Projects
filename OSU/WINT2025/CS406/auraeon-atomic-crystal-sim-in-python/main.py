import tkinter as tk
from tkinter import ttk, colorchooser
from elements import ELEMENT_DATA
from lattice import (
    generate_2d_simple_cubic, generate_2d_triangular, generate_2d_hexagonal,
    generate_3d_simple_cubic, generate_bcc, generate_fcc
)
from visualization import plot_2d_lattice, plot_3d_lattice

# Main function to create the GUI
def main():
    root = tk.Tk()
    root.title("Auraeon - Crystal Lattice Simulator v0.3.1")
    root.geometry("600x600")  # Set default window size

    # Apply a theme for modern styling
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 12), padding=8)
 
    # Lattice constant variables
    lattice_a = tk.DoubleVar(value=1.0)
    lattice_b = tk.DoubleVar(value=1.0)
    lattice_c = tk.DoubleVar(value=1.0)
    lattice_alpha = tk.DoubleVar(value=90.0)
    lattice_beta = tk.DoubleVar(value=90.0)
    lattice_gamma = tk.DoubleVar(value=90.0)
    
    # Default elements for selection
    selected_element_1 = tk.StringVar(value="Fe")
    selected_element_2 = tk.StringVar(value="C")

    # Frame for Element Selection
    frame_selection = ttk.Frame(root, padding=10)
    frame_selection.grid(row=0, column=0, columnspan=2, sticky="ew")

    # Element selection dropdowns
    ttk.Label(frame_selection, text="Select Element 1 (Corners):").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    element_combo_1 = ttk.Combobox(frame_selection, textvariable=selected_element_1, values=list(ELEMENT_DATA.keys()), width=12)
    element_combo_1.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(frame_selection, text="Select Element 2 (Centers/Faces):").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    element_combo_2 = ttk.Combobox(frame_selection, textvariable=selected_element_2, values=list(ELEMENT_DATA.keys()), width=12)
    element_combo_2.grid(row=1, column=1, padx=10, pady=5)

    # Function for Color Picker
    def pick_color(element_var):
        """Allows user to select a color for a given element variable."""
        element = element_var.get()
        initial_color = ELEMENT_DATA[element]["color"]
        chosen_color = colorchooser.askcolor(color=initial_color, title=f"Pick color for {element}")

        # Updates the color if a new one was chosen
        if chosen_color[1]:
            ELEMENT_DATA[element]["color"] = chosen_color[1]
            print(f"Updated color for {element} to {chosen_color[1]}")

    # Frame for Color Selection
    frame_colors = ttk.Frame(root, padding=10)
    frame_colors.grid(row=1, column=0, columnspan=2, sticky="ew")

    ttk.Button(frame_colors, text="Pick Color (Element 1)", command=lambda: pick_color(selected_element_1), width=18).grid(row=0, column=0, padx=5, pady=5)
    ttk.Button(frame_colors, text="Pick Color (Element 2)", command=lambda: pick_color(selected_element_2), width=18).grid(row=0, column=1, padx=5, pady=5)
    
    # Frame for lattice constants sliders
    frame_lattice_constants = ttk.LabelFrame(root, text="Lattice Constants", padding=10)
    frame_lattice_constants.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
    
    # Function to create sliders
    def add_slider(frame, label, variable, row, from_val, to_val):
        ttk.Label(frame, text=label).grid(row=row, column=0, sticky="w", padx=5, pady=2)
        slider = ttk.Scale(frame, from_=from_val, to=to_val, orient="horizontal", variable=variable, length=200)
        slider.grid(row=row, column=1, padx=5, pady=2, sticky="ew")
        return slider
    
    # Create sliders for each lattice prameter
    add_slider(frame_lattice_constants, "a (Å):", lattice_a, 0, 0.5, 10.0)
    add_slider(frame_lattice_constants, "b (Å):", lattice_b, 1, 0.5, 10.0)
    add_slider(frame_lattice_constants, "c (Å):", lattice_c, 2, 0.5, 10.0)
    add_slider(frame_lattice_constants, "α (°):", lattice_alpha, 3, 30.0, 150.0)
    add_slider(frame_lattice_constants, "β (°):", lattice_beta, 4, 30.0, 150.0)
    add_slider(frame_lattice_constants, "γ (°):", lattice_gamma, 5, 30.0, 150.0)       
    
    # Function to Generate Lattices
    def generate_and_plot(lattice_type):
        """Handles lattice generation and visualization."""
        grid_size = 5
        a, b, c = lattice_a.get(), lattice_b.get(), lattice_c.get()
        
        element_1 = selected_element_1.get()
        element_2 = selected_element_2.get()

        color_1 = ELEMENT_DATA[element_1]["color"]
        color_2 = ELEMENT_DATA[element_2]["color"]
        radius_1 = ELEMENT_DATA[element_1]["radius"]
        radius_2 = ELEMENT_DATA[element_2]["radius"]

        # 2D Lattices
        if lattice_type == "2d_sc":
            x, y = generate_2d_simple_cubic(grid_size, a, b)
            plot_2d_lattice(x, y, f"2D Simple Cubic ({element_1}) (a={a:.2f}, b={b:.2f})", color_1, radius_1 * 100)
        elif lattice_type == "2d_tri":
            x, y = generate_2d_triangular(grid_size, a, b)
            plot_2d_lattice(x, y, f"2D Triangular ({element_1}) (a={a:.2f}, b={b:.2f})", color_1, radius_1 * 100)
        elif lattice_type == "2d_hex":
            x, y = generate_2d_hexagonal(grid_size, a, b)
            plot_2d_lattice(x, y, f"2D Hexagonal ({element_1}) (a={a:.2f}, b={b:.2f})", color_1, radius_1 * 100)

        # 3D Lattices
        elif lattice_type == "3d_sc":
            x, y, z = generate_3d_simple_cubic(grid_size, a, b, c)
            plot_3d_lattice(x, y, z, f"3D Simple Cubic ({element_1}) (a={a:.2f}, b:{b:.2f}, c={c:.2f})", color_1, radius_1 * 100)
        
        elif lattice_type == "3d_bcc":
            (x_c, y_c, z_c), (x_b, y_b, z_b) = generate_bcc(grid_size, a, b, c)
            plot_3d_lattice(
                [x_c.ravel(), x_b.ravel()],
                [y_c.ravel(), y_b.ravel()],
                [z_c.ravel(), z_b.ravel()],
                title=f"3D BCC with {element_1} and {element_2} (a={a:.2f}, b={b:.2f}, c={c:.2f})",
                colors=[color_1, color_2],
                marker_sizes=[radius_1 * 100, radius_2 * 100],
                elements=[element_1, element_2]
            )
        elif lattice_type == "3d_fcc":
            (x_c, y_c, z_c), fcc_offsets = generate_fcc(grid_size, a, b, c)
            all_x = [x_c.ravel()]
            all_y = [y_c.ravel()]
            all_z = [z_c.ravel()]
            for (ox, oy, oz) in fcc_offsets:
                all_x.append(ox.ravel())
                all_y.append(oy.ravel())
                all_z.append(oz.ravel())
            plot_3d_lattice(
                all_x, all_y, all_z,
                title=f"3D FCC with {element_1} and {element_2} (a={a:.2f}, b={b:.2f}, c={c:.2f})",
                colors=[color_1, color_2],
                marker_sizes=[radius_1 * 100, radius_2 * 100],
                elements=[element_1, element_2]
            )
                   
    
    # Frame for Lattice Buttons (Grid-Aligned)
    frame_lattices = ttk.Frame(root, padding=10)
    frame_lattices.grid(row=2, column=0, columnspan=2, sticky="ew")

    # Lattice buttons for 2D and 3D structures
    lattice_buttons = [
        ("2D Simple Cubic", "2d_sc"),
        ("2D Triangular", "2d_tri"),
        ("2D Hexagonal", "2d_hex"),
        ("3D Simple Cubic", "3d_sc"),
        ("3D BCC", "3d_bcc"),
        ("3D FCC", "3d_fcc"),
    ]

    # Create buttons for each lattice type
    for i, (text, lattice_type) in enumerate(lattice_buttons):
        row, col = divmod(i, 2)  # Auto-grid in two columns
        ttk.Button(frame_lattices, text=text, command=lambda lt=lattice_type: generate_and_plot(lt), width=20).grid(row=row, column=col, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
