from collections import deque

programs = {}

with open('pipes.in') as f:
    for pipe in f:
        s, d = pipe.strip().split(' <-> ')
        programs[int(s)] = [int(d) for d in d.split(', ')]

seen = []

def bfs(node):
    queue = deque([node])
    while queue:
        node = queue.popleft()
        if node not in seen:
            seen.append(node)
            queue.extend(programs[node])

# Find group from the root node
bfs(0)
print(len(seen))

# We found the first group already
groups = 1

# Find the other groups
for program in programs.keys():
    if program not in seen:
        bfs(program)
        groups += 1

print(groups)
