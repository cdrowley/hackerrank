# https://www.hackerrank.com/challenges/alphabet-rangoli/problem


def print_rangoli(size):
    s = ""
    for i in range(size):
        s += chr(97 + i)

    for i in range(size - 1, -size, -1):
        line = s[: abs(i) : -1] + s[abs(i) :]
        print("-".join(line).center(4 * n - 3, "-"))
