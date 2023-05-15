import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    expression = "(0|1?[0-9]{1,2}?|2[0-4][0-9]|25[0-5])"
    if re.fullmatch(rf"{expression}\.{expression}\.{expression}\.{expression}", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
