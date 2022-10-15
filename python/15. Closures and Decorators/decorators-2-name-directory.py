# https://www.hackerrank.com/challenges/decorators-2-name-directory/problem


def person_lister(func):
    def inner(people):
        return [func(person) for person in sorted(people, key=lambda age: int(age[2]))]

    return inner
