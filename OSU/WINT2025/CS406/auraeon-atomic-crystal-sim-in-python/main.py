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
    root.title("Auraeon - Crystal Lattice Simulator v0.3.5")
    root.geometry("700x900")

    # ==================== TRACK CURRENT LATTICE TYPE ====================
    # If a lattice type isn't selected yet, default to '2d_sc'
    current_lattice_type = tk.StringVar(value="2d_sc")

    # ==================== CRYSTAL SYSTEM SELECTION ====================
    crystal_system = tk.StringVar(value="isometric")  # default system

    # ==================== LATTICE CONSTANTS & ANGLES ====================
    lattice_a = tk.DoubleVar(value=5.0)
    lattice_b = tk.DoubleVar(value=5.0)
    lattice_c = tk.DoubleVar(value=5.0)
    lattice_alpha = tk.DoubleVar(value=90.0)
    lattice_beta = tk.DoubleVar(value=90.0)
    lattice_gamma = tk.DoubleVar(value=90.0)

    # ==================== UNIT CELL COUNTS ====================
    unit_cells_x = tk.IntVar(value=5)
    unit_cells_y = tk.IntVar(value=5)
    unit_cells_z = tk.IntVar(value=5)

    # ==================== ELEMENT SELECTION & COLORS ====================
    selected_element_1 = tk.StringVar(value="Fe")
    selected_element_2 = tk.StringVar(value="C")
    element_color_1 = tk.StringVar(value=ELEMENT_DATA["Fe"]["color"])
    element_color_2 = tk.StringVar(value=ELEMENT_DATA["C"]["color"])

    # ==================== HELPER: RE-PLOT WHENEVER ANYTHING CHANGES ====================
    def refresh_plot(*args):
        """Re-call generate_and_plot() with the currently selected lattice type."""
        # Only re-plots if we actually have a lattice type
        lt = current_lattice_type.get()
        if lt:
            generate_and_plot(lt)

    # ==================== CHOOSE COLOR ====================
    def choose_color(color_var):
        """Opens a color picker dialog and updates the selected color, then re-plots."""
        chosen = colorchooser.askcolor(title="Pick an Atom Color")
        if chosen and chosen[1]:
            color_var.set(chosen[1])
        refresh_plot()  # refresh after color change

    # ==================== CRYSTAL SYSTEM HANDLER ====================
    def apply_crystal_system(*_):
        system = crystal_system.get()
        if system == "isometric":
            # a=b=c, α=β=γ=90
            lattice_b.set(lattice_a.get())
            lattice_c.set(lattice_a.get())
            lattice_alpha.set(90.0)
            lattice_beta.set(90.0)
            lattice_gamma.set(90.0)
        elif system == "orthorhombic":
            # α=β=γ=90, keep a,b,c distinct
            lattice_alpha.set(90.0)
            lattice_beta.set(90.0)
            lattice_gamma.set(90.0)
        elif system == "tetragonal":
            # a=b, c free, angles=90
            lattice_b.set(lattice_a.get())
            lattice_alpha.set(90.0)
            lattice_beta.set(90.0)
            lattice_gamma.set(90.0)
        elif system == "hexagonal":
            # a=b, angles=90,90,120
            lattice_b.set(lattice_a.get())
            lattice_alpha.set(90.0)
            lattice_beta.set(90.0)
            lattice_gamma.set(120.0)
        refresh_plot()  # re-plot after system changes

    def rotate_2d(x_array, y_array, alpha_degs):
        """
        Rotate 2D coordinates by alpha around the origin.
        alpha_degs is the rotation in degrees.
        """
        alpha = np.radians(alpha_degs)
        x_flat = x_array.ravel()
        y_flat = y_array.ravel()
        # 2D rotation matrix
        # [cosα  -sinα]
        # [sinα   cosα]
        cos_a = np.cos(alpha)
        sin_a = np.sin(alpha)

        x_rot = x_flat*cos_a - y_flat*sin_a
        y_rot = x_flat*sin_a + y_flat*cos_a

        # Reshape back to the original shape
        shape_2d = x_array.shape
        return x_rot.reshape(shape_2d), y_rot.reshape(shape_2d)
    
    def rotate_3d(x_array, y_array, z_array, alpha_degs, beta_degs, gamma_degs):
        """
        Rotate 3D coordinates around X (alpha), Y (beta), Z (gamma) in order:
        1.) Rotates by alpha around X
        2.) Rotates by beta around Y
        3.) Rotates by gamma around Z
        Angles are in degrees.
        """
        alpha = np.radians(alpha_degs)
        beta = np.radians(beta_degs)
        gamma = np.radians(gamma_degs)

        # Flatten
        x_flat = x_array.ravel()
        y_flat = y_array.ravel()
        z_flat = z_array.ravel()

        coords = np.vstack((x_flat, y_flat, z_flat))

        # 1) Rotate around X by alpha
        Rx = np.array([
            [1,          0,           0],
            [0,  np.cos(alpha), -np.sin(alpha)],
            [0,  np.sin(alpha),  np.cos(alpha)]
        ])

        # 2) Rotate around Y by beta
        Ry = np.array([
            [ np.cos(beta), 0, np.sin(beta)],
            [ 0,            1,           0 ],
            [-np.sin(beta), 0, np.cos(beta)]
        ])

        # 3) Rotate around Z by gamma
        Rz = np.array([
            [ np.cos(gamma), -np.sin(gamma), 0],
            [ np.sin(gamma),  np.cos(gamma), 0],
            [ 0,                 0,          1]
        ])

        # Combine: coords_rot = Rz * Ry * Rx * coords
        R = Rz @ Ry @ Rx
        coords_rot = R @ coords

        # Reshape back to original
        x_rot = coords_rot[0].reshape(x_array.shape)
        y_rot = coords_rot[1].reshape(x_array.shape)
        z_rot = coords_rot[2].reshape(x_array.shape)
        return x_rot, y_rot, z_rot

    
    # ==================== RESET SLIDERS ====================
    def reset_sliders():
        # reset defaults
        lattice_a.set(5.0)
        lattice_b.set(5.0)
        lattice_c.set(5.0)
        lattice_alpha.set(90.0)
        lattice_beta.set(90.0)
        lattice_gamma.set(90.0)
        unit_cells_x.set(5)
        unit_cells_y.set(5)
        unit_cells_z.set(5)
        crystal_system.set("isometric")
        refresh_plot()

    # ==================== UNIFY / SWAP ELEMENTS ====================
    def unify_elements():
        """Makes element_2 identical to element_1 (including color)."""
        e1 = selected_element_1.get()
        c1 = element_color_1.get()
        selected_element_2.set(e1)
        element_color_2.set(c1)
        refresh_plot()

    def swap_elements():
        """Swap element_1 <-> element_2, including color."""
        e1, e2 = selected_element_1.get(), selected_element_2.get()
        c1, c2 = element_color_1.get(), element_color_2.get()
        selected_element_1.set(e2)
        selected_element_2.set(e1)
        element_color_1.set(c2)
        element_color_2.set(c1)
        refresh_plot()

    # ==================== MAIN LATTICE GENERATOR ====================
    def generate_and_plot(lattice_type):
        """Generates & plots the lattice with the current UI state."""
        current_lattice_type.set(lattice_type)  # store the latest user-chosen type

        # gather all slider values
        a, b, c = lattice_a.get(), lattice_b.get(), lattice_c.get()
        alpha, beta, gamma = lattice_alpha.get(), lattice_beta.get(), lattice_gamma.get()
        nx, ny, nz = unit_cells_x.get(), unit_cells_y.get(), unit_cells_z.get()

        # gather element selections & colors
        e1 = selected_element_1.get()
        e2 = selected_element_2.get()
        col1 = element_color_1.get() or ELEMENT_DATA[e1]["color"]
        col2 = element_color_2.get() or ELEMENT_DATA[e2]["color"]
        same_element = (e1 == e2)
        rad1 = ELEMENT_DATA[e1]["radius"] * 80
        rad2 = ELEMENT_DATA[e2]["radius"] * 80

        # define lattice function table
        lattice_funcs = {
            "2d_sc": generate_2d_simple_cubic,
            "2d_tri": generate_2d_triangular,
            "2d_hex": generate_2d_hexagonal,
            "3d_sc": generate_3d_simple_cubic,
            "3d_bcc": generate_bcc,
            "3d_fcc": generate_fcc,
            "3d_hex": generate_3d_hexagonal,
        }

        # ==================== LATTICE TYPE GENERATORS ====================
        # 2D Lattices
        if lattice_type in ["2d_sc", "2d_tri", "2d_hex"]:
            x_total, y_total = lattice_funcs[lattice_type](nx, ny, a, b)

            # If alpha != 90, you might want to treat alpha as the 2D rotation angle
            # (Ignoring beta, gamma for 2D)
            # e.g.:
            x_total, y_total = rotate_2d(x_total, y_total, alpha)

            if same_element:
                # single array => same color
                x_list = [x_total]
                y_list = [y_total]
                colors = [col1]
                sizes = [rad1]
                elements = [e1]
            else:
                # offset second array
                x_shifted = x_total + a * 0.3
                y_shifted = y_total
                # Optionally rotate the offset array again or not
                # e.g., x_shifted, y_shifted = rotate_2d(x_shifted, y_shifted, alpha) if you want
                x_list = [x_total, x_shifted]
                y_list = [y_total, y_shifted]
                colors = [col1, col2]
                sizes = [rad1, rad2]
                elements = [e1, e2]

            plot_2d_lattice(
                x_list, y_list, a, b,
                title=f"{lattice_type.upper()} Lattice (nx={nx}, ny={ny}, alpha={alpha:.1f})",
                colors=colors,
                marker_sizes=sizes,
                elements=elements
            )

        elif lattice_type == "3d_sc":
            x_sc, y_sc, z_sc = lattice_funcs[lattice_type](nx, ny, nz, a, b, c)
            # Apply 3D rotation with alpha,beta,gamma
            x_sc, y_sc, z_sc = rotate_3d(x_sc, y_sc, z_sc, alpha, beta, gamma)

            if same_element:
                x_list = [x_sc]
                y_list = [y_sc]
                z_list = [z_sc]
                colors = [col1]
                sizes = [rad1]
                elements = [e1]
            else:
                x_shifted = x_sc
                y_shifted = y_sc
                z_shifted = z_sc + c * 0.25
                # Optionally rotate the second set again or keep the same rotation
                # x_shifted, y_shifted, z_shifted = rotate_3d(x_shifted, y_shifted, z_shifted, alpha, beta, gamma)
                x_list = [x_sc, x_shifted]
                y_list = [y_sc, y_shifted]
                z_list = [z_sc, z_shifted]
                colors = [col1, col2]
                sizes = [rad1, rad2]
                elements = [e1, e2]

            plot_3d_lattice(
                x_list, y_list, z_list,
                a, b, c,
                title=f"3D SC Lattice (nx={nx}, ny={ny}, nz={nz}, α={alpha:.1f}, β={beta:.1f}, γ={gamma:.1f})",
                colors=colors,
                marker_sizes=sizes,
                elements=elements
            )

        elif lattice_type == "3d_hex":
            x_hex, y_hex, z_hex = lattice_funcs[lattice_type](nx, ny, nz, a, b, c)
            # apply 3d rotation
            x_hex, y_hex, z_hex = rotate_3d(x_hex, y_hex, z_hex, alpha, beta, gamma)

            if same_element:
                x_list = [x_hex]
                y_list = [y_hex]
                z_list = [z_hex]
                colors = [col1]
                sizes = [rad1]
                elements = [e1]
            else:
                x_shifted = x_hex
                y_shifted = y_hex
                z_shifted = z_hex + c*0.25
                x_list = [x_hex, x_shifted]
                y_list = [y_hex, y_shifted]
                z_list = [z_hex, z_shifted]
                colors = [col1, col2]
                sizes = [rad1, rad2]
                elements = [e1, e2]

            plot_3d_lattice(
                x_list, y_list, z_list,
                a, b, c,
                title=f"3D HEX Lattice (nx={nx}, ny={ny}, nz={nz}, α={alpha:.1f}, β={beta:.1f}, γ={gamma:.1f})",
                colors=colors, marker_sizes=sizes, elements=elements
            )

        elif lattice_type == "3d_bcc":
            (x_c, y_c, z_c), (x_b, y_b, z_b) = lattice_funcs[lattice_type](nx, ny, nz, a, b, c)
            # corners
            x_c, y_c, z_c = rotate_3d(x_c, y_c, z_c, alpha, beta, gamma)
            # center
            x_b, y_b, z_b = rotate_3d(x_b, y_b, z_b, alpha, beta, gamma)

            x_list = [x_c, x_b]
            y_list = [y_c, y_b]
            z_list = [z_c, z_b]

            if same_element:
                colors = [col1, col1]
                sizes = [rad1, rad1]
                elements = [e1, e1]
            else:
                colors = [col1, col2]
                sizes = [rad1, rad2]
                elements = [e1, e2]

            plot_3d_lattice(
                x_list, y_list, z_list,
                a, b, c,
                title=f"3D BCC Lattice (nx={nx}, ny={ny}, nz={nz}, α={alpha:.1f}, β={beta:.1f}, γ={gamma:.1f})",
                colors=colors, marker_sizes=sizes, elements=elements
            )

        elif lattice_type == "3d_fcc":
            (x_c, y_c, z_c), offsets = lattice_funcs[lattice_type](nx, ny, nz, a, b, c)

            # corners rotated
            x_c, y_c, z_c = rotate_3d(x_c, y_c, z_c, alpha, beta, gamma)

            offset_x = []
            offset_y = []
            offset_z = []
            for (ox, oy, oz) in offsets:
                # rotate each face array
                ox_rot, oy_rot, oz_rot = rotate_3d(ox, oy, oz, alpha, beta, gamma)
                offset_x.append(ox_rot.ravel())
                offset_y.append(oy_rot.ravel())
                offset_z.append(oz_rot.ravel())

            x_faces = np.concatenate(offset_x)
            y_faces = np.concatenate(offset_y)
            z_faces = np.concatenate(offset_z)

            x_list = [x_c, x_faces]
            y_list = [y_c, y_faces]
            z_list = [z_c, z_faces]

            if same_element:
                colors = [col1, col1]
                sizes = [rad1, rad1]
                elements = [e1, e1]
            else:
                colors = [col1, col2]
                sizes = [rad1, rad2]
                elements = [e1, e2]

            plot_3d_lattice(
                x_list, y_list, z_list,
                a, b, c,
                title=f"3D FCC Lattice (nx={nx}, ny={ny}, nz={nz}, α={alpha:.1f}, β={beta:.1f}, γ={gamma:.1f})",
                colors=colors, marker_sizes=sizes, elements=elements
            )


    # ==================== UI LAYOUT ====================

    # Element Selection
    frame_selection = ttk.LabelFrame(root, text="Element Selection", padding=10)
    frame_selection.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    ttk.Label(frame_selection, text="Element 1:").grid(row=0, column=0, padx=5, pady=5)
    combo_1 = ttk.Combobox(frame_selection, textvariable=selected_element_1,
                           values=list(ELEMENT_DATA.keys()), width=12)
    combo_1.grid(row=0, column=1, padx=5, pady=5)
    # trace changes in element_1 => refresh plot
    selected_element_1.trace_add("write", refresh_plot)

    color_btn_1 = ttk.Button(frame_selection, text="Pick Color",
                             command=lambda: choose_color(element_color_1))
    color_btn_1.grid(row=0, column=2, padx=5, pady=5)

    ttk.Label(frame_selection, text="Element 2:").grid(row=1, column=0, padx=5, pady=5)
    combo_2 = ttk.Combobox(frame_selection, textvariable=selected_element_2,
                           values=list(ELEMENT_DATA.keys()), width=12)
    combo_2.grid(row=1, column=1, padx=5, pady=5)
    selected_element_2.trace_add("write", refresh_plot)

    color_btn_2 = ttk.Button(frame_selection, text="Pick Color",
                             command=lambda: choose_color(element_color_2))
    color_btn_2.grid(row=1, column=2, padx=5, pady=5)

    # unify & swap
    unify_btn = ttk.Button(frame_selection, text="Unify Elements", command=unify_elements)
    unify_btn.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
    swap_btn = ttk.Button(frame_selection, text="Swap Elements", command=swap_elements)
    swap_btn.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

    # Lattice Constants + Angles
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
            # re-plot on slider movement
            refresh_plot()

        var.trace_add("write", update_label)
        return slider

    add_slider(frame_constants, "a (Å):", lattice_a, 0, 1.0, 10.0)
    add_slider(frame_constants, "b (Å):", lattice_b, 1, 1.0, 10.0)
    add_slider(frame_constants, "c (Å):", lattice_c, 2, 1.0, 10.0)
    add_slider(frame_constants, "α (°):", lattice_alpha, 3, 30.0, 150.0)
    add_slider(frame_constants, "β (°):", lattice_beta, 4, 30.0, 150.0)
    add_slider(frame_constants, "γ (°):", lattice_gamma, 5, 30.0, 150.0)

    reset_button = ttk.Button(frame_constants, text="Reset All", command=reset_sliders)
    reset_button.grid(row=6, column=0, columnspan=3, pady=5)

    # Unit Cell Counts
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
            refresh_plot()

        var.trace_add("write", update_label)
        return slider

    add_int_slider(frame_cells, "nx:", unit_cells_x, 0, 1, 10)
    add_int_slider(frame_cells, "ny:", unit_cells_y, 1, 1, 10)
    add_int_slider(frame_cells, "nz:", unit_cells_z, 2, 1, 10)

    # Crystal System
    frame_crystal = ttk.LabelFrame(root, text="Crystal System", padding=10)
    frame_crystal.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    ttk.Label(frame_crystal, text="System:").grid(row=0, column=0, padx=5, pady=5)
    combo_crystal = ttk.Combobox(
        frame_crystal,
        textvariable=crystal_system,
        values=["isometric", "orthorhombic", "tetragonal", "hexagonal", "monoclinic", "triclinic"],
        width=14
    )
    combo_crystal.grid(row=0, column=1, padx=5, pady=5)
    # changes => apply_crystal_system => refresh_plot

    # Generate Lattice Buttons
    frame_lattices = ttk.LabelFrame(root, text="Generate Lattice", padding=10)
    frame_lattices.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def on_lattice_button_click(latt_type):
        """User clicked on a lattice type button -> re-plot with that type."""
        generate_and_plot(latt_type)

    # The main function that actually does lattice generation & calls the plots
    def generate_and_plot(lattice_type):
        current_lattice_type.set(lattice_type)

        a, b, c = lattice_a.get(), lattice_b.get(), lattice_c.get()
        alpha, beta, gamma = lattice_alpha.get(), lattice_beta.get(), lattice_gamma.get()
        nx, ny, nz = unit_cells_x.get(), unit_cells_y.get(), unit_cells_z.get()

        e1 = selected_element_1.get()
        e2 = selected_element_2.get()
        col1 = element_color_1.get() or ELEMENT_DATA[e1]["color"]
        col2 = element_color_2.get() or ELEMENT_DATA[e2]["color"]
        same_element = (e1 == e2)

        rad1 = ELEMENT_DATA[e1]["radius"] * 80
        rad2 = ELEMENT_DATA[e2]["radius"] * 80

        lattice_funcs = {
            "2d_sc": generate_2d_simple_cubic,
            "2d_tri": generate_2d_triangular,
            "2d_hex": generate_2d_hexagonal,
            "3d_sc": generate_3d_simple_cubic,
            "3d_bcc": generate_bcc,
            "3d_fcc": generate_fcc,
            "3d_hex": generate_3d_hexagonal,
        }

        # 2D Lattices
        if lattice_type in ["2d_sc", "2d_tri", "2d_hex"]:
            x_total, y_total = lattice_funcs[lattice_type](nx, ny, a, b)

            if same_element:
                # single array => same color
                x_list = [x_total]
                y_list = [y_total]
                colors = [col1]
                sizes = [rad1]
                elements = [e1]
            else:
                # offset second array
                x_shifted = x_total + a * 0.3
                y_shifted = y_total
                x_list = [x_total, x_shifted]
                y_list = [y_total, y_shifted]
                colors = [col1, col2]
                sizes = [rad1, rad2]
                elements = [e1, e2]

            plot_2d_lattice(
                x_list, y_list, a, b,
                title=f"{lattice_type.upper()} Lattice (nx={nx}, ny={ny})",
                colors=colors,
                marker_sizes=sizes,
                elements=elements
            )

        elif lattice_type == "3d_sc":
            x_sc, y_sc, z_sc = lattice_funcs[lattice_type](nx, ny, nz, a, b, c)
            if same_element:
                # single array => purely single element
                x_list = [x_sc]
                y_list = [y_sc]
                z_list = [z_sc]
                colors = [col1]
                sizes = [rad1]
                elements = [e1]
            else:
                # replicate if user wants 2 elements, offset second
                x_shifted = x_sc
                y_shifted = y_sc
                z_shifted = z_sc + c * 0.25
                x_list = [x_sc, x_shifted]
                y_list = [y_sc, y_shifted]
                z_list = [z_sc, z_shifted]
                colors = [col1, col2]
                sizes = [rad1, rad2]
                elements = [e1, e2]

            plot_3d_lattice(
                x_list, y_list, z_list,
                a, b, c,
                title=f"3D SC Lattice (nx={nx}, ny={ny}, nz={nz})",
                colors=colors,
                marker_sizes=sizes,
                elements=elements
            )

        elif lattice_type == "3d_hex":
            x_hex, y_hex, z_hex = lattice_funcs[lattice_type](nx, ny, nz, a, b, c)
            if same_element:
                # single array => purely single element
                x_list = [x_hex]
                y_list = [y_hex]
                z_list = [z_hex]
                colors = [col1]
                sizes = [rad1]
                elements = [e1]
            else:
                # offset second array
                x_shifted = x_hex
                y_shifted = y_hex
                z_shifted = z_hex + c*0.25
                x_list = [x_hex, x_shifted]
                y_list = [y_hex, y_shifted]
                z_list = [z_hex, z_shifted]
                colors = [col1, col2]
                sizes = [rad1, rad2]
                elements = [e1, e2]

            plot_3d_lattice(
                x_list, y_list, z_list,
                a, b, c,
                title=f"3D HEX Lattice (nx={nx}, ny={ny}, nz={nz})",
                colors=colors, marker_sizes=sizes, elements=elements
            )

        elif lattice_type == "3d_bcc":
            (x_c, y_c, z_c), (x_b, y_b, z_b) = lattice_funcs[lattice_type](nx, ny, nz, a, b, c)
            # always produce corners + center
            x_list = [x_c, x_b]
            y_list = [y_c, y_b]
            z_list = [z_c, z_b]

            if same_element:
                colors = [col1, col1]
                sizes = [rad1, rad1]
                elements = [e1, e1]
            else:
                colors = [col1, col2]
                sizes = [rad1, rad2]
                elements = [e1, e2]

            plot_3d_lattice(
                x_list, y_list, z_list,
                a, b, c,
                title=f"3D BCC Lattice (nx={nx}, ny={ny}, nz={nz})",
                colors=colors, marker_sizes=sizes, elements=elements
            )

        elif lattice_type == "3d_fcc":
            (x_c, y_c, z_c), offsets = lattice_funcs[lattice_type](nx, ny, nz, a, b, c)
            # unify face offsets
            offset_x = []
            offset_y = []
            offset_z = []
            for (ox, oy, oz) in offsets:
                offset_x.append(ox.ravel())
                offset_y.append(oy.ravel())
                offset_z.append(oz.ravel())
            x_faces = np.concatenate(offset_x)
            y_faces = np.concatenate(offset_y)
            z_faces = np.concatenate(offset_z)

            x_list = [x_c, x_faces]
            y_list = [y_c, y_faces]
            z_list = [z_c, z_faces]

            if same_element:
                colors = [col1, col1]
                sizes = [rad1, rad1]
                elements = [e1, e1]
            else:
                colors = [col1, col2]
                sizes = [rad1, rad2]
                elements = [e1, e2]

            plot_3d_lattice(
                x_list, y_list, z_list,
                a, b, c,
                title=f"3D FCC Lattice (nx={nx}, ny={ny}, nz={nz})",
                colors=colors, marker_sizes=sizes, elements=elements
            )

    # The lattice type buttons
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
            command=lambda latt=lt: on_lattice_button_click(latt),
            width=20
        ).grid(row=row, column=col, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
