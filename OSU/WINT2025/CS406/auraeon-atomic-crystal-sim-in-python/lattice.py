import numpy as np

def generate_2d_simple_cubic(nx, ny, a, b):
    x_vals = np.linspace(0, (nx - 1) * a, nx)
    y_vals = np.linspace(0, (ny - 1) * b, ny)
    x, y = np.meshgrid(x_vals, y_vals)
    return x, y

def generate_2d_triangular(nx, ny, a, b):
    x, y = generate_2d_simple_cubic(nx, ny, a, b)
    x[1::2] += a / 2
    return x, y

def generate_2d_hexagonal(nx, ny, a, b):
    x, y = generate_2d_triangular(nx, ny, a, b)
    y *= np.sqrt(3) / 2
    return x, y

def generate_3d_simple_cubic(nx, ny, nz, a, b, c):
    x_vals = np.linspace(0, (nx - 1) * a, nx)
    y_vals = np.linspace(0, (ny - 1) * b, ny)
    z_vals = np.linspace(0, (nz - 1) * c, nz)
    x, y, z = np.meshgrid(x_vals, y_vals, z_vals)
    return x, y, z

def generate_bcc(nx, ny, nz, a, b, c):
    x, y, z = generate_3d_simple_cubic(nx, ny, nz, a, b, c)
    x_bcc = x + a / 2
    y_bcc = y + b / 2
    z_bcc = z + c / 2
    return (x, y, z), (x_bcc, y_bcc, z_bcc)

def generate_fcc(nx, ny, nz, a, b, c):
    x, y, z = generate_3d_simple_cubic(nx, ny, nz, a, b, c)
    fcc_offsets = [
        (0, b/2, c/2), (a, b/2, c/2),
        (a/2, 0, c/2), (a/2, b, c/2),
        (a/2, b/2, 0), (a/2, b/2, c)
    ]
    offset_arrays = []
    for (ox, oy, oz) in fcc_offsets:
        offset_arrays.append((x + ox, y + oy, z + oz))
    return (x, y, z), offset_arrays

def generate_3d_hexagonal(nx, ny, nz, a, b, c):
    x_vals = np.linspace(0, (nx - 1) * a, nx)
    y_vals = np.linspace(0, (ny - 1) * b, ny)
    z_vals = np.linspace(0, (nz - 1) * c, nz)
    x, y, z = np.meshgrid(x_vals, y_vals, z_vals)
    y *= np.sqrt(3) / 2
    return x, y, z
