def main():
    str = input("Input your sentence: ")
    out = ""
    for ch in str:
        if isNotVowel(ch):
            out += ch
    print(out)


def isNotVowel(ch):
    ch = ch.lower()
    return not (ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u")


main()
