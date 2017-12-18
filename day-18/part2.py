from concurrent.futures.thread import ThreadPoolExecutor
import queue
from collections import defaultdict

instructions = []
q0, q1 = queue.Queue(), queue.Queue()

with open('instructions.in') as f:
    for instruction in f:
        instruction =  instruction.split()
        operand = instruction[2] if len(instruction) == 3 else None
        instructions.append((instruction[0], instruction[1], operand))

# Get the register value or return the plain number
def get(operand, registers):
    try:
        return int(operand)
    except ValueError:
        return registers[operand]

def run(p, receive_q, send_q):
    registers = defaultdict(int)
    registers['p'] = p

    sends, position = 0, 0
    while 0 <= position < len(instructions):
        opcode, operand1, operand2 = instructions[position]

        # convert to number or find value in registers
        v1 = get(operand1, registers)
        if operand2:
            v2 = get(operand2, registers)

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
            send_q.put(v1)
            sends += 1
        elif opcode == 'rcv':
            try:
                registers[operand1] = receive_q.get(True, 0.1)
            except queue.Empty:
                break
        else:
            print("Invalid instruction found: {}".format(opcode))

        position += 1

    return sends

sends = 0
with ThreadPoolExecutor(max_workers=2) as executor:
    try:
        executor.submit(run, 0, q1, q0)
        sends = executor.submit(run, 1, q0, q1).result()
    except Exception as exc:
        print('Generated an exception: %s' % (exc))

print('Sends: {}'.format(sends))
