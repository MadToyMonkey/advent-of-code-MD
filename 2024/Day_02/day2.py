import numpy as np
import pandas as pd

# import data from txt
with open("2024\Day_02\data.txt", "r") as f:
    data = [line.strip().split(" ") for line in f]

# process data a row at a time
# determine if row is increasing or decreasing
# confirm row continues increasing/decreasing at a change of 1-3
# count the number of safe rows
r, l = 0, 0
safe, unsafe = [], []
while r < len(data):  # r for reports
    int_data = list(map(int, data[r]))
    dif = [int_data[i] - int_data[i - 1] for i in range(1, len(data[r]))]
    if all(i < 0 for i in dif) and all(i >= -3 for i in dif):
        safe.append(r)
    elif all(i <= 3 for i in dif) and all(i > 0 for i in dif):
        safe.append(r)
    else:
        unsafe.append(r)
    r += 1
# print(f"safe = {safe}")
# print(f"unsafe = {unsafe}")
print(f"Number of Safe: {len(safe)}")
