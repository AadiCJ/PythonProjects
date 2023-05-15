def main():
    time = convert(input("What is the time? "))
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    hour, rest = time.split(":")
    add = 0
    hour = int(hour)
    minute = int(rest.split()[0])  # assignments

    if rest.endswith("p.m.") and hour != 12:
        add = 12  # eg. 1pm = 13, 12pm = 12, 5pm = 17 etc

    decimalMinute = minute / 60
    return hour + decimalMinute + add  # returning


if __name__ == "__main__":
    main()
