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
        a = [filein.read(1)]
        if not a[0]:
            break
        a = [[int(i) for i in bin(int.from_bytes(i, 'big'))[2:].rjust(8, '0')] for i in a]
        # b = [hamming_encode(i) for i in a]
        b = [a[0].copy() for i in range(3)]


        b = [int(''.join(map(str, i)), 2) for i in b]

        for i in b:
            fileout.write(i.to_bytes(1, 'big'))
    filein.close()
    fileout.close()


converter(open('input.dat', 'rb'), open('buf.dat', 'wb'))

# print((tot - ran) / tot)
б итии