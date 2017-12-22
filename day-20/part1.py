from operator import add
import re

particles = []
VELOCITY, ACCELERATION = 1, 2

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
    min_index = 0
    min_overall_velocity = abs(particles[0][VELOCITY][0]) + abs(particles[0][VELOCITY][1]) + abs(particles[0][VELOCITY][2])

    for index, particle in enumerate(particles):
        particle[VELOCITY] = tuple(map(add, particle[VELOCITY], particle[ACCELERATION]))
        particles[index] = particle

        min_velocity = abs(particle[VELOCITY][0]) + abs(particle[VELOCITY][1]) + abs(particle[VELOCITY][2])
        if min_velocity < min_overall_velocity:
            min_overall_velocity = min_velocity
            min_index = index

    print(min_index)
