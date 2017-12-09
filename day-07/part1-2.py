import re
from collections import namedtuple

nodes = {}
children = []

# Read towers
with open('towers.in') as f:
    for tower in f:
        subnodes= []
        match = re.match(r'([a-z]+) \((\d+)\) ?(?:->)? ?(.*)', tower)
        if match.group(3):
            subnodes = match.group(3).replace(' ', '').strip().split(',')

        children += subnodes
        nodes[match.group(1)] = {
            'weight': int(match.group(2)),
            'subnodes': subnodes,
            'parent': None
        }

root = None
for node in nodes.keys():
    if not node in children:
        root = node
        break

print ("Root of the tree: {}".format(root))

# Build flattened tree with DFS (non-recursive!! :-)
tree = []
stack = [root]
while stack:
    node = stack.pop()

    if nodes[node]['subnodes']:
        # Add parents
        for n in nodes[node]['subnodes']:
             nodes[n]['parent'] = node
        stack += nodes[node]['subnodes']

    tree.append(node)

# Walk the flattened tree backwards and add the weights to parents.
# Keep track of the weights added to the parents and detect an anomaly,
# this is the parent of the possible culprit.
weights = {}
p = None
while tree:
    node = tree.pop()

    if nodes[node]['parent']:
        parent = nodes[node]['parent']
        if parent in weights and nodes[node]['weight'] != weights[parent]:
            if not p:
                p = parent

        weights[parent] = nodes[node]['weight']
        nodes[parent]['weight'] += nodes[node]['weight']

# Print all possible culprits and leave for human interpretation :-)
for node in nodes[p]['subnodes']:
    print(node, nodes[node]['weight'])
