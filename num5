from math import atan

def main(y, x, z):
    res = 0
    n = len(y)
    for i in range(n):
        res += atan(y[i//4]**3 + z[n-1-i//2]/21 + 96 * x[i]**2)**7
    return '{:.2e}'.format(73*res)
