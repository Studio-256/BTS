#!/usr/bin/python3
from io import BytesIO


def converter(filein: BytesIO, fileout: BytesIO):
    blocksize = 3
    while True:
        s = filein.read(blocksize)
        if not s:
            break
        fileout.write(s)
        fileout.write(s)


a = open('testio/input.dat', 'rw')
