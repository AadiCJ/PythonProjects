def main():
    plate = input("What is your plate? ").strip()
    if isValid(plate):
        print("Valid")
    else:
        print("Invalid")


def isValid(plate):
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


main()
