from numpy import argmax

with open('memory.in') as f:
    banks = [int(bank) for bank in f.readline().split()]

num_banks = len(banks)

def rebalance(banks):
    seen = set()
    seen.add(tuple(banks))
    cycle = 0

    while True:
        cycle += 1
        bank = argmax(banks)
        blocks = banks[bank]
        banks[bank] = 0

        while blocks > 0:
            bank += 1
            banks[bank % num_banks] += 1
            blocks -= 1

        t = tuple(banks)
        if t in seen:
            break
        else:
            seen.add(t)

    return cycle, banks

cycle, banks = rebalance(banks)
print("Duplicate found at cycle: {}".format(cycle))

cycle, _ = rebalance(banks)
print("Loop after cycle: {}".format(cycle))
