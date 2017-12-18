from collections import defaultdict

registers = defaultdict(int)
instructions = []

with open('instructions.in') as f:
    for instruction in f:
        instruction =  instruction.split()
        operand = instruction[2] if len(instruction) == 3 else None
        instructions.append((instruction[0], instruction[1], operand))

# Get the register value or return the plain number
def get(operand):
    try:
        return int(operand)
    except ValueError:
        # converting to int failed, try to look it up in the registers
        return registers[operand]

position = 0
frequency = 0
while 0 <= position < len(instructions):
    opcode, operand1, operand2 = instructions[position]

    # convert to number or find value in registers
    v1 = get(operand1)
    if operand2:
        v2 = get(operand2)

    if opcode == 'set':
        registers[operand1] = v2
    elif opcode == 'mul':
        registers[operand1] = v1 * v2
    elif opcode == 'jgz':
        if v1 > 0:
            position += v2
            continue
    elif opcode == 'add':
        registers[operand1] = v1 + v2
    elif opcode == 'mod':
        registers[operand1] = v1 % v2
    elif opcode == 'snd':
        frequency = v1
    elif opcode == 'rcv':
        if v1 != 0:
            print(frequency)
            break
    else:
        print("Invalid instruction found: {}".format(opcode))

    position += 1
