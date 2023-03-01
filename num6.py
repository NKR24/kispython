part_zero = [1967, 'LASSO', 1963, 1967]
part_one = [1967, 'LASSO', 1963, 1959]
part_two = [1967, 'LASSO', 1996, 1967]
part_three = [1967, 'LASSO', 1996, 1959]
part_four = [1967, 'LASSO', 1970]
part_six = [1967, 'OPAL', 1968, 1967]
part_seven = [1967, 'OPAL', 1968, 1959]
part_eight = [1967, 'OPAL', 1975]
part_nine = [1967, 'NU', 1967]
part_ten = [1967, 'NU', 1959]
part_eleven = [2011]
part_twelve = [1969]


def f1(x):
    if x[4] == 1959:
        return 9
    elif x[4] == 1967:
        return 8


def f2(x):
    if x[2] == 1975:
        return 7
    elif x[2] == 1968:
        if x[4] == 1959:
            return 6
        elif x[4] == 1967:
            return 5


def f3(x):
    if x[3] == 1970:
        return 4
    elif x[3] == 1996:
        if x[4] == 1959:
             return 3
        elif x[4] == 1967:
            return 2
    elif x[3] == 1963:
        if x[4] == 1959:
            return 1
        elif x[4] == 1967:
            return 0


def main(x):
    if x[1] == 1969:
        return 11
    elif x[1] == 2011:
        return 10
    elif x[1] == 1967:
        if x[0] == 'NU':
            return f1(x)
        elif x[0] == 'OPAL':
            return f2(x)
        elif x[0] == 'LASSO':
            return f3(x)
                
print (main(['OPAL', 1967, 1975, 1970, 1959]))
print (main(['LASSO', 1969, 1975, 1963, 1967]))
print (main(['NU', 2011, 1968, 1970, 1967]))
print (main(['LASSO', 1967, 1975, 1970, 1959]))
print (main(['OPAL', 1967, 1968, 1970, 1959]))
