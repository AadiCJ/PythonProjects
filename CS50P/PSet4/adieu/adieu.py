import inflect


def main():
    engine = inflect.engine()
    wordList = []
    while True:
        try:
            wordIn = input("Input: ")
            wordList.append(wordIn)
        except EOFError:
            print(f"Adieu, adieu, to {engine.join(wordList)}")
            break


if __name__ == "__main__":
    main()
