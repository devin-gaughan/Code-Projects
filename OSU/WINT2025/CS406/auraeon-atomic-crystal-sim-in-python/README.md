# Auraeon - Crystal Lattice Simulator v0.2.4

## Overview

The **Auraeon Crystal Lattice Simulator** is a Python-based program designed to generate and visualize 2D and 3D crystal lattices. With version **v0.2.4**, the simulator features a refined GUI, improved visualization, and full support for multi-element plotting, allowing users to:

- **Select Elements**: Choose from a dropdown of elements, each with unique colors, atomic radii, and other properties.
- **Pick Colors**: Use a color picker to customize the display color of the selected element.
- **Visualize Lattices**: Render 2D (Simple Cubic, Triangular, Hexagonal) and 3D (Simple Cubic, BCC, FCC) lattices in Matplotlib plots.
- **Improved UI**: Modernized button layouts and better spacing for usability.
- **Legends Outside the Plot**: Prevents overlap and ensures a clear view of lattice structures.

**GitHub Repository Location:**  
[https://github.com/devin-gaughan/Code-Projects/tree/master/OSU/WINT2025/CS406/auraeon-atomic-crystal-sim-in-python](https://github.com/devin-gaughan/Code-Projects/tree/master/OSU/WINT2025/CS406/auraeon-atomic-crystal-sim-in-python)

---

## Features

### Element Selection

- **Dropdown Menu**: Select an element (e.g., "Fe," "Cu") from the periodic table defined in `elements.py`.
- **Dynamic Properties**: Each element has:
  - **Color**: Default colors for visualization.
  - **Atomic Radius**: Determines marker size in plots.
  - **Mass**: For potential future property calculations.

### Color Picker

- Customize the color of any selected element using a Tkinter-based color chooser dialog.
- Updated colors are applied dynamically to subsequent lattice visualizations.

### Supported Lattice Types

- **2D Lattices**:
  - Simple Cubic
  - Triangular
  - Hexagonal
- **3D Lattices**:
  - Simple Cubic
  - Body-Centered Cubic (BCC)
  - Face-Centered Cubic (FCC)

### Improved Visualization

- **Legend Placement**: Legends now appear **outside the plot** to avoid overlap.
- **Dynamic Figure Scaling**: The GUI ensures that the plot window resizes to accommodate legends without distortion.
- **Single Window Behavior**: Closing a 2D or 3D plot allows new plots to open correctly without conflicts.

---

## Getting Started

### Prerequisites

- **Python 3.8+**
- **Pip** package manager

### Dependencies

- `numpy`
- `matplotlib`
- `tkinter` (usually included with Python installations)
- `pyvista` (for potential future 3D enhancements)

You can install dependencies with:

```bash
pip install -r requirements.txt
```

### Installation & Running

1. **Clone or Download** the repository:
   ```bash
   git clone https://github.com/devin-gaughan/Code-Projects.git
   ```
   Then navigate to:  
   `OSU/WINT2025/CS406/auraeon-atomic-crystal-sim-in-python`
2. **Navigate** into the project directory:
   ```bash
   cd auraeon-atomic-crystal-sim-in-python
   ```
3. **Run** the main script:
   ```bash
   python main.py
   ```
4. **Interact** with the GUI:
   - Select an element from the dropdown.
   - Click "Pick Color" to customize the selected element's color.
   - Click lattice type buttons to generate and visualize structures.

---

## Usage Example

When you click "3D BCC," for example, the program:

1. Generates a BCC lattice with corner and center atoms.
2. Applies the selected element’s color and radius to all atoms.
3. Displays the lattice in a 3D scatter plot with proper sizing and coloring.

---

## Project Status (v0.2.4)

### Completed in v0.2.4

- **Refined GUI Layout**: Buttons now align properly for a cleaner look.
- **Legend Fixes**: Legends are now placed outside the plots to avoid overlap.
- **Improved Multi-Element Support**: Corrected handling of multiple elements in BCC/FCC.

### What’s Next (v0.3.0)

- **Sliders for Grid Size & Lattice Constant**: Users will be able to adjust lattice parameters dynamically.
- **Embedded Matplotlib for a Unified UI**: Instead of separate windows, plots will be embedded in the main application.
- **Optimized Rendering for Larger Lattices**: Improving performance for larger lattice structures.

---

## Contributing

This project is in a learning/demo phase. Contributions or suggestions are welcome, but features like support for molecules (in addition to individual atoms), advanced atomic and molecular property calculations, and calculations for electron conductivity and magnetic properties are already planned for future versions.

---

## License

Feel free to use the code for educational or personal projects. Not for commercial use.

---

## Contact

For questions or feedback:

- **Name**: Devin Patrick Gaughan
- **GitHub**: [devin-gaughan](https://github.com/devin-gaughan)
- **Email**: devin@devingaughan.com
