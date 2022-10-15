# https://www.hackerrank.com/challenges/swap-case/problem


def swap_case(s):
    swp = lambda l: l.upper() if l.islower() else l.lower()
    return "".join(list(map(swp, s)))
