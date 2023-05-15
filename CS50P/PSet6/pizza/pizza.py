import csv
from tabulate import tabulate
import sys

def main():
    if(len(sys.argv) > 2):
        sys.exit("Too many command-line arguments")
    elif(len(sys.argv) < 2):
        sys.exit("Too few command-line arguments")

    if(sys.argv[1].endswith(".csv")):
        makeTable(sys.argv[1])
    else:
        sys.exit("Not a CSV file")


def makeTable(filePath):
    file = None
    try:
        file = open(filePath, newline = "")
    except FileNotFoundError:
        sys.exit("File not found")

    reader = csv.DictReader(file)
    print(tabulate(reader, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()