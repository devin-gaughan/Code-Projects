# elements.py
"""
Dictionary of elemental data for Auraeon Crystal Lattice Simulator.

Each key is an element's symbol (as a string),
and each value is another dictionary specifying these properties:
- name: Full element name
- color: A Matplotlib friendly color
- radius: Approximate atomic radius used for plotting
- mass: Atomic mass for future plans involving calculating densities, etc.
"""

ELEMENT_DATA = {
    "H": {
        "name": "Hydrogen",
        "color": "white",
        "radius": 0.25,
        "mass": 1.008
    },
    "He": {
        "name": "Helium",
        "color": "#ffccd9",  # Light pink
        "radius": 0.31,
        "mass": 4.0026
    },
    "Li": {
        "name": "Lithium",
        "color": "#cc80ff",  # Light purple
        "radius": 1.28,
        "mass": 6.94
    },
    "Be": {
        "name": "Beryllium",
        "color": "#c2ff00",  # Lime
        "radius": 0.96,
        "mass": 9.0122
    },
    "C": {
        "name": "Carbon",
        "color": "gray",
        "radius": 0.70,
        "mass": 12.011
    },
    "N": {
        "name": "Nitrogen",
        "color": "#3050f8",  # Deep blue
        "radius": 0.65,
        "mass": 14.007
    },
    "O": {
        "name": "Oxygen",
        "color": "red",
        "radius": 0.60,
        "mass": 15.999
    },
    "F": {
        "name": "Fluorine",
        "color": "#90e050",  # Greenish
        "radius": 0.50,
        "mass": 18.998
    },
    "Ne": {
        "name": "Neon",
        "color": "#b3e3f5",  # Pale blue
        "radius": 0.38,
        "mass": 20.180
    },
    "Na": {
        "name": "Sodium",
        "color": "#ab5cf2",  # Purple
        "radius": 1.66,
        "mass": 22.990
    },
    "Mg": {
        "name": "Magnesium",
        "color": "#8aff00",  # Light green
        "radius": 1.41,
        "mass": 24.305
    },
    "Al": {
        "name": "Aluminum",
        "color": "#bfa6a6",  # Grayish
        "radius": 1.21,
        "mass": 26.982
    },
    "Si": {
        "name": "Silicon",
        "color": "green",
        "radius": 1.17,
        "mass": 28.085
    },
    "Fe": {
        "name": "Iron",
        "color": "#e06633",  # Orange-brown
        "radius": 1.26,
        "mass": 55.845
    },
    "Cu": {
        "name": "Copper",
        "color": "brown",
        "radius": 1.28,
        "mass": 63.546
    },
    "Ag": {
        "name": "Silver",
        "color": "silver",
        "radius": 1.45,
        "mass": 107.8682
    },
    "Au": {
        "name": "Gold",
        "color": "gold",
        "radius": 1.36,
        "mass": 196.96657
    },
    "Pb": {
        "name": "Lead",
        "color": "#575961",  # Dark gray
        "radius": 1.55,
        "mass": 207.2
    },
    # Will add more elements later...
}
