import numpy as np

def regularize_straight_line(XY):
    x1, y1 = XY[0]
    x2, y2 = XY[-1]
    return np.array([[x1, y1], [x2, y2]])
