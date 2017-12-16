dances = []
with open('dances.in') as f:
    dances = f.readline().strip().split(',')

def dance(rounds):
    programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    for _ in range(rounds%48):
        for dance in dances:
            if dance[0] == 's':
                p = int(dance[1:])
                programs = programs[-p:] + programs[:-p]
            elif dance[0] == 'x':
                p1, p2 = [int(p) for p in dance[1:].split('/')]
                programs[p1], programs[p2] = programs[p2], programs[p1]
            elif dance[0] == 'p':
                for i,p in enumerate(programs):
                    if p == dance[1]: p1 = i
                    if p == dance[3]: p2 = i
                programs[p1], programs[p2] = programs[p2], programs[p1]

    return ''.join(programs)

print(dance(1))
print(dance(1000000000))
