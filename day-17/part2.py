position = 0
steps = 382
after_zero = 0

for value in range(1, 50000000):
    position = 1 + (position + steps) % value
    if position == 1:
        after_zero = value

print(after_zero)
