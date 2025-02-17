# Auraeon - Crystal Lattice Simulator v0.3.3

## Overview

The **Auraeon Crystal Lattice Simulator** is a Python-based program designed to generate and visualize 2D and 3D crystal lattices. Version **v0.3.3** continues our progress by refining the multi-element support, UI enhancements, and structural rendering. However, two known issues have appeared in this release:

1. **Overlapping Atoms** in 2D plots and 3D Hex plots.
2. **Broken Dynamic Plot Updates** when slider values change—plots do not always refresh automatically.

These bugs will be addressed in a future fix.

## Features in v0.3.3

### Lattice Constants & Angular Rotations

- **Sliders:** Modify `(a, b, c, α, β, γ)` via a user-friendly GUI.
- **Partially Real-Time Updates:** Sliders are present, but dynamic updates are temporarily broken.
- **Angular Control:** Simulate rotations in 3D to reflect `α, β, γ` angles (once dynamic refresh is fixed).

### Unit Cell Customization

- **`nx, ny, nz`** sliders control the number of unit cells.
- **2D & 3D** patterns available: SC, BCC, FCC, Hex.
- **Multi-Element**: Users can display up to two different elements.

### Color Picker & Element Selection

- **Drop-down** to choose element_1 and element_2 from a built-in table.
- **Color pickers** for both element_1 and element_2, giving users freedom to style atoms.

### 2D & 3D Visualization

- **Matplotlib** used for plotting.
- **No blank windows**—only one figure for 2D and one for 3D.
- **Auto-scaling** aims to fill the view but can cause overlapping in some lattice types.

## Known Bugs

- **Overlapping Atoms** in certain 2D plots and the 3D Hex plot.
- **Slider-Driven Updates** for plots are currently broken and do not consistently refresh.
- **Legend text** outside of plot grid caused a fatal UI bug. Move the legend back into the plot window to fix for now.
- **Gridlines for 2D Plots** are currently missing.

## Installation & Running

1. **Clone or Download** this repository:
   ```bash
   git clone https://github.com/devin-gaughan/Code-Projects.git
   ```
2. **Navigate** into the project directory:
   ```bash
   cd auraeon-atomic-crystal-sim-in-python
   ```
3. **Install** the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run** the main script:
   ```bash
   python main.py
   ```
5. **Interact** with the GUI:
   - Adjust **(a, b, c, α, β, γ)**.
   - Increase **(nx, ny, nz)** to show more unit cells.
   - Select two elements & pick colors for each.
   - Choose 2D or 3D lattice types to generate (noting the known overlapping bugs).

## Future Fixes

- **Address Overlapping** in 2D and 3D hex.
- **Fix Slider Refresh** to restore dynamic updates when constants/angles change.

## Contact

For questions or feedback:

- **Name:** Devin Patrick Gaughan
- **GitHub:** [devin-gaughan](https://github.com/devin-gaughan)
- **Email:** devin@devingaughan.com
