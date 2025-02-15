# Auraeon - Crystal Lattice Simulator v0.3.1

## Overview

The **Auraeon Crystal Lattice Simulator** is a Python-based program designed to generate and visualize 2D and 3D crystal lattices. Version **v0.3.1** introduces adjustable lattice constants (a, b, c, α, β, γ), allowing users to dynamically modify lattice structures in real-time.

## Features in v0.3.1

### **Adjustable Lattice Constants**
- **New UI Sliders:** Modify lattice parameters (`a, b, c, α, β, γ`) via sliders.
- **Real-Time Updates:** Adjust lattice constants dynamically without restarting the program.
- **Updated Lattice Generation:** Supports variable lattice constants in 2D and 3D structures.

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

## Future Work (v0.3.2 - v0.3.9)
- **Fix UI bugs related to element selection and visualization.**
- **Improve real-time updating of axis labels when sliders are changed.**
- **Enable two-element rendering for Simple Cubic and 2D plots.**
- **Add better slider labels for clarity.**
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
