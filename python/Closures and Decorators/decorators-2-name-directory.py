# https://www.hackerrank.com/challenges/decorators-2-name-directory/problem


def person_lister(f):
    def inner(people):
        return [f(person) for person in sorted(people, key=lambda age: int(age[2]))]

    return inner
