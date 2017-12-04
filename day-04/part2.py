valid = 0
with open('passphrases.in') as f:
    for line in f:
        words = [''.join(sorted(word)) for word in line.split()]
        if len(words) == len(set(words)):
            valid += 1

print valid
