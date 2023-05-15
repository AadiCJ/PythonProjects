import emoji


def main():
    inputStr = input("Input your string: ")
    print(emoji.emojize(inputStr, language="alias"))


if __name__ == "__main__":
    main()
