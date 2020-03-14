#!/usr/bin/python3
from io import BytesIO


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
    if len(wrong) > 1 and sum(wrong) < len(count):
        count[sum(wrong) - 1] ^= 1
    x = x0
    while x >= 1:
        c = count.pop(x - 1)
        x //= 2

    return count


def converter(filein: BytesIO, fileout: BytesIO, filelog: BytesIO):
    times = []
    while True:
        entry = filelog.read(4)
        if not entry:
            break
        entry = int.from_bytes(entry, 'big')
        if len(times) > 0 and times[-1][1] != entry % 256:
            times.append((entry // 256, entry % 256))
        elif len(times) == 0:
            times.append((0, entry % 256))
    cur_t = 0
    data = []
    while True:
        time = filein.read(4)
        time = int.from_bytes(time, 'big')
        data = [filein.read(1) for i in range(4)]
        while cur_t + 1 < len(times) and time > times[cur_t + 1][0]:
            cur_t += 1
        a = [filein.read(1) for i in range(4)]
        for i in a:
            if not a:
                break
        a = [int.from_bytes(i, 'big') for i in a]
        for i in range(4):
            a[i] ^= times[cur_t]
        a = [[int(i) for i in bin(i)[2:].rjust(8, '0')] for i in a]
        data += a
        while len(data) >= 3:
            b = [data[0] + data[1][:4], data[1][4:] + data[2]]
            data = data[3:]
            b = [hamming_decode(i) for i in b]
            b = [int(''.join(map(str, i)), 2) for i in b]
            for i in b:
                fileout.write(i.to_bytes(1, 'big'))


converter(open('sas/buf.dat', 'rb'), open('sas/input.dat', 'wb'), open('track.txt', 'rb'))
