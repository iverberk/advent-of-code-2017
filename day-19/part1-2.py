maze = []
with open('maze.in') as f:
    for line in f:
        maze.append(list(line.rstrip('\n')))

UP, DOWN, LEFT, RIGHT = -1, 1, -1, 1
NORTH_EDGE, EAST_EDGE, SOUTH_EDGE, WEST_EDGE = -1, len(maze[0]), len(maze) - 1, -1
HORIZONTAL, VERTICAL = 0, 1

letters = []
direction = DOWN
orientation = VERTICAL
total_steps = 1

def X(point): x, y = point; return x
def Y(point): x, y = point; return y

def find_in_column(sx, sy, direction):
    edge = SOUTH_EDGE if direction == DOWN else NORTH_EDGE
    pos = (sx, sy)
    for y in range(sy + direction, edge, direction):
        if maze[y][sx].isalpha():
            letters.append(maze[y][sx])
            pos = (sx, y)
        if maze[y][sx] == '+':
            pos = (sx, y)
            break

    return pos, abs(sy - Y(pos))

def find_in_row(sx, sy, direction):
    edge = EAST_EDGE if direction == RIGHT else WEST_EDGE
    pos = (sx, sy)
    for x in range(sx + direction, edge, direction):
        if maze[sy][x].isalpha():
            letters.append(maze[sy][x])
            pos = (x, sy)
        if maze[sy][x] == '+':
            pos = (x, sy)
            break

    return pos, abs(sx - X(pos))

def find_direction(x, y):
    if maze[y][x+1] != ' ' and (direction != LEFT or orientation == VERTICAL):
        return HORIZONTAL, RIGHT
    elif maze[y][x-1] != ' ' and (direction != RIGHT or orientation == VERTICAL):
        return HORIZONTAL, LEFT
    elif maze[y+1][x] != ' ' and (direction != UP or orientation == HORIZONTAL):
        return VERTICAL, DOWN
    elif maze[y-1][x] != ' ' and (direction != DOWN or orientation == HORIZONTAL):
        return VERTICAL, UP
    else:
        return None, None

position = (maze[0].index('|'), 0)

while True:
    if orientation == VERTICAL:
        position, steps = find_in_column(X(position), Y(position), direction)
        total_steps += steps
        orientation, direction = find_direction(X(position), Y(position))
        if not direction:
            break

    if orientation == HORIZONTAL:
        position, steps = find_in_row(X(position), Y(position), direction)
        total_steps += steps
        orientation, direction = find_direction(X(position), Y(position))
        if not direction:
            break

print (''.join(letters), total_steps)
