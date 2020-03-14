def axe(N, t1, t2):
    from math import pi
    return 4*pi*N*(t1-t2)/(t1*t2*(t1+t2))

print(axe(300, 1.7 , 1.7))