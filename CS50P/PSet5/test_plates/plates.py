def main():
    plate = input("What is your plate? ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if not plate.isalnum():
        return False
    firstTwo = plate[:2]
    afterTwo = plate[2:]
    length = len(plate)
    remainingCheck = True
    digits = False
    for ch in afterTwo:
        if ch.isdigit():
            if not digits and int(ch) == 0:
                remainingCheck = False
                break
            digits = True
        elif ch.isalpha():
            if digits:
                remainingCheck = False
                break
        else:
            remainingCheck = False
            break
    return firstTwo.isalpha() and (2 <= length <= 6) and remainingCheck


if __name__ == "__main__":
    main()
