# Import necessary functions
from curve_io import read_csv, save_as_svg
from curve_detection import is_straight_line, has_reflection_symmetry  # Ensure to import the needed functions
from curve_regularization import regularize_straight_line
import matplotlib.pyplot as plt

def plot(paths_XYs):
    fig, ax = plt.subplots(tight_layout=True, figsize=(8, 8))
    for XYs in paths_XYs:
        for XY in XYs:
            if is_straight_line(XY):
                regularized_XY = regularize_straight_line(XY)
                ax.plot(regularized_XY[:, 0], regularized_XY[:, 1], linewidth=2, color='green')  # Regularized line in green
            elif has_reflection_symmetry(XY, axis='x'):
                ax.plot(XY[:, 0], XY[:, 1], linewidth=2, color='red')  # Symmetric curve in red
            else:
                ax.plot(XY[:, 0], XY[:, 1], linewidth=2, color='blue')  # Original curve in blue
    ax.set_aspect('equal')
    plt.show()

if __name__ == "__main__":
    csv_path = 'C:/Users/LENOVO/OneDrive/Desktop/Adobe/problems/frag0.csv'
    print("Reading CSV file...")
    paths_XYs = read_csv(csv_path)
    print("Paths_XYs:", paths_XYs)
    plot(paths_XYs)
    save_as_svg(paths_XYs, filename='output.svg')
