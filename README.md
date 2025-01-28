# Code-Projects

# Crystal Lattice Simulator v0.2.0

## Overview

This repository demonstrates a Python-based crystal lattice simulator, currently capable of generating and visualizing:

- **2D Lattices**: Simple Cubic (SC), Triangular, Hexagonal
- **3D Lattices**: Simple Cubic (SC), Body-Centered Cubic (BCC), Face-Centered Cubic (FCC)

At this stage (v0.2.0), the program allows you to:

1. Generate 2D and 3D lattice coordinate grids.
2. Visualize them in separate Matplotlib windows via **Tkinter** GUI buttons.

**GitHub Repository Location:**  
[https://github.com/devin-gaughan/Code-Projects/tree/master/OSU/WINT2025/CS406/auraeon-atomic-crystal-sim-in-python](https://github.com/devin-gaughan/Code-Projects/tree/master/OSU/WINT2025/CS406/auraeon-atomic-crystal-sim-in-python)

## Features

- **Folder Structure**

  - `lattice.py`: Lattice generation functions for 2D and 3D.
  - `visualization.py`: Basic plotting functions for 2D and 3D.
  - `main.py`: A Tkinter GUI that provides buttons to select each lattice type and display the resulting structure.

- **3D Lattice Support**

  - **Simple Cubic (SC)**: Corner atoms only
  - **BCC**: SC + center atoms
  - **FCC**: SC + face-centered atoms

- **Tkinter GUI**
  - Buttons for **2D** structures (SC, Tri, Hex)
  - Buttons for **3D** structures (SC, BCC, FCC)
  - Each button click opens a Matplotlib window with the chosen lattice.

## Project Status (v0.2.0)

- **What’s Done**

  - 2D lattice generation and visualization working.
  - 3D lattice generation (SC, BCC, FCC) implemented.
  - Tkinter buttons trigger separate plots for different lattice types.

- **What’s Next**
  - Interval 3 (not yet implemented here) will introduce interactive sliders for grid size and lattice constants.
  - Future intervals may include embedding Matplotlib in a single window and advanced 3D interactivity.

## Getting Started

### Prerequisites

- **Python 3.8+** (or a reasonably recent version)
- **Pip** package manager

### Dependencies

- `numpy`
- `matplotlib`
- Tkinter (typically installed with Python on most platforms)

You can install dependencies with:

```bash
pip install numpy matplotlib
```

### Installation & Running

1. **Clone or Download** this repository:
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
   - Click a **2D** button (SC, Tri, Hex) or a **3D** button (SC, BCC, FCC).
   - A Matplotlib window appears displaying the generated lattice points.

## Usage Example

When you click **3D BCC**, for example, the script:

1. Calls the `generate_bcc()` function from `lattice.py`.
2. Combines corner atoms and center atoms into coordinate arrays.
3. Opens a Matplotlib window to visualize the scatter plot in 3D.

## Contributing

This project is in a learning/demo phase. Contributions or suggestions are welcome, but please note that features like sliders, advanced 3D embedding, or additional lattice types are planned for future versions.

## License

Feel free to use the code for educational or personal projects. Not for commercial use.

## Contact

For questions or feedback:

- **Name**: Devin Patrick Gaughan
- **GitHub**: devin-gaughan
- **Email**: devin@devingaughan.com
