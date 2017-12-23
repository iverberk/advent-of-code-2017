from collections import deque
from operator import add
from enum import Enum

directions = deque(['UP', 'RIGHT', 'DOWN', 'LEFT'])
moves = {
    'UP': (0, -1),
    'RIGHT': (1, 0),
    'DOWN': (0, 1),
    'LEFT': (-1, 0)
}

State = Enum('State', ('WEAKENED', 'INFECTED', 'FLAGGED'))

nodes = {}

with open('map.in') as f:
    grid = [list(line.strip()) for line in f]
    mx, my = len(grid[0]) // 2, len(grid) // 2
    for y, row in enumerate(grid):
        for x, node in enumerate(row):
            if node == '#':
                nodes[(x-mx,y-my)] = State.INFECTED

carrier = (0,0)
infections = 0
for _ in range(10000000):
    if carrier in nodes:
        if nodes[carrier] == State.WEAKENED:
            nodes[carrier] = State.INFECTED
            infections += 1
        elif nodes[carrier] == State.INFECTED:
            nodes[carrier] = State.FLAGGED
            directions.rotate(-1)
        elif nodes[carrier] == State.FLAGGED:
            del nodes[carrier]
            directions.rotate(2)
    else:
        nodes[carrier] = State.WEAKENED
        directions.rotate(1)

    carrier = tuple(map(add, carrier, moves[directions[0]]))

print(infections)
