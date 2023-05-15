ddMax = 31  # max number of days in a month
mmMax = 12  # max number of months in a year
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    while True:
        dateGiven = input("What is your date? ")
        dateConverted = convert(dateGiven)
        if dateConverted is not None:
            print(dateConverted)
            break


def convert(date):
    if valid(date) == "W":
        return processWord(date)
    elif valid(date) == "N":
        return processNumbers(date)
    else:
        return None


def processWord(date):
    # for Month Day, Year format
    monthStr, day, year = date.replace(",", "").split()
    month = months.index(monthStr) + 1
    # get numberic value of month +1 as indexing starts at 0
    return f"{int(year):04d}-{int(month):02d}-{int(day):02d}"


def processNumbers(date):
    # for MM/DD/YYYY format
    month, day, year = date.split("/")
    return f"{int(year):04d}-{int(month):02d}-{int(day):02d}"


def valid(date):
    # check if given date is valid and return how to process
    if "/" in date:
        dateList = date.split("/")  # 0th pos = mm, 1st pos = dd
        try:
            if int(dateList[0]) <= mmMax and int(dateList[1]) <= ddMax:
                return "N"
        except Exception:
            return None
    elif "," in date:
        dateList = date.replace(",", "").split()
        if dateList[0] in months and int(dateList[1]) <= ddMax:
            return "W"
    else:
        return None


main()
