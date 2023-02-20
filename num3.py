import math


def main(n, m, a, z):
    sum = 0
    for c in range(1, a + 1):
        for i in range(1, m + 1):
            for k in range(1, n + 1):
                sum += 29 * (1 - 12 * k - z ** 3) ** 7 + c ** 6 / 50 + i ** 3
    return sum
