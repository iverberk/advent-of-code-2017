import sys
import itertools

# Input
spreadsheet = []

with open('spreadsheet.in') as f:
    for line in f:
       spreadsheet.append([int(i) for i in line.split()])

# Algorithm
checksum = 0
for line in spreadsheet:
    combinations = itertools.combinations(line, 2)
    for combination in combinations:
        first, second = 0, 1
        if combination[1] >= combination[0]:
            first, second = 1, 0

        q, m = divmod(combination[first], combination[second])
        if not m:
            checksum += q

print (checksum)
