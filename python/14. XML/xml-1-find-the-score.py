# https://www.hackerrank.com/challenges/xml-1-find-the-score/problem


def get_attr_number(node):
    return sum([len(n.items()) for n in node.iter()])
