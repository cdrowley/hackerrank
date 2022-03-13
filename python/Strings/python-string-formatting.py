# https://www.hackerrank.com/challenges/python-string-formatting/problem


def print_formatted(number):
    for i in range(1, number + 1):
        pad = number.bit_length()
        print(f"{i:{pad}d} {i:{pad}o} {i:{pad}X} {i:{pad}b}")
