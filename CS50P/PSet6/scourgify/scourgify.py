import csv
import sys


def main():
    if isValid(sys.argv):
        writeToNewFile(sys.argv[1], sys.argv[2])


def isValid(args):
    if(len(args) < 3):
        sys.exit("Too few command-line arguments")
    elif(len(args) > 3):
        sys.exit("Too many command-line arguments")

    if(not (args[1].endswith(".csv") and args[2].endswith(".csv"))):
        sys.exit("Provided files are not CSV's")

    return True


def writeToNewFile(oldFile, newFile):
    try:
        readFile = open(oldFile, newline = "")
        reader = csv.DictReader(readFile)
    except FileNotFoundError:
        sys.exit(f"Could not read from {oldFile}")

    fieldnames = ["first", "last", "house"]
    rows = list(reader)
    rowsChanged = []

    for row in rows:
        last, first = row["name"].split(",")
        house = row["house"]
        rowsChanged.append({fieldnames[0]: first.strip(), fieldnames[1]: last.strip(), fieldnames[2]: house})


    with open(newFile, "w") as writeFile:
        writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rowsChanged)





if __name__ == "__main__":
    main()
