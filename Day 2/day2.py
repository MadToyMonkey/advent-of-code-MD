# Advent of Code: Day 2-1
'''
Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.
What is the sum of the IDs of those games?
'''
#imports
import re
import csv

# Get data into list
red = 12 
green = 13 
blue = 14   # num of cubes in bag
poss = []   # list of possible games
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
        if(max(r)<=red)&(max(g)<=green)&(max(b)<=blue):
            poss.append(line[0])
    wins = [int(i) for i in re.findall(r"(?<=Game.)\d+",str(poss))]
    print(sum(wins))
#print(data)