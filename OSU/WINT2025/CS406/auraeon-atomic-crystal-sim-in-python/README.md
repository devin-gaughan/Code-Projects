# Auraeon - Crystal Lattice Simulator v0.2.1

## Overview

The **Auraeon Crystal Lattice Simulator** is a Python-based program designed to generate and visualize 2D and 3D crystal lattices. With version **v0.2.1**, the simulator introduces enhanced features for element selection and customization, allowing users to:

- **Select Elements**: Choose from a dropdown of elements, each with unique colors, atomic radii, and other properties.
- **Pick Colors**: Use a color picker to customize the display color of the selected element.
- **Visualize Lattices**: Render 2D (Simple Cubic, Triangular, Hexagonal) and 3D (Simple Cubic, BCC, FCC) lattices in separate Matplotlib windows.

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

---

## Getting Started

### Prerequisites

- **Python 3.8+**
- **Pip** package manager

### Dependencies

- `numpy`
- `matplotlib`
- `tkinter` (usually included with Python installations)

You can install dependencies with:

```bash
pip install numpy matplotlib
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

## Project Status (v0.2.1)

### Completed in v0.2.1

- Added an element selection dropdown.
- Introduced a color picker for element customization.
- Updated the visualization pipeline to handle dynamic colors and marker sizes.

### What’s Next (v0.2.2)

- **Legend Support**: Add legends to plots showing selected elements and their colors.
- **Multi-Element Support**: Enable users to assign different elements to sub-lattices (e.g., corner vs. center atoms in BCC).
- **Save/Restore Colors**: Implement saving of custom colors to a JSON file for persistence between sessions.
- **Embedded Matplotlib**: Start transitioning to embedded Matplotlib plots for a unified UI.

---

## Contributing

This project is in a learning/demo phase. Contributions or suggestions are welcome, but features like multi-element lattices, embedded plots, and advanced property calculations are already planned for future versions.

---

## License

Feel free to use the code for educational or personal projects. Not for commercial use.

---

## Contact

For questions or feedback:

- **Name**: Devin Patrick Gaughan
- **GitHub**: [devin-gaughan](https://github.com/devin-gaughan)
- **Email**: devin@devingaughan.com
