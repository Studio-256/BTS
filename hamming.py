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


if __name__ == '__main__':
    print(hamming_encode([1, 0, 1, 1, 0]))
hamming_decode([1, 0, 1, 0, 0, 1, 1, 0, 0])
