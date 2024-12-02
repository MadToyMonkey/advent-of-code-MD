# Advent of Code: Day 2-2
'''
As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
'''
#imports
import re
import csv

# Get data into list
red = 12 
green = 13 
blue = 14   # num of cubes in bag
power = []   # list of possible games
with open('Day 2\input.csv', newline='\n') as f:
    reader = csv.reader(f,)
    data = list(reader)
    for line in data:
        line = (str(line).replace(":",";") # replace game ID colon with semi colon
        .replace("'","") # remove excess single quotes
        .split(";")) # split each game round into separate elements
    # determine possible games
        r = [int(i) for i in re.findall(r"\d+.(?=red)",str(line))]
        g = [int(i) for i in re.findall(r"\d+.(?=green)",str(line))]
        b = [int(i) for i in re.findall(r"\d+.(?=blue)",str(line))]
        power.append(max(r)*max(g)*max(b))
    print(sum(power))
#print(data)