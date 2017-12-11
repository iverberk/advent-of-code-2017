CLIST_LEN = 256

def rotate(l, n):
    return l[-n:] + l[:-n]

def hash(clist, lengths, cpos = 0, skip_size = 0):
    for length in lengths:
        clist = rotate(clist, -cpos)
        sublist = clist[:length]
        clist[:length] = sublist[::-1]
        clist = rotate(clist, cpos)
        cpos = (cpos + length + skip_size) % CLIST_LEN
        skip_size += 1

    return clist, cpos, skip_size

with open('lengths.in') as f:
    input = f.readline().strip()
    clist, _, _ = hash(
        list(range(0, CLIST_LEN)),
        map(int,input.split(','))
    )

    print(clist[0]*clist[1])

    lengths = map(ord, list(input))
    lengths += [17, 31, 73, 47, 23]

    sparse_hash = list(range(0, CLIST_LEN))
    cpos, skip_size = 0, 0
    for _ in range(0, 64):
        sparse_hash, cpos, skip_size = hash(sparse_hash, lengths, cpos, skip_size)

    dense_hash = ""
    for i in range(0, 256, 16):
        number = 0
        for element in sparse_hash[i:i+16]:
            number ^= element
        dense_hash += '{0:02x}'.format(number)

    print(dense_hash)
