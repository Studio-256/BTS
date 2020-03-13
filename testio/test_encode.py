from random import randint


def hamming_encode(data: list):
    data = data.copy()
    x = 1
    while x <= len(data):
        data.insert(x - 1, 0)
        x *= 2
    x = 1
    while x <= len(data):
        s = 0
        for i in range(x - 1, len(data), x * 2):
            for j in range(i, i + x):
                if j < len(data):
                    s += data[j]
        data[x - 1] = s % 2
        x *= 2
    return data


inp = open('input.dat', 'rb')
signal = open('buf.dat', 'wb')
for i in range(7):
    a = [[int(i) for i in bin(int.from_bytes(inp.read(1), 'big'))[2:].rjust(8, '0')] for i in range(2)]
    b = [hamming_encode(i) for i in a]
    b = [b[0][:8], b[0][8:] + b[1][:4], b[1][4:]]
    for i in range(randint(0, 2)):
        x, y = randint(0, 2), randint(0, 7)
        b[x][y] ^= 1
    b = [int(''.join(map(str, i)), 2) for i in b]
    for i in b:
        signal.write(i.to_bytes(1, 'big'))
inp.close()
signal.close()
