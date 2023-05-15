import re


def main():
    print(convert(input("Hours: ")))


def convert(workingTimes):
    if "to" not in workingTimes:
        raise ValueError
    hoursRegex = "(?:[0-9]+)"
    minutesRegex = "(?::[0-9]+)?"
    allTimes = re.findall(f"({hoursRegex})({minutesRegex})? (AM|PM)", workingTimes)
    output = ""
    if len(allTimes) != 2:
        raise ValueError

    for i in range(len(allTimes)):
        time = allTimes[i]
        if len(time) != 3 or int(time[0]) > 12 or not time[0]:
            raise ValueError

        if i == 1:
            output += "to "  # add "to" to the output in the middle

        hours = int(time[0])
        minutes = 0
        if time[1]:
            minutes = int(time[1].replace(":", ""))
            if minutes > 59:
                raise ValueError

        if time[2] == "PM":
            output += parsePMTime(hours, minutes)
        elif time[2] == "AM":
            output += parseAMTime(hours, minutes)

    return output


def parsePMTime(hours, minutes):
    if hours != 12:
        hours += 12

    if minutes is not None:
        return f"{hours:02}:{minutes:02} "

    return f"{hours:02}:00 "


def parseAMTime(hours, minutes):
    if hours == 12:
        hours = 0

    if minutes is not None:
        return f"{hours:02}:{minutes:02} "

    return f"{hours:02}:00 "


if __name__ == "__main__":
    main()
