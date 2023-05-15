def main():
    inputStr = input(
        "What is the Answer to the Great Question of Life, the Universe and Everything? "
    )
    inputStr = inputStr.lower().strip()
    if inputStr == "42" or inputStr == "forty-two" or inputStr == "forty two":
        print("Yes")
    else:
        print("No")


main()
