a = 1
b, c = 84, 84
h = 0

if a:
    b = b * 100 + 100000
    c = b + 17000

def prime(n):
    if (n == 1): return False
    elif (n == 2): return True;
    else:
        for x in range(2, n):
            if n % x == 0: return False

    return True

for b in range(b, c + 1, 17):
    if not prime(b):
        h = h + 1

print(h)
