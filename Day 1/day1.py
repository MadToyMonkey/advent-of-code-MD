# Advent of Code: Day 1
'''
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
Consider your entire calibration document. What is the sum of all of the calibration values?
'''
# get the numbers out of the line
import csv
import re

## get data out of csv
with open('Day 1\input.csv',newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
#print(data)
for x in data:

#print(num_list)

# save the first and last digit together

# sum the new two digit numbers