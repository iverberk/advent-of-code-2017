MOD = 2147483647
MASK = (1 << 16) - 1;

def generator_A(seed):
    product = (seed * 16807) % MOD
    while True:
        yield product
        product = (product * 16807) % MOD

def generator_B(seed):
    product = (seed * 48271) % MOD
    while True:
        yield product
        product = (product * 48271) % MOD

matches = 0
A = generator_A(512)
B = generator_B(191)
for _ in range(40000000):
    if ((next(A) & MASK) == (next(B) & MASK)): matches += 1

print(matches)
