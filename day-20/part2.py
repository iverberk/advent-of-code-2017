from operator import add
import re

particles = []
POSITION, VELOCITY, ACCELERATION = 0, 1, 2

with open('particles.in') as f:
    for index, particle in enumerate(f):
        m = re.match(r'p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>', particle)
        particles.append(
            [
                (int(m.group(1)), int(m.group(2)), int(m.group(3))),
                (int(m.group(4)), int(m.group(5)), int(m.group(6))),
                (int(m.group(7)), int(m.group(8)), int(m.group(9))),
            ]
        )

for _ in range(0, 1000):
    seen, duplicates = {}, []

    for index, particle in enumerate(particles):
        seen[particle[POSITION]] = index

        particles[index][VELOCITY] = tuple(map(add, particle[VELOCITY], particle[ACCELERATION]))
        particles[index][POSITION] = tuple(map(add, particle[POSITION], particle[VELOCITY]))

        if particles[index][POSITION] in seen:
            duplicates += [index, seen[particles[index][POSITION]]]
        else:
            seen[particles[index][POSITION]] = index

    for duplicate in sorted(list(set(duplicates)))[::-1]:
        del particles[duplicate]

print(len(particles))
