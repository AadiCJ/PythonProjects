import validators


def main():
    str = input("Email: ")
    if validators.email(str):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
