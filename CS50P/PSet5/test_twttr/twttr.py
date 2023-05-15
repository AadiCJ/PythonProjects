def main():
    str = input("Input your sentence: ")
    out = shorten(str)
    print(out)


def isNotVowel(ch):
    ch = ch.lower()
    return not (ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u")


def shorten(word):
    out = ""
    for ch in word:
        if isNotVowel(ch):
            out += ch
    return out


if __name__ == "__main__":
    main()
