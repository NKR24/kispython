import math

def main(z, y):
    a = ((((y + 67 + z ** 2) ** 5 + 1) / (29 * y ** 3 - (z ** 4 / 38))) ** 0.5) 
    b = (89 * (49 * z - 27 * y ** 3 - 97 * y ** 2) ** 6 - 91 * y ** 3) 
    c = (35 * z + 64 * y ** 2 + z ** 3) ** 7
    return a - (b / c)
