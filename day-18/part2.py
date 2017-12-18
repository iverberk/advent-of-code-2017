import logging
from concurrent.futures.thread import ThreadPoolExecutor
import queue
from collections import defaultdict

logging.basicConfig(level=logging.INFO, format='%(threadName)s %(message)s')
logger = logging.getLogger('duet')

instructions = []
q0 = queue.Queue()
q1 = queue.Queue()

with open('instructions.in') as f:
    for instruction in f:
        instruction =  instruction.split()
        operand = None
        if len(instruction) == 3:
            operand = instruction[2]

        instructions.append((instruction[0], instruction[1], operand))

# Get the register value or return the plain number
def get(operand, registers):
    if not operand:
        return None
    try:
        return int(operand)
    except ValueError:
        return registers[operand]

def run(p, receive_q, send_q):
    registers = defaultdict(int)
    registers['p'] = p

    sends = 0
    position = 0
    while 0 <= position < len(instructions):
        opcode, operand1, operand2 = instructions[position]

        # convert to number or find value in registers
        operand2 = get(operand2, registers)

        if opcode == 'set':
            registers[operand1] = operand2
        elif opcode == 'mul':
            registers[operand1] = get(operand1, registers) * operand2
        elif opcode == 'jgz':
            if get(operand1, registers) > 0:
                position += operand2
                continue
        elif opcode == 'add':
            registers[operand1] = get(operand1, registers) + operand2
        elif opcode == 'mod':
            registers[operand1] = get(operand1, registers) % operand2
        elif opcode == 'snd':
            send_q.put(get(operand1, registers))
            sends += 1
        elif opcode == 'rcv':
            try:
                registers[operand1] = receive_q.get(True, 0.1)
            except queue.Empty:
                logger.info("Blocked waiting for data, terminating!")
                break
        else:
            logger.log("Invalid instruction found: {}".format(opcode))

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
