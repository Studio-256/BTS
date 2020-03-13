a = open('data')
b = open('recieved')

entries = 0
errors = 0
while True:
    x, y = a.read(1), b.read(1)
    if not (x and y):
        break
    if x != y:
        errors += 1
print(errors / entries)
