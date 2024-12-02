import numpy as np

# Replace 'your_file.txt' with the path to your file
data = np.loadtxt(
    "2024\Day_01\data.txt", delimiter=None
)  # Use '\t' for tab-separated data
column1 = data[:, 0]  # First column
column2 = data[:, 1]  # Second column

print("Column 1:", column1)
print("Column 2:", column2)
