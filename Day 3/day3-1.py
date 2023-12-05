# Advent of Code Day 3 - 1
'''
The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. 
If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. 
There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. 
(Periods (.) do not count as a symbol.)

What is the sum of all of the part numbers in the engine schematic?
'''

import csv, re

with open('Day 3\input.csv', newline='\n') as f:
    reader = csv.reader(f,)
    data = list(reader)
def sym_check(i,j,list):
    if '*'|'#'|'+'|'$' in list[i][j]:
            if(list[i][j-1].isnumeric()):
                r = list[i][j-1] + list[i][j]
                if(list[i][j+1].isnumeric()):
                    r = r + list[i][j+1]
                    list[i][j+1] = 'x'
                list[i][j-1] = 'x'
            list[i][j] = 'x'
            return r
def num_check(i,j,list):
    '''check if element is a number'''
    if(list[i][j].isnumeric()):
        if '*'|'#'|'+'|'$' in list[i-1][j-1]:
            if(list[i][j-1].isnumeric()):
                r = list[i][j-1] + list[i][j]
                if(list[i][j+1].isnumeric()):
                    r = r + list[i][j+1]
                    list[i][j+1] = 'x'
                list[i][j-1] = 'x'
            list[i][j] = 'x'
            return r
        if '*'|'#'|'+'|'$' in list[i-1][j-1]:
            if(list[i][j-1].isnumeric()):
                r = list[i][j-1] + list[i][j]
                if(list[i][j+1].isnumeric()):
                    r = r + list[i][j+1]
                    list[i][j+1] = 'x'
                list[i][j-1] = 'x'
            list[i][j] = 'x'
            return r
        if '*'|'#'|'+'|'$' in list[i][j-1]:
            if(list[i][j-1].isnumeric()):
                r = list[i][j-1] + list[i][j]
                if(list[i][j+1].isnumeric()):
                    r = r + list[i][j+1]
                    list[i][j+1] = 'x'
                list[i][j-1] = 'x'
            list[i][j] = 'x'
            return r
        if '*'|'#'|'+'|'$' in list[i+1][j-1]:
            if(list[i][j-1].isnumeric()):
                r = list[i][j-1] + list[i][j]
                if(list[i][j+1].isnumeric()):
                    r = r + list[i][j+1]
                    list[i][j+1] = 'x'
                list[i][j-1] = 'x'
            list[i][j] = 'x'
            return r
        if '*'|'#'|'+'|'$' in list[i-1][j]:
            if(list[i][j-1].isnumeric()):
                r = list[i][j-1] + list[i][j]
                if(list[i][j+1].isnumeric()):
                    r = r + list[i][j+1]
                    list[i][j+1] = 'x'
                list[i][j-1] = 'x'
            list[i][j] = 'x'
            return r
        if '*'|'#'|'+'|'$' in list[i+1][j]:
            if(list[i][j-1].isnumeric()):
                r = list[i][j-1] + list[i][j]
                if(list[i][j+1].isnumeric()):
                    r = r + list[i][j+1]
                    list[i][j+1] = 'x'
                list[i][j-1] = 'x'
            list[i][j] = 'x'
            return r
        if '*'|'#'|'+'|'$' in list[i-1][j+1]:
            if(list[i][j-1].isnumeric()):
                r = list[i][j-1] + list[i][j]
                if(list[i][j+1].isnumeric()):
                    r = r + list[i][j+1]
                    list[i][j+1] = 'x'
                list[i][j-1] = 'x'
            list[i][j] = 'x'
            return r
        if '*'|'#'|'+'|'$' in list[i][j+1]:
            if(list[i][j-1].isnumeric()):
                r = list[i][j-1] + list[i][j]
                if(list[i][j+1].isnumeric()):
                    r = r + list[i][j+1]
                    list[i][j+1] = 'x'
                list[i][j-1] = 'x'
            list[i][j] = 'x'
            return r
        if '*'|'#'|'+'|'$' in list[i+1][j+1]:
            if(list[i][j-1].isnumeric()):
                r = list[i][j-1] + list[i][j]
                if(list[i][j+1].isnumeric()):
                    r = r + list[i][j+1]
                    list[i][j+1] = 'x'
                list[i][j-1] = 'x'
            list[i][j] = 'x'
            return r

element = []
for line in data:
    for x in line:
        z = []
        for y in x: z = z + ([*y])
    element.append(z)


#print(data)