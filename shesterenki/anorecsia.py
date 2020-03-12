def axe(N, t1, t2):
    t1 /= 500
    t2 /= 500
    from math import pi
    return 720 * N * (t1 - t2) / (t1 * t2 * (t1 + t2))
