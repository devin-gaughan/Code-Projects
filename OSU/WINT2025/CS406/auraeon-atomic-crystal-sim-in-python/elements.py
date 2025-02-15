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
        "radius": 0.53,
        "mass": 1.008
    },
    "He": {
        "name": "Helium",
        "color": "cyan",
        "radius": 0.31,
        "mass": 4.0026
    },
    "Li": {
        "name": "Lithium",
        "color": "purple",
        "radius": 1.67,
        "mass": 6.94
    },
    "Be": {
        "name": "Beryllium",
        "color": "darkgreen",
        "radius": 1.12,
        "mass": 9.0122
    },
    "B": {
        "name": "Boron",
        "color": "brown",
        "radius": 0.87,
        "mass": 10.81
    },
    "C": {
        "name": "Carbon",
        "color": "black",
        "radius": 0.70,
        "mass": 12.011
    },
    "N": {
        "name": "Nitrogen",
        "color": "blue",
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
        "color": "green",
        "radius": 0.50,
        "mass": 18.998
    },
    "Ne": {
        "name": "Neon",
        "color": "cyan",
        "radius": 0.38,
        "mass": 20.180
    },
    "Na": {
        "name": "Sodium",
        "color": "blue",
        "radius": 1.90,
        "mass": 22.990
    },
    "Mg": {
        "name": "Magnesium",
        "color": "darkgreen",
        "radius": 1.45,
        "mass": 24.305
    },
    "Al": {
        "name": "Aluminum",
        "color": "gray",
        "radius": 1.18,
        "mass": 26.982
    },
    "Si": {
        "name": "Silicon",
        "color": "orange",
        "radius": 1.11,
        "mass": 28.085
    },
    "P": {
        "name": "Phosphorus",
        "color": "violet",
        "radius": 0.98,
        "mass": 30.974
    },
    "S": {
        "name": "Sulfur",
        "color": "yellow",
        "radius": 0.88,
        "mass": 32.06
    },
    "Cl": {
        "name": "Chlorine",
        "color": "green",
        "radius": 0.79,
        "mass": 35.45
    },
    "Ar": {
        "name": "Argon",
        "color": "cyan",
        "radius": 0.71,
        "mass": 39.948
    },
    "K": {
        "name": "Potassium",
        "color": "blue",
        "radius": 2.43,
        "mass": 39.098
    },
    "Ca": {
        "name": "Calcium",
        "color": "darkgreen",
        "radius": 1.94,
        "mass": 40.078
    },
    "Sc": {
        "name": "Scandium",
        "color": "gray",
        "radius": 1.84,
        "mass": 44.956
    },
    "Ti": {
        "name": "Titanium",
        "color": "gray",
        "radius": 1.76,
        "mass": 47.867
    },
    "V": {
        "name": "Vanadium",
        "color": "gray",
        "radius": 1.71,
        "mass": 50.942
    },
    "Cr": {
        "name": "Chromium",
        "color": "gray",
        "radius": 1.66,
        "mass": 51.996
    },
    "Mn": {
        "name": "Manganese",
        "color": "gray",
        "radius": 1.61,
        "mass": 54.938
    },
    "Fe": {
        "name": "Iron",
        "color": "orange",
        "radius": 1.56,
        "mass": 55.845
    },
    "Co": {
        "name": "Cobalt",
        "color": "blue",
        "radius": 1.52,
        "mass": 58.933
    },
    "Ni": {
        "name": "Nickel",
        "color": "green",
        "radius": 1.49,
        "mass": 58.693
    },
    "Cu": {
        "name": "Copper",
        "color": "brown",
        "radius": 1.45,
        "mass": 63.546
    },
    "Zn": {
        "name": "Zinc",
        "color": "gray",
        "radius": 1.42,
        "mass": 65.38
    },
    "Ag": {
        "name": "Silver",
        "color": "gray",
        "radius": 1.65,
        "mass": 107.87
    },
    "Cd": {
        "name": "Cadmium",
        "color": "gray",
        "radius": 1.61,
        "mass": 112.41
    }
}
