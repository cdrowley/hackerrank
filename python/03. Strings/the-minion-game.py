# https://www.hackerrank.com/challenges/the-minion-game/problem


def minion_game(string):
    VOWELS = "AEIOU"
    vows = 0
    cons = 0
    str_len = len(string)

    for idx in range(str_len):
        if string[idx] in VOWELS:
            vows += str_len - idx
        else:
            cons += str_len - idx

    if vows > cons:
        print(f"Kevin {vows}")
    elif vows < cons:
        print(f"Stuart {cons}")
    else:
        print("Draw")
