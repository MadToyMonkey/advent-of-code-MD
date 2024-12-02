import numpy as np
import pandas as pd

# import data from txt
data = pd.read_csv("2024\Day_02\\data.txt", delimiter=None)

# process data a row at a time
# determine if row is increasing or decreasing
# confirm row continues increasing/decreasing at a change of 1-3
# count the number of safe rows
r, l = 0, 0
safe, unsafe = [], []
while r < len(data):  # r for reports
    dif = np.diff(data[r])
    if np.all(dif < 0) and np.all(dif >= -3):
        safe.append(r)
    elif np.all(dif <= 3) and np.all(dif > 0):
        safe.append(r)
    else:
        unsafe.append(r)
    r += 1
print(f"safe = {safe}")
print(f"unsafe = {unsafe}")
