def main():
    inputStr = input("Greeting: ")
    inputStr = inputStr.lower().strip()
    if inputStr.startswith("hello"):
        print("$0")
    elif inputStr.startswith("h"):
        print("$20")
    else:
        print("$100")


main()
