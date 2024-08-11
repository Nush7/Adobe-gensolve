import numpy as np
import matplotlib.pyplot as plt
import csv

# Function to read CSV file and extract curve data
def read_csv(csv_path):
    try:
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
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

# Function to plot the curves
def plot(paths_XYs):
    fig, ax = plt.subplots(tight_layout=True, figsize=(8, 8))
    for XYs in paths_XYs:
        for XY in XYs:
            ax.plot(XY[:, 0], XY[:, 1], linewidth=2)
    ax.set_aspect('equal')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Curve Plot')
    plt.show()

# Example usage: Replace 'path_to_your_csv_file.csv' with your CSV file path
csv_path = 'C:/Users/LENOVO/OneDrive/Desktop/Adobe/problems/frag0.csv'
paths_XYs = read_csv(csv_path)
if paths_XYs:
    plot(paths_XYs)