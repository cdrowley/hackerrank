# https://www.hackerrank.com/challenges/capitalize/problem


def solve(full_name):
    cap_name = " ".join(map(str.capitalize, full_name.split(" ")))
    return cap_name
