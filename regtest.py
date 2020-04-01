import re


def Main():
    line = "I think I understand regular expressions"

    mathResult = re.match('think', line, re.M | re.I)
    if matchResult:
        print("Match Found: " matchResult.group())
    else:
        print("No Match was Found")

    searchResult = re.search('think', line, re.M | re.I)
    if searchResult:
        print("Search Found: " searchResult.group())
    else:
        print("No Search was Found")


if __name__ = "__main__":
    Main()
