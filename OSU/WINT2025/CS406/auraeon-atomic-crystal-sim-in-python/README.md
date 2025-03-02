# Auraeon - Crystal Lattice Simulator v0.3.6

## Overview

The **Auraeon Crystal Lattice Simulator** is a Python-based program designed to generate and visualize 2D and 3D crystal lattices with customizable parameters. **Version v0.3.6** improves UI clarity by fixing **legend positioning** and implementing **3D camera angle preservation**.

## Features

### 1. Legend & 3D Camera Enhancements

- **Legend Placement Fix**:
  - **Legends are now positioned outside the main plot area**, preventing overlap with atoms.
  - 2D and 3D legends are **aligned to the right** of the figure.
- **3D Camera Angle Preservation**:
  - User-defined **camera angles (elev, azim)** persist between re-plots.
  - The simulator now remembers custom **zoom, rotation, and elevation adjustments**.

### 2. Real-Time UI Interactivity

- **Live Plot Updates**:
  - All changes to sliders (`a, b, c, α, β, γ, nx, ny, nz`), crystal system dropdowns, or color selection **immediately re-render the lattice**.
- **No Extra Windows**:
  - The **same figure** is reused for both 2D and 3D, preventing unnecessary windows from opening.

### 3. 2D & 3D Lattice Types

- **2D**: Simple Cubic, Triangular, Hexagonal.
- **3D**: Simple Cubic, BCC, FCC, Hexagonal.
- **Multi-Element Configurations**:
  - Supports distinct element positioning in BCC and FCC.

## Installation & Running

Clone or download this repository:

```
git clone https://github.com/devin-gaughan/Code-Projects.git
```

Navigate into the project directory:

```
cd auraeon-atomic-crystal-sim-in-python
```

Install the required Python packages:

```
pip install -r requirements.txt
```

Run the main script:

```
python main.py
```

Interact with the GUI:

```
- Choose a lattice type (2D or 3D).
- Adjust lattice constants (a, b, c, α, β, γ) and unit cells (nx, ny, nz).
- Select and color two elements, swap or unify them.
- Change the crystal system to auto-adjust relationships between lattice parameters.
```

## Fixed Bugs in v0.3.6

- **Legend Overlap Eliminated**:
  - The legend now appears **outside** the main plot area, ensuring no interference with atoms.
- **Camera Rotation Persistence**:
  - 3D **camera angles no longer reset** after refreshing the plot.

## Known Issues

1. **Legend Clipping on Small Screens**:
   - While the legend placement is fixed, very small window sizes may still result in slight clipping.
2. **3D View Resets on Hard Refresh**:
   - If the **entire figure window is closed**, camera angles reset to default.

## Future Work

- **v0.3.7: Bond Visualization & Nearest Neighbors**.
- **Vacancy & Doping Simulation**: Randomly remove atoms (vacancies) or replace elements in select sites.
- **Export to CIF/XYZ**: Save lattice structures for external software.

## Contact

- **Name**: Devin Patrick Gaughan
- **GitHub**: [devin-gaughan](https://github.com/devin-gaughan)
- **Email**: devin@devingaughan.com
