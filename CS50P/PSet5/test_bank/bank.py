def main():
    inputStr = input("Greeting: ")
    valueReturned = value(inputStr)
    print(f"${valueReturned}")


def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
