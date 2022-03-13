# https://www.hackerrank.com/challenges/text-wrap/problem


def wrap(string, max_width):
    subs = [string[i : max_width + i] for i in range(len(string)) if i % max_width == 0]
    return "\n".join(subs)
