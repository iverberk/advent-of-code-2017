instructions = []
steps = 0
position = 0

# Read instructions
with open('instructions.in') as f:
    for offset in f:
        instructions.append(int(offset))

while position >= 0 and position < len(instructions):
    previous_position = position
    position += instructions[position]
    instructions[previous_position] += 1
    steps += 1

print (steps)
