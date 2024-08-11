import numpy as np
import svgwrite

from curve_detection import is_straight_line

def save_as_svg(paths_XYs, filename):
    """
    Save the curves as an SVG file.

    Args:
        paths_XYs (list): List of curves, where each curve is a list of (x, y) points.
        filename (str): Output SVG file name.

    Returns:
        None
    """
    # Create an SVG drawing object
    dwg = svgwrite.Drawing(filename, size=(800, 800))

    # Define the stroke styles for different types of curves
    stroke_styles = {
        'straight': {'stroke': 'green', 'stroke-width': 2},
        'symmetric': {'stroke': 'red', 'stroke-width': 2},
        'original': {'stroke': 'blue', 'stroke-width': 2}
    }

    # Iterate over the curves and add them to the SVG drawing
    for XYs in paths_XYs:
        for XY in XYs:
            if is_straight_line(XY):
                stroke_style = stroke_styles['straight']
            elif is_reflection_symmetric(XY, axis='x'):
                stroke_style = stroke_styles['symmetric']
            else:
                stroke_style = stroke_styles['original']

            # Create an SVG path element for the curve
            path = dwg.path(d="M {} {}".format(XY[0][0], XY[0][1]), **stroke_style)
            for x, y in XY[1:]:
                path.push("L {} {}".format(x, y))

            # Add the path element to the SVG drawing
            dwg.add(path)

    # Save the SVG drawing to a file
    dwg.save()


def read_csv(csv_path):
    np_path_XYs = np.genfromtxt(csv_path, delimiter=',')
    path_XYs = []
    for i in np.unique(np_path_XYs[:, 0]):
        npXYs = np_path_XYs[np_path_XYs[:, 0] == i][:, 1:]
        XYs = []
        for j in np.unique(npXYs[:, 0]):
            XY = npXYs[npXYs[:, 0] == j][:, 1:]
            XYs.append(XY)
        path_XYs.append(XYs)
    return path_XYs

# def save_as_svg(paths_XYs, filename='output.svg'):
#     dwg = svgwrite.Drawing(filename, profile='tiny')
#     for XYs in paths_XYs:
#         for XY in XYs:
#             points = [(x, y) for x, y in XY]
#             dwg.add(dwg.polyline(points, stroke=svgwrite.rgb(10, 10, 16, '%'), fill='none'))
#     dwg.save()
