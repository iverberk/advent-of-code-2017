from operator import xor
from binascii import hexlify, unhexlify
from functools import reduce
from collections import deque

def rotate(l, n):
    return l[-n:] + l[:-n]

def knot_hash(key):
    lengths = [ord(n) for n in key]
    lengths.extend([17, 31, 73, 47, 23])

    sparse = list(range(256))
    p, s = 0, 0
    for _ in range(64):
        for length in lengths:
            sparse = rotate(sparse, -p)
            sparse[:length] = sparse[:length][::-1]
            sparse = rotate(sparse, p)
            p = (p + length + s) % 256
            s += 1

    return hexlify(bytearray([reduce(xor, sparse[i:i+16]) for i in range(0, 256, 16)]))

used = 0
grid = {}
for row in range(128):
    key = 'xlqgujun-{}'.format(row)
    bits = '{:0128b}'.format(int(knot_hash(key), 16))
    for index, bit in enumerate(bits):
        if int(bit): used += 1
        grid[(index, row)] = int(bit)

print("Used: {}".format(used))

# Reuse some Peter Norvig utility functions :-)

def X(point): x, y = point; return x
def Y(point): x, y = point; return y

def neighbors4(square):
    "The four neighboring squares."
    x, y = square
    return (          (x, y-1),
            (x-1, y),           (x+1, y),
                      (x, y+1))

seen = []
def bfs(square):
    queue = deque([square])
    region = 0
    while queue:
        square = queue.popleft()
        if square not in seen and grid[square]:
            region = 1
            seen.append(square)
            for neighbour in neighbors4(square):
                if 0 <= X(neighbour) < 128 and 0 <= Y(neighbour) < 128:
                    if neighbour not in seen and grid[neighbour]:
                        queue.extend([neighbour])

    return region

regions = 0
for y in range(128):
    for x in range(128):
        if (x,y) not in seen:
            regions += bfs((x,y))

print("Regions: {}".format(regions))
