from math import ceil, sqrt, floor

input = 347991

distance = 0

if input > 1:
    # Determine the ring of the memory location
    ring = ceil((sqrt(input) - 1) / 2)

    # Find the start of the ring's memory locations
    start = ((1 + (ring - 1) * 2) ** 2)

    # Determine the edge where the memory location is (0,1,2 or 3)
    edge = floor((input - start) / (2 * ring))

    # Determine the middle of the edge
    middle = start + ring + edge * (2 * ring)

    # Now calculate the distance by adding the ring distance and distance from
    # the middle of the edge
    distance = ring + abs(input - middle)

print (distance)
