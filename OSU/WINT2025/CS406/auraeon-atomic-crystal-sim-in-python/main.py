import tkinter as tk
from tkinter import ttk, colorchooser
import numpy as np
from elements import ELEMENT_DATA
from lattice import (
    generate_2d_simple_cubic, generate_2d_triangular, generate_2d_hexagonal,
    generate_3d_simple_cubic, generate_bcc, generate_fcc, generate_3d_hexagonal
)
from visualization import plot_2d_lattice, plot_3d_lattice

def main():
    root = tk.Tk()
    root.title("Auraeon - Crystal Lattice Simulator v0.3.3")
    root.geometry("700x700")

    # Lattice Constants
    lattice_a = tk.DoubleVar(value=5.0)
    lattice_b = tk.DoubleVar(value=5.0)
    lattice_c = tk.DoubleVar(value=5.0)
    lattice_alpha = tk.DoubleVar(value=90.0)
    lattice_beta = tk.DoubleVar(value=90.0)
    lattice_gamma = tk.DoubleVar(value=90.0)

    # Unit Cell Counts
    unit_cells_x = tk.IntVar(value=5)
    unit_cells_y = tk.IntVar(value=5)
    unit_cells_z = tk.IntVar(value=5)

    # Element Selections
    selected_element_1 = tk.StringVar(value="Fe")
    selected_element_2 = tk.StringVar(value="C")
    
    # Color pickers for each element
    element_color_1 = tk.StringVar(value=ELEMENT_DATA[selected_element_1.get()]["color"])
    element_color_2 = tk.StringVar(value=ELEMENT_DATA[selected_element_2.get()]["color"])

    def choose_color(color_var):
        """Opens a color picker dialog and updates the selected color."""
        chosen = colorchooser.askcolor(title="Pick an Atom Color")
        if chosen and chosen[1]:
            color_var.set(chosen[1])

    # ========== UI Layout ==========
    # 1. Element Selection
    frame_selection = ttk.LabelFrame(root, text="Element Selection", padding=10)
    frame_selection.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    # Element 1
    ttk.Label(frame_selection, text="Element 1:").grid(row=0, column=0, padx=5, pady=5)
    combo_1 = ttk.Combobox(
        frame_selection,
        textvariable=selected_element_1,
        values=list(ELEMENT_DATA.keys()),
        width=12
    )
    combo_1.grid(row=0, column=1, padx=5, pady=5)
    color_btn_1 = ttk.Button(
        frame_selection,
        text="Pick Color",
        command=lambda: choose_color(element_color_1)
    )
    color_btn_1.grid(row=0, column=2, padx=5, pady=5)

    # Element 2
    ttk.Label(frame_selection, text="Element 2:").grid(row=1, column=0, padx=5, pady=5)
    combo_2 = ttk.Combobox(
        frame_selection,
        textvariable=selected_element_2,
        values=list(ELEMENT_DATA.keys()),
        width=12
    )
    combo_2.grid(row=1, column=1, padx=5, pady=5)
    color_btn_2 = ttk.Button(
        frame_selection,
        text="Pick Color",
        command=lambda: choose_color(element_color_2)
    )
    color_btn_2.grid(row=1, column=2, padx=5, pady=5)

    # 2. Lattice Constants + Angles
    frame_constants = ttk.LabelFrame(root, text="Lattice Constants", padding=10)
    frame_constants.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def add_slider(parent, label, var, row, from_val, to_val):
        ttk.Label(parent, text=label).grid(row=row, column=0, sticky="w", padx=5, pady=2)
        slider = ttk.Scale(parent, from_=from_val, to=to_val, orient="horizontal", variable=var, length=200)
        slider.grid(row=row, column=1, padx=5, pady=2, sticky="ew")
        lbl_val = ttk.Label(parent, text=f"{var.get():.2f}")
        lbl_val.grid(row=row, column=2, padx=5, pady=2)

        def update_label(*args):
            lbl_val.config(text=f"{var.get():.2f}")

        var.trace_add("write", update_label)
        return slider

    # Sliders for (a, b, c, alpha, beta, gamma)
    add_slider(frame_constants, "a (Å):", lattice_a, 0, 1.0, 10.0)
    add_slider(frame_constants, "b (Å):", lattice_b, 1, 1.0, 10.0)
    add_slider(frame_constants, "c (Å):", lattice_c, 2, 1.0, 10.0)
    add_slider(frame_constants, "α (°):", lattice_alpha, 3, 30.0, 150.0)
    add_slider(frame_constants, "β (°):", lattice_beta, 4, 30.0, 150.0)
    add_slider(frame_constants, "γ (°):", lattice_gamma, 5, 30.0, 150.0)

    # 3. Unit Cell Counts
    frame_cells = ttk.LabelFrame(root, text="Unit Cell Counts", padding=10)
    frame_cells.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def add_int_slider(parent, label, var, row, from_val, to_val):
        ttk.Label(parent, text=label).grid(row=row, column=0, sticky="w", padx=5, pady=2)
        slider = ttk.Scale(parent, from_=from_val, to=to_val, orient="horizontal", variable=var, length=200)
        slider.grid(row=row, column=1, padx=5, pady=2, sticky="ew")
        lbl_val = ttk.Label(parent, text=f"{var.get()} cells")
        lbl_val.grid(row=row, column=2, padx=5, pady=2)

        def update_label(*args):
            lbl_val.config(text=f"{var.get()} cells")

        var.trace_add("write", update_label)
        return slider

    add_int_slider(frame_cells, "nx:", unit_cells_x, 0, 1, 10)
    add_int_slider(frame_cells, "ny:", unit_cells_y, 1, 1, 10)
    add_int_slider(frame_cells, "nz:", unit_cells_z, 2, 1, 10)

    # 4. Generate Lattice Buttons
    frame_lattices = ttk.LabelFrame(root, text="Generate Lattice", padding=10)
    frame_lattices.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def generate_and_plot(lattice_type):
        """Handles lattice generation & visualization when user clicks a button."""
        # Gather slider values
        a, b, c = lattice_a.get(), lattice_b.get(), lattice_c.get()
        alpha, beta, gamma = lattice_alpha.get(), lattice_beta.get(), lattice_gamma.get()
        nx, ny, nz = unit_cells_x.get(), unit_cells_y.get(), unit_cells_z.get()

        # Element selections & colors
        e1 = selected_element_1.get()
        e2 = selected_element_2.get()
        col1 = element_color_1.get() or ELEMENT_DATA[e1]["color"]
        col2 = element_color_2.get() or ELEMENT_DATA[e2]["color"]

        # Marker sizes from atomic radii
        rad1 = ELEMENT_DATA[e1]["radius"] * 80
        rad2 = ELEMENT_DATA[e2]["radius"] * 80

        # Lattice generation functions
        lattice_funcs = {
            "2d_sc": generate_2d_simple_cubic,
            "2d_tri": generate_2d_triangular,
            "2d_hex": generate_2d_hexagonal,
            "3d_sc": generate_3d_simple_cubic,
            "3d_bcc": generate_bcc,
            "3d_fcc": generate_fcc,
            "3d_hex": generate_3d_hexagonal,
        }

        # Colors, sizes, elements arrays
        colors = [col1, col2]
        sizes = [rad1, rad2]
        elems = [e1, e2]

        # Branch by lattice type
        if lattice_type in ["2d_sc", "2d_tri", "2d_hex"]:
            x_total, y_total = lattice_funcs[lattice_type](nx, ny, a, b)
            # If we want to show TWO elements in 2D, replicate the array for both
            x_list = [x_total, x_total]
            y_list = [y_total, y_total]

            plot_2d_lattice(
                x_list, y_list, a, b,
                title=f"{lattice_type.upper()} Lattice (nx={nx}, ny={ny})",
                colors=colors,
                marker_sizes=sizes,
                elements=elems
            )

        elif lattice_type == "3d_sc":
            x, y, z = lattice_funcs[lattice_type](nx, ny, nz, a, b, c)
            # If single element array => unify as second array for multi-element
            x_list = [x, x]
            y_list = [y, y]
            z_list = [z, z]

            plot_3d_lattice(
                x_list, y_list, z_list, a, b, c,
                title=f"3D SC Lattice (nx={nx}, ny={ny}, nz={nz})",
                colors=colors, marker_sizes=sizes, elements=elems
            )

        elif lattice_type == "3d_hex":
            x, y, z = lattice_funcs[lattice_type](nx, ny, nz, a, b, c)
            # Again, replicate if you want element_1 and element_2 shown
            x_list = [x, x]
            y_list = [y, y]
            z_list = [z, z]

            plot_3d_lattice(
                x_list, y_list, z_list, a, b, c,
                title=f"3D HEX Lattice (nx={nx}, ny={ny}, nz={nz})",
                colors=colors, marker_sizes=sizes, elements=elems
            )

        elif lattice_type == "3d_bcc":
            (x_c, y_c, z_c), (x_b, y_b, z_b) = lattice_funcs[lattice_type](nx, ny, nz, a, b, c)
            # Corners = element_1, Center = element_2
            x_list = [x_c, x_b]
            y_list = [y_c, y_b]
            z_list = [z_c, z_b]

            plot_3d_lattice(
                x_list, y_list, z_list, a, b, c,
                title=f"3D BCC Lattice (nx={nx}, ny={ny}, nz={nz})",
                colors=colors, marker_sizes=sizes, elements=elems
            )

        elif lattice_type == "3d_fcc":
            (x_c, y_c, z_c), fcc_offsets = lattice_funcs[lattice_type](nx, ny, nz, a, b, c)
            # Corners -> element_1, All face offsets combined -> element_2
            offset_x = []
            offset_y = []
            offset_z = []
            for (ox, oy, oz) in fcc_offsets:
                offset_x.append(ox.ravel())
                offset_y.append(oy.ravel())
                offset_z.append(oz.ravel())

            x_faces = np.concatenate(offset_x)
            y_faces = np.concatenate(offset_y)
            z_faces = np.concatenate(offset_z)

            x_list = [x_c, x_faces]
            y_list = [y_c, y_faces]
            z_list = [z_c, z_faces]

            plot_3d_lattice(
                x_list, y_list, z_list, a, b, c,
                title=f"3D FCC Lattice (nx={nx}, ny={ny}, nz={nz})",
                colors=colors, marker_sizes=sizes, elements=elems
            )

    # Lattice type buttons
    all_lattices = [
        ("2D Simple Cubic", "2d_sc"),
        ("2D Triangular",   "2d_tri"),
        ("2D Hexagonal",    "2d_hex"),
        ("3D Simple Cubic", "3d_sc"),
        ("3D BCC",          "3d_bcc"),
        ("3D FCC",          "3d_fcc"),
        ("3D Hexagonal",    "3d_hex"),
    ]
    for i, (text, lt) in enumerate(all_lattices):
        row, col = divmod(i, 2)
        ttk.Button(
            frame_lattices,
            text=text,
            command=lambda latt=lt: generate_and_plot(latt),
            width=20
        ).grid(row=row, column=col, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
