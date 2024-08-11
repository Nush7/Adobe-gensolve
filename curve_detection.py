import numpy as np

def is_straight_line(XY, tolerance=1e-6):
    x = XY[:, 0]
    y = XY[:, 1]
    if len(x) <= 2:
        return True
    slopes = (y[1:] - y[:-1]) / (x[1:] - x[:-1])
    return np.all(np.abs(slopes - slopes[0]) < tolerance)

def has_reflection_symmetry(XY, axis='x'):
    if axis == 'x':
        return np.allclose(XY[:, 1], -XY[::-1, 1])
    elif axis == 'y':
        return np.allclose(XY[:, 0], -XY[::-1, 0])
    return False