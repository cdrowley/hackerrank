# https://www.hackerrank.com/challenges/validating-credit-card-number/problem

import re

PATTERNS = [r"(^[4|5|6][0-9]{3}(-)?[0-9]{4}(-)?[0-9]{4}(-)?[0-9]{4}$)", r"(\d)\1{3,}"]


def valid_card(card, patterns=PATTERNS):
    if (
        re.findall(patterns[0], card) != []
        and re.findall(patterns[1], card.replace("-", "")) == []
    ):
        return "Valid"
    else:
        return "Invalid"


N = int(input())
[print(valid_card(input())) for _ in range(N)]
