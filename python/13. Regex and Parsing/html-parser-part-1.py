# https://www.hackerrank.com/challenges/html-parser-part-1/problem

from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        [print("-> {} > {}".format(*attr)) for attr in attrs]

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        [print("-> {} > {}".format(*attr)) for attr in attrs]


text = "\n".join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(text)
parser.close()
