# Auraeon - Crystal Lattice Simulator v0.3.5

## Overview

The **Auraeon Crystal Lattice Simulator** is a Python-based program for generating and visualizing 2D and 3D crystal lattices. Version **v0.3.5** introduces several new capabilities and fixes while retaining a couple of known issues.

## Features

### 1. Dynamic UI & Plot Refresh

- **Live Updates**: Any change in sliders (`a, b, c, α, β, γ, nx, ny, nz`), crystal system selection, or element dropdown **automatically** re-renders the lattice plot.
- **Consolidated Plots**: The same 2D figure and 3D figure are reused without spawning extra windows.

### 2. Multi-Element & Color Picker

- **Two Element Selection**: Choose element_1 and element_2 from a built-in dictionary (see `elements.py`).
- **Unify & Swap**:
  - **Unify**: Makes Element 2 match Element 1 (both type and color).
  - **Swap**: Exchanges the two elements and their colors.
- **Color Pickers** to customize each element’s appearance.

### 3. Crystal System Selector

- **Combo Box**: Pick **isometric, orthorhombic, tetragonal, hexagonal** (placeholders for monoclinic, triclinic).
- **Auto-Overrides**: `(a, b, c, α, β, γ)` adjust to typical angles/side relationships for each system.

### 4. Lattice Constants & Rotation Angles

- **Sliders** for `(a, b, c, α, β, γ)` provide real-time adjustments.
- **2D Rotation**: Optionally apply α to rotate 2D structures in-plane.
- **3D Rotation**: Angles `(α, β, γ)` can rotate the lattice about X/Y/Z (if enabled in the code).

### 5. 2D & 3D Lattice Types

- **2D**: Simple Cubic, Triangular, Hexagonal
- **3D**: Simple Cubic, BCC, FCC, Hex
  - **Multi-Element**: BCC corners vs. center, FCC corners vs. face-centered atoms, etc.

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
