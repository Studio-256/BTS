#!/usr/bin/python3
from io import BytesIO


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
        a = [filein.read(1) for i in range(2)]
        if not a[0] or not a[1]:
            break
        a = [[int(i) for i in bin(int.from_bytes(i, 'big'))[2:].rjust(8, '0')] for i in a]
        b = [hamming_encode(i) for i in a]
        b = [b[0][:8], b[0][8:] + b[1][:4], b[1][4:]]
        b = [int(''.join(map(str, i)), 2) for i in b]
        for i in b:
            fileout.write(i.to_bytes(1, 'big'))
