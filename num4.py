import math


def main(n):
    if n == 0:
        return 0.72
    elif n == 1:
        return -0.78
    elif n >= 2:
        return main(n-1) + 67 + abs(main(n-2))**2

