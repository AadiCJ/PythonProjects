import re


def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall(r"\b\W*um\b\W*", s, re.I))


if __name__ == "__main__":
    main()
