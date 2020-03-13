from hamming import hamming_encode

# a = hamming_encode([int(i) for i in '10011001010000001011011'])
a = hamming_encode([0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0])
print(a)