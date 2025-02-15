# Auraeon - Crystal Lattice Simulator v0.3.21

## Overview

The **Auraeon Crystal Lattice Simulator** is a Python-based program designed to generate and visualize 2D and 3D crystal lattices. Version **v0.3.21** builds on v0.3.1 by adding customizable unit cell size (`nx, ny, nz`), allowing users to specify the number of unit cells in each direction dynamically.

## Features in v0.3.21

### **Adjustable Lattice Constants & Unit Cell Size**
- **New UI Sliders:** Modify lattice parameters (`a, b, c, α, β, γ`) via sliders.
- **Unit Cell Customization:** Adjust unit cell count in each direction (`nx, ny, nz`).
- **Real-Time Updates:** Changes dynamically modify lattice structures without restarting the program.
- **Updated Lattice Generation:** Supports variable lattice constants and multiple unit cells in 2D and 3D structures.

### **Supported Lattice Types**
- **2D Lattices:**
  - Simple Cubic
  - Triangular
  - Hexagonal
- **3D Lattices:**
  - Simple Cubic
  - Body-Centered Cubic (BCC)
  - Face-Centered Cubic (FCC)

### **Multi-Element Support**
- **Dropdown selection for atomic species**
- **Color picker for real-time element customization**
- **Dynamic legend for element identification in multi-element plots**

### **Visualization Enhancements**
- **Legend Placement Fixes:** Legends appear outside the plot to avoid overlap.
- **Improved Axis Scaling:** Adjustments ensure better visualization of lattice structures.
- **Updated GUI Layout:** Improved organization and button placement for better usability.

## Known Bugs and Issues
- **Single element 2D and 3D plots show "unknown" instead of the name of `element_1` in their legend label.**
- **Plot axis labels do not update dynamically when sliders are changed—requiring a new plot window to be opened to see the updated slider values.**
- **Sliders are not labeled with what value their position on the slider bar represents.**
- **Element selector drop-downs only allow `element_1` to be used for corner atoms and `element_2` to be used for face and body-centered atoms—there is no way to view a multi-element plot using Simple Cubic or 2D plots.**
- **2D plots and Simple Cubic 3D plots only show single elements even when two elements are selected (3D BCC and 3D FCC are unaffected).**
- **3D plots do not correctly scale with increasing unit cell count (`nx, ny, nz`), causing distortion in the visualization.**
- **2D plots currently do not use the adjustable unit cell values (`nx, ny`) and always display a fixed grid size.**

## Future Work (v0.3.22 - v0.3.29)
- **Fix UI bugs related to element selection and visualization.**
- **Improve real-time updating of axis labels when sliders are changed.**
- **Enable two-element rendering for Simple Cubic and 2D plots.**
- **Fix scaling issues for 3D plots with larger unit cell counts.**
- **Ensure 2D plots correctly use `nx` and `ny` values for unit cell sizing.**
- **Continue optimizing visualization scaling for large lattice structures.**

## Installation & Running

1. **Clone or Download** the repository:
   ```bash
   git clone https://github.com/devin-gaughan/Code-Projects.git
   ```
2. **Navigate into the project directory:**
   ```bash
   cd auraeon-atomic-crystal-sim-in-python
   ```
3. **Run the main script:**
   ```bash
   python main.py
   ```

## Contact

For questions or feedback:
- **Name:** Devin Patrick Gaughan
- **GitHub:** [devin-gaughan](https://github.com/devin-gaughan)
- **Email:** devin@devingaughan.com
