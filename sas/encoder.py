#!/usr/bin/python3
from io import BytesIO
from random import random


tot = 0
ran = 0

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


def converter(filein: BytesIO, fileout: BytesIO):
    while True:
        # a = [filein.read(1)]
        # if not a[0]:
        #     break
        # a = [[int(i) for i in bin(int.from_bytes(i, 'big'))[2:].rjust(8, '0')] for i in a]
        # b = [a[0][:4], a[0][4:]]
        # b = [hamming_encode(i) for i in b]

        # a = [filein.read(1) for i in range(2)]
        # if not a[0] or not a[1]:
        #     break
        # a = [[int(i) for i in bin(int.from_bytes(i, 'big'))[2:].rjust(8, '0')] for i in a]
        # b = [hamming_encode(i) for i in a]
        # b = [b[0][:8], b[0][8:] + b[1][:4], b[1][4:]]

        a = [filein.read(1)]
        if not a[0]:
            break
        a = [[int(i) for i in bin(int.from_bytes(i, 'big'))[2:].rjust(8, '0')] for i in a]
        # b = [hamming_encode(i) for i in a]
        b = [a[0].copy() for i in range(3)]

        # Добавляем шум
        global tot, ran

        # x = 0
        # for i in range(12):
        #     b[i // 8][i % 8] ^= 1
        #     x += 1
        # if x > 1:
        #     print('aaaaa')

        for i in range(len(b)):
            x = 0
            tot += 1
            for j in range(len(b[i])):
                random1 = random()
                if random1 >= 0.942253:
                    x += 1
                    b[i][j] ^= 1
                    # print(i, j, random1)
            if x > 0:
                ran += 1
                print('aaaa')
        print()

        # b = [int(''.join(map(str, i + [0])), 2) for i in b]
        b = [int(''.join(map(str, i)), 2) for i in b]

        for i in b:
            fileout.write(i.to_bytes(1, 'big'))
    filein.close()
    fileout.close()


converter(open('input.dat', 'rb'), open('buf.dat', 'wb'))

print((tot - ran) / tot)
