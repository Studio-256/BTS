def count(*a):
    s = 0
    res = []
    if len(a) > 1:
        for i in range(len(a) - 1):
            b = a[i + 1] - a[i]
            s += b
            res += b
    s /= len(a) + 1
    print('mean', s)

