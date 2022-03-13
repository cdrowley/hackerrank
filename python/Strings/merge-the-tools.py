# https://www.hackerrank.com/challenges/merge-the-tools/problem


def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        y = ""
        for i in string[i : i + k]:
            if i not in y:
                y += i
        print(y)
