import numpy as np

rules = []

with open('rules.in') as f:
    for rule in f:
        rule, enhancement = rule.strip().split(' => ')
        rules.append({
            'pattern': np.array([list(part) for part in rule.split('/')]),
            'enhancement': np.array([list(part) for part in enhancement.split('/')])
        })


def find_enhancement(pattern):
    patterns = [pattern] + [np.rot90(pattern, n) for n in range(1, 4)] + \
               [np.fliplr(pattern)] + [np.rot90(np.fliplr(pattern), n) for n in range(1, 4)]

    for pattern in patterns:
        for rule in rules:
            if np.array_equal(pattern, rule['pattern']):
                return rule['enhancement']

def enhance(art):
    s = art.shape[0]
    m = 2 if s % 2 == 0 else 3
    nm = m + 1
    ns = (s // m) * nm
    enhanced = np.zeros([ns, ns], dtype=str)
    for y in range(0, s // m):
        for x in range(0, s // m):
            xs, xe = x*nm, x*nm+nm
            ys, ye = y*nm, y*nm+nm
            enhanced[xs:xe, ys:ye] = find_enhancement(art[x*m:x*m+m, y*m:y*m+m])

    return enhanced

art = np.array([
    ['.', '#', '.'],
    ['.', '.', '#'],
    ['#', '#', '#']
])

for _ in range(0, 5):
    art = enhance(art)

print((art == '#').sum())

for _ in range(0, 13):
    art = enhance(art)

print((art == '#').sum())
