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
    bits = ''.join(['{:0>04b}'.format(int(d, 16)) for d in knot_hash(key)])
    for index, bit in enumerate(bits):
        if int(bit): used += 1
        grid[(index, row)] = int(bit)

print("Used: {}".format(used))

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
        if square not in seen and grid[square] == 1:
            region = 1
            seen.append(square)
            for neighbour in neighbors4(square):
                if neighbour not in seen and neighbour in grid and grid[neighbour] == 1:
                    queue.extend([neighbour])

    return region

regions = 0
for y in range(128):
    for x in range(128):
        if (x,y) not in seen:
            regions += bfs((x,y))

print("Regions: {}".format(regions))
