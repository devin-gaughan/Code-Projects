import tkinter as tk
from tkinter import ttk, colorchooser
import numpy as np
from elements import ELEMENT_DATA
from lattice import (
    generate_2d_simple_cubic, generate_2d_triangular, generate_2d_hexagonal,
    generate_3d_simple_cubic, generate_bcc, generate_fcc, generate_3d_hexagonal
)
from visualization import plot_2d_lattice, plot_3d_lattice
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def main():
    root = tk.Tk()
    root.title("Auraeon - Crystal Lattice Simulator v0.3.7")
    root.geometry("1200x900")

    # ==================== TRACK CURRENT LATTICE TYPE ====================
    current_lattice_type = tk.StringVar(value="3d_bcc")

    # ==================== CRYSTAL SYSTEM SELECTION ====================
    crystal_system = tk.StringVar(value="isometric")

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

    # ==================== BOND LENGTH THRESHOLD ====================
    bond_length_threshold = tk.DoubleVar(value=2.0)

   # ==================== SELECTED ATOM FOR HIGHLIGHTING ====================
    selected_atom_index = tk.IntVar(value=-1)  # Initially no atom is selected
    highlight_artist = None # stores the highlight object
    x_coords_global = None
    y_coords_global = None
    z_coords_global = None

    # ==================== INITIALIZE MATPLOTLIB FIGURE AND AXES ====================
    fig, ax = plt.subplots(figsize=(8, 6), subplot_kw={'projection': '3d'})
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()

    # ==================== UI ELEMENTS ====================
    frame = ttk.Frame(root, padding="10 10 10 10")

    # --------- Layout using grid ---------
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    canvas_widget.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
    root.columnconfigure(1, weight=1)  # plot expands
    root.rowconfigure(0, weight=1)

    # ==================== HELPER: RE-PLOT WHENEVER ANYTHING CHANGES ====================
    def refresh_plot(*args):
        """Re-call generate_and_plot() with the currently selected lattice type."""
        lt = current_lattice_type.get()
        if lt:
            generate_and_plot(lt, ax)

    # ==================== CHOOSE COLOR ====================
    def choose_color(color_var):
        """Opens a color picker dialog and updates the selected color, then re-plots."""
        chosen = colorchooser.askcolor(title="Pick an Atom Color")
        if chosen and chosen[1]:
            color_var.set(chosen[1])
            refresh_plot()

    # ==================== CRYSTAL SYSTEM HANDLER ====================
    def apply_crystal_system(*_):
        system = crystal_system.get()
        if system == "isometric":
            lattice_b.set(lattice_a.get())
            lattice_c.set(lattice_a.get())
            lattice_alpha.set(90.0)
            lattice_beta.set(90.0)
            lattice_gamma.set(90.0)
        elif system == "orthorhombic":
            lattice_alpha.set(90.0)
            lattice_beta.set(90.0)
            lattice_gamma.set(90.0)
        elif system == "tetragonal":
            lattice_b.set(lattice_a.get())
            lattice_alpha.set(90.0)
            lattice_beta.set(90.0)
            lattice_gamma.set(90.0)
        elif system == "hexagonal":
            lattice_b.set(lattice_a.get())
            lattice_alpha.set(90.0)
            lattice_beta.set(90.0)
            lattice_gamma.set(120.0)
        refresh_plot()

    def rotate_2d(x_array, y_array, alpha_degs):
        alpha = np.radians(alpha_degs)
        x_flat = x_array.ravel()
        y_flat = y_array.ravel()
        cos_a = np.cos(alpha)
        sin_a = np.sin(alpha)
        x_rot = x_flat * cos_a - y_flat * sin_a
        y_rot = x_flat * sin_a + y_flat * cos_a
        shape_2d = x_array.shape
        return x_rot.reshape(shape_2d), y_rot.reshape(shape_2d)

    def rotate_3d(x_array, y_array, z_array, alpha_degs, beta_degs, gamma_degs):
        alpha = np.radians(alpha_degs)
        beta = np.radians(beta_degs)
        gamma = np.radians(gamma_degs)
        x_flat = x_array.ravel()
        y_flat = y_array.ravel()
        z_flat = z_array.ravel()
        coords = np.vstack((x_flat, y_flat, z_flat))
        Rx = np.array([[1, 0, 0], [0, np.cos(alpha), -np.sin(alpha)], [0, np.sin(alpha), np.cos(alpha)]])
        Ry = np.array([[np.cos(beta), 0, np.sin(beta)], [0, 1, 0], [-np.sin(beta), 0, np.cos(beta)]])
        Rz = np.array([[np.cos(gamma), -np.sin(gamma), 0], [np.sin(gamma), np.cos(gamma), 0], [0, 0, 1]])
        R = Rz @ Ry @ Rx
        coords_rot = R @ coords
        x_rot = coords_rot[0].reshape(x_array.shape)
        y_rot = coords_rot[1].reshape(y_array.shape)
        z_rot = coords_rot[2].reshape(z_array.shape)
        return x_rot, y_rot, z_rot

    def reset_sliders():
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

    def unify_elements():
        e1 = selected_element_1.get()
        c1 = element_color_1.get()
        selected_element_2.set(e1)
        element_color_2.set(c1)
        refresh_plot()

    def swap_elements():
        e1, e2 = selected_element_1.get(), selected_element_2.get()
        c1, c2 = element_color_1.get(), element_color_2.get()
        selected_element_1.set(e2)
        selected_element_2.set(e1)
        element_color_1.set(c2)
        element_color_2.set(c1)
        refresh_plot()

    def on_atom_click(event):
        """Handles atom click events to highlight nearest atom."""
        if event.xdata is None or event.ydata is None:
            return # click was outside the plot

        x, y = event.xdata, event.ydata # coords of the click

        # Find the index of the atom nearest to the click
        min_distance = float('inf')
        nearest_atom = -1

        # Get current atom positions
        global x_coords_global, y_coords_global, z_coords_global
        if x_coords_global is not None and len(x_coords_global) > 0:
            # Iterate through atoms & compute distances
            num_atoms = len(x_coords_global)
            for i in range(num_atoms):
                distance = np.sqrt((x_coords_global[i] - x)**2 + (y_coords_global[i] - y)**2 + (z_coords_global[i] - 0)**2) # simple 2D distance
                if distance < min_distance: # If closer...
                    min_distance = distance  # Store the new minimum distance
                    nearest_atom = i # Store the index of the closest atom
        # Set selected atom
        selected_atom_index.set(nearest_atom)
        # Update plot
        refresh_plot() # redraw with new highlighting

    def generate_and_plot(lattice_type, ax):
        """Generates & plots the lattice with the current UI state."""
        # Set title before generating
        title = f"{lattice_type.upper()} Lattice"

        # Clear the axes before plotting new data
        ax.clear()
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
        bond_threshold = bond_length_threshold.get()
        selected_atom = selected_atom_index.get()

        lattice_funcs = {
            "2d_sc": generate_2d_simple_cubic,
            "2d_tri": generate_2d_triangular,
            "2d_hex": generate_2d_hexagonal,
            "3d_sc": generate_3d_simple_cubic,
            "3d_bcc": generate_bcc,
            "3d_fcc": generate_fcc,
            "3d_hex": generate_3d_hexagonal
        }

        if lattice_type in ["2d_sc", "2d_tri", "2d_hex"]:
            x_total, y_total = lattice_funcs[lattice_type](nx, ny, a, b)
            x_total, y_total = rotate_2d(x_total, y_total, alpha)
            if same_element:
                x_list = [x_total]
                y_list = [y_total]
                colors = [col1]
                sizes = [rad1]
                elements = [e1]
            else:
                x_shifted = x_total + a * 0.3
                y_shifted = y_total
                x_list = [x_total, x_shifted]
                y_list = [y_total, y_shifted]
                colors = [col1, col2]
                sizes = [rad1, rad2]
                elements = [e1, e2]
            plot_2d_lattice(
                ax, x_list, y_list, a, b,
                title=f"{lattice_type.upper()} Lattice (nx={nx}, ny={ny}, alpha={alpha:.1f})",
                colors=colors,
                marker_sizes=sizes,
                elements=elements,
                bond_threshold=bond_threshold
            )
            #clear the variables, preventing bugs
            x_coords_global = None
            y_coords_global = None
            z_coords_global = None
        elif lattice_type == "3d_sc":
            x_sc, y_sc, z_sc = lattice_funcs[lattice_type](nx, ny, nz, a, b, c)
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
                x_list = [x_sc, x_shifted]
                y_list = [y_sc, y_shifted]
                z_list = [z_sc, z_shifted]
                colors = [col1, col2]
                sizes = [rad1, rad2]
                elements = [e1, e2]
            plot_3d_lattice(
                ax, x_list, y_list, z_list,
                a, b, c,
                title=f"3D SC Lattice (nx={nx}, ny={ny}, nz={nz}, α={alpha:.1f}, β={beta:.1f}, γ={gamma:.1f})",
                colors=colors,
                marker_sizes=sizes,
                elements=elements,
                bond_threshold=bond_threshold
            )

            #clear the variables, preventing bugs
            x_coords_global = None
            y_coords_global = None
            z_coords_global = None

        elif lattice_type == "3d_hex":
            x_hex, y_hex, z_hex = lattice_funcs[lattice_type](nx, ny, nz, a, b, c)
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
                z_shifted = z_hex + c * 0.25
                x_list = [x_hex, x_shifted]
                y_list = [y_hex, y_shifted]
                z_list = [z_hex, z_shifted]
                colors = [col1, col2]
                sizes = [rad1, rad2]
                elements = [e1, e2]
            plot_3d_lattice(
                ax, x_list, y_list, z_list,
                a, b, c,
                title=f"3D HEX Lattice (nx={nx}, ny={ny}, nz={nz}, α={alpha:.1f}, β={beta:.1f}, γ={gamma:.1f})",
                colors=colors,
                marker_sizes=sizes,
                elements=elements,
                bond_threshold=bond_threshold
            )
            #clear the variables, preventing bugs
            x_coords_global = None
            y_coords_global = None
            z_coords_global = None

        elif lattice_type == "3d_bcc":
            (x_c, y_c, z_c), (x_b, y_b, z_b) = lattice_funcs[lattice_type](nx, ny, nz, a, b, c)
            x_c, y_c, z_c = rotate_3d(x_c, y_c, z_c, alpha, beta, gamma)
            x_b, y_b, z_b = rotate_3d(x_b, y_b, z_b, alpha, beta, gamma)

            if same_element:
                x_list = [x_c, x_b]
                y_list = [y_c, y_b]
                z_list = [z_c, z_b]
                colors = [col1, col1]  # Same color for both
                sizes = [rad1, rad1]
                elements = [e1, e1]
            else:
                x_list = [x_c, x_b]
                y_list = [y_c, y_b]
                z_list = [z_c, z_b]
                colors = [col1, col2]
                sizes = [rad1, rad2]
                elements = [e1, e2]
            plot_3d_lattice(
                ax, x_list, y_list, z_list,
                a, b, c,
                title=f"3D BCC Lattice (nx={nx}, ny={ny}, nz={nz}, α={alpha:.1f}, β={beta:.1f}, γ={gamma:.1f})",
                colors=colors,
                marker_sizes=sizes,
                elements=elements,
                bond_threshold=bond_threshold
            )

            # Store the coordinates for highlighting
            x_coords_global = np.concatenate([x_c.ravel(), x_b.ravel()])
            y_coords_global = np.concatenate([y_c.ravel(), y_b.ravel()])
            z_coords_global = np.concatenate([z_c.ravel(), z_b.ravel()])

        elif lattice_type == "3d_fcc":
            (x_c, y_c, z_c), (x_f1, y_f1, z_f1), (x_f2, y_f2, z_f2), (x_f3, y_f3, z_f3) = lattice_funcs[lattice_type](nx, ny, nz, a, b, c)
            x_c, y_c, z_c = rotate_3d(x_c, y_c, z_c, alpha, beta, gamma)
            x_f1, y_f1, z_f1 = rotate_3d(x_f1, y_f1, z_f1, alpha, beta, gamma)
            x_f2, y_f2, z_f2 = rotate_3d(x_f2, y_f2, z_f2, alpha, beta, gamma)
            x_f3, y_f3, z_f3 = rotate_3d(x_f3, y_f3, z_f3, alpha, beta, gamma)

            if same_element:
                x_list = [x_c, x_f1, x_f2, x_f3]
                y_list = [y_c, y_f1, y_f2, y_f3]
                z_list = [z_c, z_f1, z_f2, z_f3]
                colors = [col1, col1, col1, col1]
                sizes = [rad1, rad1, rad1, rad1]
                elements = [e1, e1, e1, e1]
            else:
                x_list = [x_c, x_f1, x_f2, x_f3]
                y_list = [y_c, y_f1, y_f2, y_f3]
                z_list = [z_c, z_f1, z_f2, z_f3]
                colors = [col1, col2, col2, col2]
                sizes = [rad1, rad2, rad2, rad2]
                elements = [e1, e2, e2, e2]
            plot_3d_lattice(
                ax, x_list, y_list, z_list,
                a, b, c,
                title=f"3D FCC Lattice (nx={nx}, ny={ny}, nz={nz}, α={alpha:.1f}, β={beta:.1f}, γ={gamma:.1f})",
                colors=colors,
                marker_sizes=sizes,
                elements=elements,
                bond_threshold=bond_threshold
            )

        # Store the coordinates for highlighting
            x_coords_global = np.concatenate([x_c.ravel(), x_f1.ravel(), x_f2.ravel(), x_f3.ravel()])
            y_coords_global = np.concatenate([y_c.ravel(), y_f1.ravel(), y_f2.ravel(), y_f3.ravel()])
            z_coords_global = np.concatenate([z_c.ravel(), z_f1.ravel(), z_f2.ravel(), z_f3.ravel()])

        #clear artist for highlighint to prevent bugs
            if highlight_artist:
                highlight_artist.remove()
                highlight_artist = None

        # Add highlighting for the nearest neighbor
            if selected_atom > -1: # is there an selected atom?
                try:
                    # Use offset from data
                    x_h, y_h, z_h = x_coords_global[selected_atom], y_coords_global[selected_atom], z_coords_global[selected_atom]

                    # Set radius and render
                    highlight_radius = 0.2
                    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
                    x_surf = highlight_radius * np.cos(u) * np.sin(v) + x_h
                    y_surf = highlight_radius * np.sin(u) * np.sin(v) + y_h
                    z_surf = highlight_radius * np.cos(v) + z_h
                    highlight_artist = ax.plot_surface(x_surf, y_surf, z_surf, color='yellow', alpha=0.5)
                except IndexError:
                    print("Error: Selected atom index out of range.")
                except AttributeError:
                    print("Error: No atom has been selected.")
                except ValueError:
                    print("Error: Value error")
            else:
                    x_coords_global = None
                    y_coords_global = None
                    z_coords_global = None
        # set title/labels and redraw canvas
        ax.set_title(title)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        canvas.draw()

    # ==================== UI ELEMENTS ====================
    frame = ttk.Frame(root, padding="10 10 10 10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # --------- Lattice Type Selection ---------
    ttk.Label(frame, text="Lattice Type:").grid(column=0, row=0, sticky=(tk.W, tk.E))
    lattice_type_combo = ttk.Combobox(frame, textvariable=current_lattice_type, values=["2d_sc", "2d_tri", "2d_hex", "3d_sc", "3d_bcc", "3d_fcc", "3d_hex"], state='readonly')
    lattice_type_combo.grid(column=1, row=0, sticky=(tk.W, tk.E))
    lattice_type_combo.bind("<<ComboboxSelected>>", lambda event: refresh_plot())

        # Register click event handler
    canvas.mpl_connect('button_press_event', on_atom_click)

    # --------- Crystal System Selection ---------
    ttk.Label(frame, text="Crystal System:").grid(column=0, row=1, sticky=(tk.W, tk.E))
    crystal_system_combo = ttk.Combobox(frame, textvariable=crystal_system, values=["isometric", "orthorhombic", "tetragonal", "hexagonal"], state='readonly')
    crystal_system_combo.grid(column=1, row=1, sticky=(tk.W, tk.E))
    crystal_system_combo.bind("<<ComboboxSelected>>", apply_crystal_system)

    # --------- Lattice Constants ---------
    ttk.Label(frame, text="Lattice Constant a:").grid(column=0, row=2, sticky=tk.W)
    a_slider = tk.Scale(frame, from_=0.1, to=10.0, resolution=0.1, orient=tk.HORIZONTAL, variable=lattice_a, command=lambda event: refresh_plot())
    a_slider.grid(column=1, row=2, sticky=(tk.W, tk.E))

    ttk.Label(frame, text="Lattice Constant b:").grid(column=0, row=3, sticky=tk.W)
    b_slider = tk.Scale(frame, from_=0.1, to=10.0, resolution=0.1, orient=tk.HORIZONTAL, variable=lattice_b, command=lambda event: refresh_plot())
    b_slider.grid(column=1, row=3, sticky=(tk.W, tk.E))

    ttk.Label(frame, text="Lattice Constant c:").grid(column=0, row=4, sticky=tk.W)
    c_slider = tk.Scale(frame, from_=0.1, to=10.0, resolution=0.1, orient=tk.HORIZONTAL, variable=lattice_c, command=lambda event: refresh_plot())
    c_slider.grid(column=1, row=4, sticky=(tk.W, tk.E))

    # --------- Lattice Angles ---------
    ttk.Label(frame, text="Lattice Angle α:").grid(column=0, row=5, sticky=tk.W)
    alpha_slider = tk.Scale(frame, from_=0.0, to=180.0, resolution=1.0, orient=tk.HORIZONTAL, variable=lattice_alpha, command=lambda event: refresh_plot())
    alpha_slider.grid(column=1, row=5, sticky=(tk.W, tk.E))

    ttk.Label(frame, text="Lattice Angle β:").grid(column=0, row=6, sticky=tk.W)
    beta_slider = tk.Scale(frame, from_=0.0, to=180.0, resolution=1.0, orient=tk.HORIZONTAL, variable=lattice_beta, command=lambda event: refresh_plot())
    beta_slider.grid(column=1, row=6, sticky=(tk.W, tk.E))

    ttk.Label(frame, text="Lattice Angle γ:").grid(column=0, row=7, sticky=tk.W)
    gamma_slider = tk.Scale(frame, from_=0.0, to=180.0, resolution=1.0, orient=tk.HORIZONTAL, variable=lattice_gamma, command=lambda event: refresh_plot())
    gamma_slider.grid(column=1, row=7, sticky=(tk.W, tk.E))

    # --------- Unit Cells ---------
    ttk.Label(frame, text="Unit Cells nx:").grid(column=0, row=8, sticky=tk.W)
    nx_slider = tk.Scale(frame, from_=1, to=10, resolution=1, orient=tk.HORIZONTAL, variable=unit_cells_x, command=lambda event: refresh_plot())
    nx_slider.grid(column=1, row=8, sticky=(tk.W, tk.E))

    ttk.Label(frame, text="Unit Cells ny:").grid(column=0, row=9, sticky=tk.W)
    ny_slider = tk.Scale(frame, from_=1, to=10, resolution=1, orient=tk.HORIZONTAL, variable=unit_cells_y, command=lambda event: refresh_plot())
    ny_slider.grid(column=1, row=9, sticky=(tk.W, tk.E))

    ttk.Label(frame, text="Unit Cells nz:").grid(column=0, row=10, sticky=tk.W)
    nz_slider = tk.Scale(frame, from_=1, to=10, resolution=1, orient=tk.HORIZONTAL, variable=unit_cells_z, command=lambda event: refresh_plot())
    nz_slider.grid(column=1, row=10, sticky=(tk.W, tk.E))

    # --------- Element 1 Selection ---------
    ttk.Label(frame, text="Element 1:").grid(column=0, row=11, sticky=(tk.W, tk.E))
    element1_combo = ttk.Combobox(frame, textvariable=selected_element_1, values=list(ELEMENT_DATA.keys()), state='readonly')
    element1_combo.grid(column=1, row=11, sticky=(tk.W, tk.E))
    element1_combo.bind("<<ComboboxSelected>>", lambda event: update_element1_color())

    def update_element1_color():
        element = selected_element_1.get()
        element_color_1.set(ELEMENT_DATA[element]["color"])
        refresh_plot()

    # --------- Element 1 Color ---------
    ttk.Label(frame, text="Element 1 Color:").grid(column=0, row=12, sticky=(tk.W, tk.E))
    element1_color_button = ttk.Button(frame, text="Choose Color", command=lambda: choose_color(element_color_1))
    element1_color_button.grid(column=1, row=12, sticky=(tk.W, tk.E))

    # --------- Element 2 Selection ---------
    ttk.Label(frame, text="Element 2:").grid(column=0, row=13, sticky=(tk.W, tk.E))
    element2_combo = ttk.Combobox(frame, textvariable=selected_element_2, values=list(ELEMENT_DATA.keys()), state='readonly')
    element2_combo.grid(column=1, row=13, sticky=(tk.W, tk.E))
    element2_combo.bind("<<ComboboxSelected>>", lambda event: update_element2_color())

    def update_element2_color():
        element = selected_element_2.get()
        element_color_2.set(ELEMENT_DATA[element]["color"])
        refresh_plot()

    # --------- Element 2 Color ---------
    ttk.Label(frame, text="Element 2 Color:").grid(column=0, row=14, sticky=(tk.W, tk.E))
    element2_color_button = ttk.Button(frame, text="Choose Color", command=lambda: choose_color(element_color_2))
    element2_color_button.grid(column=1, row=14, sticky=(tk.W, tk.E))

    # --------- Unify Elements ---------
    unify_button = ttk.Button(frame, text="Unify Elements", command=unify_elements)
    unify_button.grid(column=0, row=15, columnspan=2, sticky=(tk.W, tk.E))

    # --------- Swap Elements ---------
    swap_button = ttk.Button(frame, text="Swap Elements", command=swap_elements)
    swap_button.grid(column=0, row=16, columnspan=2, sticky=(tk.W, tk.E))

    # --------- Reset Sliders ---------
    reset_button = ttk.Button(frame, text="Reset All", command=reset_sliders)
    reset_button.grid(column=0, row=17, columnspan=2, sticky=(tk.W, tk.E))

     # ---------Bond Length slider---------
    ttk.Label(frame, text="Bond Length Threshold:").grid(column=0, row=18, sticky=tk.W)
    bond_length_slider = tk.Scale(frame, from_=0.1, to=5.0, resolution=0.1, orient=tk.HORIZONTAL, variable=bond_length_threshold, command=lambda event: refresh_plot())
    bond_length_slider.grid(column=1, row=18, sticky=(tk.W, tk.E))

    # ---------Canvas and Frame Weight ---------
    canvas.get_tk_widget().grid(row=0, column=1, sticky="nsew")
    # Register click event handler
    canvas.mpl_connect('button_press_event', on_atom_click)

    # ==================== INITIAL PLOT + UI ====================
    refresh_plot()
    root.mainloop()

if __name__ == "__main__":
    main()
