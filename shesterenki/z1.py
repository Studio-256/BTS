import matplotlib.pyplot as plt

t, pd1, pd2, pd3 = [], [], [], []

CUR = pd1
DRAW = True

f = open('data/result.dat', 'r')

for i in f.readlines()[1:100000]:
    q, w, e, r = map(int, i.split())
    t.append(q)
    pd1.append(w)
    pd2.append(e)
    pd3.append(r)

prev = 0
uping = True
ch = []
for i in range(len(CUR) - 1):
    if uping and CUR[i] > 100:
        ch.append([t[i], t[i] - prev, 0])
        uping = not uping
        prev = t[i]
    elif not uping and CUR[i] < 96:
        ch.append([t[i], t[i] - prev, 1])
        uping = not uping
        prev = t[i]
a = min(ch, key=lambda x: x[1])[1]
b = list(map(lambda x: x[1], filter(lambda x: x[1] < a * 1.2, ch)))
m = sum(b) / len(b)

for i in ch:
    if round(i[1] / m) == 5 or False:
        print(i[0], round(i[1] / m) * str(i[2]), (i[0] - i[1]) / m, sep='\t\t')

if DRAW:
    plt.plot(t[:10000], pd1[:10000], 'r')
    plt.show()
    plt.plot(t[:10000], pd2[:10000], 'g')
    plt.show()
    plt.plot(t[:10000], pd3[:10000], 'b')
    plt.show()
