spinlock = [0]
position = 0
steps = 382

for value in range(1, 2018):
    position = 1 + (position + steps) % len(spinlock)
    spinlock.insert(position, value)

print(spinlock[spinlock.index(2017)+1])
