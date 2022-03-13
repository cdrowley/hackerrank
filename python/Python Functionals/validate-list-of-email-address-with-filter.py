# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem

import re


def fun(email):
    match = re.match("(^[a-zA-Z-_0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$)", email)
    return match is not None
