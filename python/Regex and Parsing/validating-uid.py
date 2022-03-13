# https://www.hackerrank.com/challenges/validating-uid/problem

import re


def validate_uid(
    uid: str, patterns: str = r"[A-Z]{2} [0-9]{3} ^[A-Z0-9a-z]{10}$ (.)\1"
):
    try:
        patterns = patterns.split()
        assert re.search(patterns[0], uid)
        assert re.search(patterns[1], uid)
        assert re.search(patterns[2], uid)
        assert not re.search(patterns[3], uid)
    except:
        return "Invalid"
    else:
        return "Valid"


uids_count = int(input())
uids = [print(validate_uid("".join(sorted(input())))) for _ in range(uids_count)]
