buffer = []
with open('stream.in') as f:
    buffer = f.read()

index = 0
inside_garbage = False
group_score = 1
total_score = 0
garbage_count = 0

while index < len(buffer):

    # Ignore characters after ! in garbage
    if inside_garbage and buffer[index] == '!':
        index += 2
        continue

    # Beginning of garbage
    if not inside_garbage and buffer[index] == '<':
        inside_garbage = True
        index += 1
        continue

    # End of garbage
    if inside_garbage and buffer[index] == '>':
        inside_garbage = False
        index += 1
        continue

    if inside_garbage:
        garbage_count += 1

    # Beginning of group
    if not inside_garbage and buffer[index] == '{':
        total_score += group_score
        group_score += 1

    # End of group
    if not inside_garbage and buffer[index] == '}':
        group_score -= 1

    index += 1

print(total_score, garbage_count)
