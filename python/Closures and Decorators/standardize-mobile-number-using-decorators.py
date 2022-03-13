# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem


def wrapper(f):
    def fun(UI):
        f("+91 " + i[-10:-5] + " " + i[-5:] for i in UI)

    return fun
