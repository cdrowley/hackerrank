# https://www.hackerrank.com/challenges/default-arguments/problem


def print_from_stream(n, stream=EvenStream()):
    stream.__init__()  # or set defualt to None | stream = stream or EvenStream()
    for _ in range(n):
        print(stream.get_next())
