maximum = 0
registers = {}
operands = {
    '>': lambda r,v : r > v,
    '<': lambda r,v : r < v,
    '!=': lambda r,v : r != v,
    '>=': lambda r,v : r >= v,
    '<=': lambda r,v : r <= v,
    '==': lambda r,v : r == v,
    'inc': lambda r,v : r + v,
    'dec': lambda r,v : r - v
}

# Read instructions
with open('instructions.in') as f:
    for instruction in f:
        register1, operand1, value1, _, register2, operand2, value2 = instruction.strip().split()

        if operands[operand2](registers.get(register2, 0), int(value2)):
            registers[register1] = operands[operand1](registers.get(register1, 0), int(value1))
            maximum = max(maximum, registers[register1])

print ("Max register: {}, Max overall: {}".format(max(registers.values()), maximum))
