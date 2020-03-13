def hamming_decode(message: list):
    count = message.copy()
    x = 1
    while x <= len(count):
        count[x - 1] = 0
        x *= 2
    x = 1
    while x <= len(count):
        s = 0
        for i in range(x - 1, len(count), x * 2):
            for j in range(i, i + x):
                if j < len(count):
                    s += count[j]
        count[x - 1] = s % 2
        x *= 2
    x //= 2
    x0 = x
    wrong = []
    while x >= 1:
        if message[x - 1] != count[x - 1]:
            wrong.append(x)
        x //= 2
    if len(wrong) > 1:
        count[sum(wrong) - 1] ^= 1
    x = x0
    while x >= 1:
        c = count.pop(x - 1)
        x //= 2

    return count

signal = open('buf.dat', 'rb')
a = [[int(i) for i in bin(int.from_bytes(signal.read(1), 'big'))[2:].rjust(8, '0')] for i in range(3)]
b = [a[0] + a[1][:4], a[1][4:] + a[2]]
b = [hamming_decode(i) for i in b]
b = [int(''.join(map(str, i)), 2) for i in b]

out = open('_input.dat', 'wb')
for i in b:
    out.write(i.to_bytes(1, 'big'))
signal.close()
