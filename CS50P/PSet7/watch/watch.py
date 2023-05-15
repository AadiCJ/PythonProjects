import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    linkExpression = "(?:https?://)?(?:www\.)?youtube.com/embed/([a-z0-9]+)"
    link = re.search(rf"src=\"{linkExpression}\"", s, re.IGNORECASE)
    if link is None:
        return None
    linkEnd = link.group(1)
    linkParsed = "https://youtu.be/" + linkEnd
    return linkParsed


if __name__ == "__main__":
    main()
