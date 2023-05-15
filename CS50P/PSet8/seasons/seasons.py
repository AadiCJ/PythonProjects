from datetime import date
import inflect
import sys


def main():
    dateGiven = getDate()
    print(findMinuteGap(dateGiven))


def findMinuteGap(dateObj):
    p = inflect.engine()
    today = date.today()
    try:
        dateInput = dateObj
    except ValueError:
        sys.exit("Year, month or day is out of bounds")

    dif = today - dateInput
    output = p.number_to_words(
        (round(dif.total_seconds() / 60)), andword=""
    ).capitalize()
    return output + " minutes"


def getDate():
    dateInput = input("Date of Birth: ")
    try:
        year, month, day = dateInput.split("-")
    except Exception:
        sys.exit("Invalid date")

    try:
        return date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
