import sys

# Input
spreadsheet = []

with open('spreadsheet.in') as f:
    for line in f:
       spreadsheet.append([int(i) for i in line.split()])

# Algorithm
checksum = 0
for line in spreadsheet:
    minimum, maximum = sys.maxsize, -sys.maxsize
    for number in line:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
    checksum += (maximum-minimum)

print (checksum)
