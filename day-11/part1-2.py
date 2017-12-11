import operator

directions = {
    'n': (0, 1), 'ne': (1, 1), 'se': (1, 0),
    's': (0, -1), 'sw': (-1, -1), 'nw': (-1, 0)
}

def hex_distance(position):
    dx, dy = position[0], position[1]
    return max(abs(dx), abs(dy), abs(dy-dx))

position = (0,0)
max_distance = 0
with open('input.txt') as f:
    for move in f.readline().strip().split(','):
        position = tuple(map(operator.add, position, directions[move]))
        max_distance = max(max_distance, hex_distance(position))

print(hex_distance(position), max_distance)
