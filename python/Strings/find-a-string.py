# https://www.hackerrank.com/challenges/find-a-string/problem


def count_substring(string, sub_string):
    return sum(
        [1 for i in range(len(string)) if sub_string == string[i : len(sub_string) + i]]
    )
