# Part 1
import numpy as np

# import pandas as pd

# import data from txt
with open("2024\Day_02\data.txt", "r") as f:
    data = [line.strip().split(" ") for line in f]

# process data a row at a time
# determine if row is increasing or decreasing
# confirm row continues increasing/decreasing at a change of 1-3
# count the number of safe rows
# r, l = 0, 0
# safe, unsafe = [], []
# while r < len(data):  # r for reports
#    int_data = list(map(int, data[r]))
#    dif = [int_data[i] - int_data[i - 1] for i in range(1, len(data[r]))]
#    if all(i < 0 for i in dif) and all(i >= -3 for i in dif):
#        safe.append(r)
#    elif all(i <= 3 for i in dif) and all(i > 0 for i in dif):
#        safe.append(r)
#    else:
#        unsafe.append(r)
#    r += 1
## print(f"safe = {safe}")
## print(f"unsafe = {unsafe}")
# print(f"Number of Safe: {len(safe)}")


# Part 2
def detect_changes(report):
    r, l = 0, 0
    safe, unsafe = [], []
    while r < len(report):  # r for reports
        int_data = list(map(int, report[r]))
        dif = [int_data[i] - int_data[i - 1] for i in range(1, len(report[r]))]
        if all(i < 0 for i in dif) and all(i >= -3 for i in dif):
            safe.append(int_data)
        elif all(i <= 3 for i in dif) and all(i > 0 for i in dif):
            safe.append(int_data)
        else:
            unsafe.append(int_data)
        r += 1
    print(f"Number of Safe: {len(safe)}")
    # print(f"safe = {safe}")
    # print(f"unsafe = {unsafe}")
    return safe, unsafe


def remove_unsafe_level(report):
    x = 0
    all_good = report
    while x < len(report):
        int_data = list(map(int, report[x]))
        dif = [int_data[i] - int_data[i - 1] for i in range(1, len(report[x]))]
        # print(dif)
        count = []
        for i, y in enumerate(dif):
            if (y == 0) or (y < -3) or (y > 3):
                count.append(i)
        if (len(count) == 1) and (i < len(dif) - 1):
            del report[x][i + 1]
        elif (len(count) == 1) and (i == len(dif) - 1):
            del report[x][i]

        if is_neither_increasing_nor_decreasing(report[x]):
            lst = report[x]
            if all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)):
                # if increasing: find and remove first decrease
                for i in range(len(lst) - 1):
                    if lst[i] > lst[i + 1]:
                        del report[x][i]
            elif all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1)):
                # if decreasing: find and remove first increase
                for i in range(len(lst) - 1):
                    if lst[i] < lst[i + 1]:
                        del report[x][i]
            # print(is_neither_increasing_nor_decreasing(report[x]))
        x += 1
        # print(count)
    return all_good


def is_neither_increasing_nor_decreasing(lst):
    is_increasing = all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
    is_decreasing = all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))
    return not (is_increasing or is_decreasing)


# find the number of safe if you remove the 1st instance of unsafe in the report
good, bad = detect_changes(data)
good_now = remove_unsafe_level(bad)
new_good, new_bad = detect_changes(good_now)
print(f"Total Safe: {len(good) + len(new_good)}")
print(new_bad)
