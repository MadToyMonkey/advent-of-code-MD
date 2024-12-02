## Part 1
# organize lists from smallest to largest
import numpy as np

data = np.loadtxt("2024\Day_01\data.txt", delimiter=None)
left = np.sort(data[:, 0])
right = np.sort(data[:, 1])

# pair up the numbers in order for both lists
paired = []
x = 0

while x < len(left):
    # find the difference between the pairs (absolute)
    paired.append(abs(left[x] - right[x]))
    x += 1
# sum all the differences
print(sum(paired))

## Part 2
