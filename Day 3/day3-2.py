# Advent of Code Day 3 - 2
'''
The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. 
Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.
What is the sum of all of the gear ratios in your engine schematic?
'''

import csv, re

with open('Day 3\input.csv', newline='\n') as f:
    reader = csv.reader(f,)
    data = list(reader)

def num_check(i,j,list):
    '''check if element is a number'''
    if(list[i][j].isnumeric()):
        num = list[i][j]
        if(list[i][j-1].isnumeric()):
            num = list[i][j-1] + num
            list[i][j-1] = '.'
            if(list[i][j-2].isnumeric()):
                num = list[i][j-2] + num
                list[i][j-2] = '.'
        if(list[i][j+1].isnumeric()):
            num = num + list[i][j+1]
            list[i][j+1] = '.'
            if(list[i][j+2].isnumeric()):
                num = num + list[i][j+2]
                list[i][j+2] = '.'
        list[i][j] = '.'
        return num

# break each line into elements to be parsed
element = []
for line in data:
    for x in line:
        z = []
        for y in x: z = z + ([*y])
    element.append(z)


product = []
# determine if element is symbol
for i,x in enumerate(element):
    for j,y in enumerate(x):
        part = []
        if not y.isalnum():
            if not y=='.':
                #print (y)
                # determine if symbol touches numbers
                num1 = num_check(i-1,j-1,element)
                if num1 != None: part.append(num1)
                num2 = num_check(i-1,j,element)
                if num2 != None: part.append(num2)
                num3 = num_check(i-1,j+1,element)
                if num3 != None: part.append(num3)
                num4 = num_check(i,j-1,element)
                if num4 != None: part.append(num4)
                num5 = num_check(i,j+1,element)
                if num5 != None: part.append(num5)
                num6 = num_check(i+1,j-1,element)
                if num6 != None: part.append(num6)
                num7 = num_check(i+1,j,element)
                if num7 != None: part.append(num7)
                num8 = num_check(i+1,j+1,element)
                if num8 != None: part.append(num8)
            if (y=='*')&(len(part)==2):
                ratio = int(part[0])*int(part[1])
                product.append(ratio)


            



# add number to part

print(sum(product))