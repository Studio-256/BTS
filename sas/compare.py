total = 0
right = 0

a = open('input.dat', 'rb')
b = open('_input.dat', 'rb')

print()
print()
while True:
    x = a.read(1)
    y = b.read(1)
    if not x:
        break
    total += 1
    if x == y:
        right += 1
print(right / total)