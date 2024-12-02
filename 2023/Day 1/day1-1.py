# Advent of Code: Day 1
'''
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
Consider your entire calibration document. What is the sum of all of the calibration values?
'''
# get the numbers out of the line
import csv
import re

## get data out of csv
with open('Day 1\input.csv', newline='\n') as f:
    reader = csv.reader(f)
    data = list(reader)
#print(data[0])
digits = []
for x in data:
    x_num = re.findall(r"\d",str(x))
    digits.append(x_num)
#print(digits[3])

# save the first and last digit together
sum = []
for x in digits:
    sum.append(x[0]+x[-1])
print(sum)
# sum the new two digit numbers
total = 0
for x in sum:
    total = total + int(x)
print(total)