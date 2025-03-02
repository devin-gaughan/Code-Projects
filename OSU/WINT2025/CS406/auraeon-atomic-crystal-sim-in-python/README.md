# Auraeon - Crystal Lattice Simulator v0.3.6

## Overview

The **Auraeon Crystal Lattice Simulator** is a Python-based program designed to generate and visualize 2D and 3D crystal lattices with customizable parameters. This version (v0.3.7) introduces **bond visualization** and **nearest neighbor highlighting**, adding enhanced interactivity and analytical capabilities to the simulator.

## Features

### 1. Bond Visualization & Nearest Neighbor Highlighting

- **Bond Length Slider**:
    - Users can adjust the bond threshold dynamically using a slider in the UI.

-   **Bond Rendering:**
    - Bonds between atoms are computed and drawn based on the user-defined bond length.

-   **Nearest Neighbor Highlighting:**
    - Clicking on an atom highlights its nearest neighbors within the bond length.

### 2. Real-Time UI Interactivity

-   **Live Plot Updates**:
    -   Changes to sliders, dropdowns, or color selections immediately re-render the lattice.

-   **Single-Window Interface**:
    -   The same figure is reused for both 2D and 3D plots, preventing unnecessary windows from opening.

### 3. 2D & 3D Lattice Types

-   **2D**: Simple Cubic, Triangular, Hexagonal.
-   **3D**: Simple Cubic, BCC, FCC, Hexagonal.
-   **Multi-Element Configurations**: Supports distinct element positioning in BCC and FCC.

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

## Fixed Bugs in v0.3.7

*   Addressed an issue where bonds were not displaying correctly with all bond length threshold values.
*   Corrected issues related to coordinate calculations.

## Known Issues

1.  **3D View Resets on Hard Refresh**:

    *   If the entire figure window is closed, camera angles reset to default.

## Future Work

*   **v0.3.8: Defects & Doping Simulation**
    *   Introduce vacancies: Users can define a % of missing atoms.
    *   Implement atomic substitution: Randomly replace atoms in the lattice.

*   **Export to CIF/XYZ**: Save lattice structures for external software.

## Contact

*   **Name**: Devin Patrick Gaughan
*   **GitHub**: [devin-gaughan](https://github.com/devin-gaughan)
*   **Email**: devin@devingaughan.com