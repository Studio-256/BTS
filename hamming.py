from math import log2


def hamming_encode(data: list):
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
    print(message)
    print(count)
    x //= 2
    while x >= 1:
        count.pop(x - 1)
        x //= 2
    print(count)


if __name__ == '__main__':

    c1 = [int(i) for i in '''0	
11	
0	
1	
0	
11	
00	
11111	
'''.replace('\n', '').replace('\t', '').replace(' ', '')]

    c2 = [int(i) for i in '''111	
    0	
    1	
    0	
    1	
    0000
    111	
    00	
    1	
    00	
    1	
    0	
    '''.replace('\n', '').replace('\t', '').replace(' ', '')]

    c3 = [int(i) for i in '''
    11		
0		
11		
0		
1		
00000	
1		
0		
1		
0		
1		
00		
111		
000		
11		
0			
    '''.replace('\n', '').replace('\t', '').replace(' ', '')]


    hamming_decode(c1)
    print()
    print()
    print()
    hamming_decode(list(reversed(c2)))
    print()
    print()
    hamming_decode(c3)
    print()
    hamming_decode(list(reversed(c3)))


    # hamming_decode([1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0])
