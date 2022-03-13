# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem


def average(array):
    s = set(array)
    return sum(s) / len(s)
