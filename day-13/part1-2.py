layers = {}
max_depth = 0

with open("firewall.in") as f:
    for layer in f:
        d, r = [int(l) for l in layer.split(': ')]
        layers[d] = {
            'range': r,
            'interval': r*2-2
        }
        max_depth = max(max_depth, d)

def run(delay = 0, stop_when_caught = False):
    severity = 0
    depth = 0
    ps = delay
    caught = False
    while depth <= max_depth:
        if depth in layers and ps % (layers[depth]['interval']) == 0:
            caught = True
            if stop_when_caught:
                return caught, severity
            severity += depth * layers[depth]['range']
        depth += 1
        ps += 1

    return caught, severity

print(run(0, False))

delay = 1
while run(delay, True)[0]:
    delay += 1

print(delay)
