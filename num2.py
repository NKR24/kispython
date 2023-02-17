
import math


def main(z):

    if z < 82:
        return (92 * math.log(z)) - (92 * math.sin(z) ** 4) - 62
    elif z >= 82 and z < 94:
        return z
    elif z >= 94 and z < 114:
        return z ** 6 + 89 * z ** 4
    elif z >= 114 and z < 127:
        t = (26 * math.exp(1) ** 2) * (z ** 3 + 47 * z ** 2 + 1)
        h = (19 * ((z ** 2 - z) ** 5) - z ** 4)
        return t - h
    elif z >= 127:
        a = 43 * z - math.exp(1) ** 2
        b = 84 * z ** 2 - 28 * z - 67 * z ** 3
        c = 3 * z ** 8
        return a * b - c
