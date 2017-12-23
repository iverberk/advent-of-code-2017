from collections import deque
from operator import add

directions = deque(['UP', 'RIGHT', 'DOWN', 'LEFT'])
moves = {
    'UP': (0, -1),
    'RIGHT': (1, 0),
    'DOWN': (0, 1),
    'LEFT': (-1, 0)
}

infected = set()

with open('map.in') as f:
    grid = [list(line.strip()) for line in f]
    mx, my = len(grid[0]) // 2, len(grid) // 2
    for y, row in enumerate(grid):
        for x, node in enumerate(row):
            if node == '#':
                infected.add((x-mx,y-my))

carrier = (0,0)
infections = 0
for _ in range(10000):
    if carrier in infected:
        directions.rotate(-1)
        infected.remove(carrier)
    else:
        directions.rotate(1)
        infected.add(carrier)
        infections += 1

    carrier = tuple(map(add, carrier, moves[directions[0]]))

print(infections)
