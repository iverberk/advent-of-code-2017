from enum import Enum
import sys

class Orientation(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

input = 347991
pos_x = 0
pos_y = 0
outer_ring = {}
inner_ring = { (0,0): 1 }

def calc_sum(pos_x, pos_y, orientation):
    sum = 0

    if orientation == Orientation.EAST:
        sum += inner_ring.get((pos_x-1, pos_y-1), 0)
        sum += inner_ring.get((pos_x-1, pos_y), 0)
        sum += inner_ring.get((pos_x-1, pos_y+1), 0)

        sum += outer_ring.get((pos_x, pos_y-1), 0)

    if orientation == Orientation.NORTH:
        sum += inner_ring.get((pos_x+1, pos_y-1), 0)
        sum += inner_ring.get((pos_x, pos_y-1), 0)
        sum += inner_ring.get((pos_x-1, pos_y-1), 0)

        sum += outer_ring.get((pos_x+1, pos_y), 0)
        sum += outer_ring.get((pos_x+1, pos_y-1), 0)
        sum += outer_ring.get((pos_x-1, pos_y-1), 0)

    if orientation == Orientation.WEST:
        sum += inner_ring.get((pos_x+1, pos_y+1), 0)
        sum += inner_ring.get((pos_x+1, pos_y), 0)
        sum += inner_ring.get((pos_x+1, pos_y-1), 0)

        sum += outer_ring.get((pos_x, pos_y+1), 0)
        sum += outer_ring.get((pos_x+1, pos_y+1), 0)

    if orientation == Orientation.SOUTH:
        sum += inner_ring.get((pos_x+1, pos_y+1), 0)
        sum += inner_ring.get((pos_x, pos_y+1), 0)
        sum += inner_ring.get((pos_x-1, pos_y+1), 0)

        sum += outer_ring.get((pos_x, pos_y+1), 0)
        sum += outer_ring.get((pos_x-1, pos_y), 0)
        sum += outer_ring.get((pos_x-1, pos_y+1), 0)
        sum += outer_ring.get((pos_x+1, pos_y+1), 0)

    if sum > input:
        print ("First value larger than input: {}".format(sum))
        sys.exit(0)

    return sum

for ring in range(1, 5):
    # First we move one the right to start the new ring
    pos_x += 1

    # Calculate the edge size
    edge_size = (ring * 2) + 1

    # Calculate first sum
    orientation = Orientation.EAST
    outer_ring[(pos_x, pos_y)] = calc_sum(pos_x, pos_y, orientation)

    # Fill the east edge
    for _ in range(0, edge_size-2):
        pos_y += 1
        outer_ring[(pos_x, pos_y)] = calc_sum(pos_x, pos_y, orientation)

    # Fill the north edge
    orientation = Orientation.NORTH
    for _ in range(0, edge_size-1):
        pos_x -= 1
        outer_ring[(pos_x, pos_y)] = calc_sum(pos_x, pos_y, orientation)

    # Fill the west edge
    orientation = Orientation.WEST
    for _ in range(0, edge_size-1):
        pos_y -= 1
        outer_ring[(pos_x, pos_y)] = calc_sum(pos_x, pos_y, orientation)

    # Fill the south edge
    orientation = Orientation.SOUTH
    for _ in range(0, edge_size-1):
        pos_x += 1
        outer_ring[(pos_x, pos_y)] = calc_sum(pos_x, pos_y, orientation)

    # Save the outer ring, it is now our new inner ring
    # Clear the outer ring, since we will build it again
    inner_ring = outer_ring
    outer_ring = {}
