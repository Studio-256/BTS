from shesterenki.anorecsia import axe


import matplotlib.pyplot as plt

t, pd1, pd2, pd3 = [], [], [], []

CUR = pd2
if CUR is pd1:
    HILLS = 4
elif CUR is pd2:
    HILLS = 6
else:
    HILLS = 8
DRAW = False

f = open('data/result2.dat', 'r')

for i in f.readlines()[1:100000]:
    q, w, e, r = map(int, i.split())
    t.append(q)
    pd1.append(w)
    pd2.append(e)
    pd3.append(r)

prev = 0
uping = True
ch = []
cycle = []
hills = 0
for i in range(len(CUR) - 1):
    if uping and CUR[i] > 120:
        ch.append([t[i], t[i] - prev, 0])
        uping = not uping
        prev = t[i]
    elif not uping and CUR[i] < 80:
        ch.append([t[i], t[i] - prev, 1])
        hills += 1
        if hills == HILLS:
            hills = 0
            cycle.append(t[i])
        uping = not uping
        prev = t[i]
a = min(ch, key=lambda x: x[1])[1]
b = list(map(lambda x: x[1], filter(lambda x: x[1] < a * 1.2, ch)))
m = sum(b) / len(b)

for i in cycle:
    print(i)

if DRAW:
    plt.plot(t[:7000], pd1[:7000], 'r')
    plt.show()
    # plt.plot(cycle[:4], [100] * 4, 'yo')
    plt.plot(t[:7000], pd2[:7000], 'g')
    plt.show()
    plt.plot(t[:7000], pd3[:7000], 'b')
    plt.show()


# print(axe(9, 10070 - 2006, 14669 - 10070))
# print(axe(2, 10070 - 8793, 11231 - 10070))
# print()
# print(axe(622, 9614 - 2545, 13848 - 9614))
# print(axe(5, 9614 - 4249, 13216 - 9614))
# print(axe(2, 9614 - 7804, 11170 - 9614))
# print()
# print(axe(5, 9989 - 3014, 14258 - 9989))
# print(axe(2, 9989 - 7786, 11857 - 9989))

print()
print()
print()

print(axe(8, 10010 - 3334, 14177 - 10010))
print(axe(2, 10010 - 8722, 11171 - 10010))
print()
print(axe(6, 10328 - 4088, 14379 - 10328))
print(axe(2, 10328 - 8665, 11815 - 10328))
print()
print(axe(4, 9861 - 4743, 13388 - 9861))
print(axe(2, 9861 - 7624, 11744 - 9861))