import matplotlib.pyplot as plt

f = open('data/result.dat', 'r')
t, pd1, pd2, pd3 = [], [], [], []

for i in f.readlines()[1:10000]:
    q, w, e, r = map(int, i.split())
    t.append(q)
    pd1.append(w)
    pd2.append(e)
    pd3.append(r)

prev = 0
uping = True
ch = []
for i in range(3600):
    if uping and pd2[i] > 150:
        ch.append([t[i] - prev, 0])
        uping = not uping
        prev = t[i]
    elif not uping and pd2[i] < 60:
        ch.append([t[i] - prev, 1])
        uping = not uping
        prev = t[i]
a = min(ch, key=lambda x: x[0])[0]
b = list(map(lambda x: x[0], filter(lambda x: x[0] < a * 1.2, ch)))
m = sum(b) / len(b)

for i in ch:
    print(round(i[0] / m) * str(i[1]))
# plt.plot(t[:1500], pd1[:1500], 'r')
# plt.show()
# plt.plot(t[:2700], pd2[:2700], 'g')
# plt.show()
# plt.plot(t[:3200], pd3[:3200], 'b')
# plt.show()
