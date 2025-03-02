# Auraeon - Crystal Lattice Simulator v0.3.8

## Overview

The **Auraeon Crystal Lattice Simulator** is a Python-based program designed to generate and visualize 2D and 3D crystal lattices with customizable parameters. This version (v0.3.8) introduces **defect and doping simulation**, adding enhanced flexibility in creating more versatile simulated structures.

## Features

### 1. Defects & Doping Simulation
*   **Vacancy creation:** Ability to define a % of atoms to be missing.
*   **Atomic substitution:** Ability to substitute atoms within the lattice.

### 2. Bond Visualization & Nearest Neighbor Highlighting

*   **Bond Length Slider**:

    *   Users can adjust the bond threshold dynamically using a slider in the UI.
*   **Bond Rendering:**

    *   Bonds between atoms are computed and drawn based on the user-defined bond length.
*   **Nearest Neighbor Highlighting:**

    *   Clicking on an atom highlights its nearest neighbors within the bond length.

### 3. Real-Time UI Interactivity

*   **Live Plot Updates**:

    *   Changes to sliders, dropdowns, or color selections immediately re-render the lattice.
*   **Single-Window Interface**:

    *   The same figure is reused for both 2D and 3D plots, preventing unnecessary windows from opening.

### 4. 2D & 3D Lattice Types

*   **2D**: Simple Cubic, Triangular, Hexagonal.
*   **3D**: Simple Cubic, BCC, FCC, Hexagonal.
*   **Multi-Element Configurations**: Supports distinct element positioning in BCC and FCC.

## Installation & Running

Clone or download this repository:
git clone https://github.com/devin-gaughan/Code-Projects.git

Navigate into the project directory:
cd auraeon-atomic-crystal-sim-in-python

Install the required Python packages:
pip install -r requirements.txt

Run the main script:
python main.py

Interact with the GUI:
* Choose a lattice type (2D or 3D).
* Adjust lattice constants (a, b, c, α, β, γ) and unit cells (nx, ny, nz).
* Select and color two elements, swap or unify them.
* Change the crystal system to auto-adjust relationships between lattice parameters.
* Adjust the bond length threshold using the slider.
* Click on an atom in the plot to highlight its nearest neighbors.

## Fixed Bugs in v0.3.8

* Fixed a critical bug preventing 3D visualization of BCC and FCC lattices.
* Resolved issue of program crash by ensuring all variables are locally accessible.

## Known Issues

1.  **3D View Resets on Hard Refresh**:
If the entire figure window is closed, camera angles reset to default.
2. **Incorrect Legend Labels**: The legend displays only Element 2's color.

## Future Work

*   **v0.3.9: Export & Import Features**
    *   Save lattice structures to CIF/XYZ files.
    *   Load lattice structures from external data.
    *   Allow exporting high-resolution PNG images.
*   **v0.4.0: Advanced Computation & Analysis**
    *   Atomic Packing Factor Calculation.
    *   Nearest-Neighbor Distance Measurement.
    *   Lattice Energy Approximation (Lennard-Jones Potential).
*   **v0.5.x: Research-Grade Features**
    *   Diffraction Pattern Simulation (Powder & Single Crystal).
    *   Reciprocal Space Visualization.
    *   Monte Carlo Simulations for Phase Transitions.
*   **v0.6.x: AI-Assisted Features**
    *   Machine Learning-based Material Prediction.
    *   AI-assisted Structure Optimization.

## Contact

*   **Name**: Devin Patrick Gaughan
*   **GitHub**: [devin-gaughan](https://github.com/devin-gaughan)
*   **Email**: devin@devingaughan.com
