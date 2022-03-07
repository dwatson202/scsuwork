def xgcd(p,d):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while d != 0:
        q, p, d = p // d, d, p % d
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  (int(p), int(x0), int(y0))


print(xgcd(9,3))
