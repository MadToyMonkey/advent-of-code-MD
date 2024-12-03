import re

# import corrupted data
pattern = r"mul\((\d+),(\d+)\)"

with open("2024\\Day_03\\data.txt", "r") as f:
    line = f.read()

# process massive string
matches = re.findall(pattern, line)
# Convert matched digits to integers
matches = [(int(n1), int(n2)) for n1, n2 in matches]
# Multiply each pair and sum the products
total_sum = sum(n1 * n2 for n1, n2 in matches)

print("Sum of products:", total_sum)
