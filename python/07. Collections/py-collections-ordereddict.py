# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

ordered_dictionary = OrderedDict()

for _ in range(int(input())):
    UI = input().split()
    item_name = " ".join(UI[:-1])
    net_price = int(UI[-1])

    ordered_dictionary.setdefault(item_name, 0)
    ordered_dictionary[item_name] += net_price

[print(k, v) for k, v in ordered_dictionary.items()]
