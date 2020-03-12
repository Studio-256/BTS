from math import sqrt


def count(*a):
    s = 0
    res = []
    if len(a) > 1:
        for i in range(len(a) - 1):
            b = a[i + 1] - a[i]
            s += b
            res.append(b)
    s /= len(a) - 1
    print('mean', s * 2)
    d = 0
    for i in res:
        d += (i - s) ** 2
    d /= len(res)
    print('error', sqrt(d))


count(1117,2078,3035,3990,4950,5911,6868,7823,8781,9745,10700,11656,12614,13575,14535)
print()
# count(370,1630,2880,4163,5425,6674,7955,9221,10468,11745,13014,14265)
# print()
# count(985,2570,4141,5700,7288,8852,10415,12003,13561)
# print()
count(365,1627,2877,4158,5422,6671,7952,9217,10465,11742,13010,14262)
print()
count(980,2565,4136,5696,7284,8847,10411,11998,13556)
print()
