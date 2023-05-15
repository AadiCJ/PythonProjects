#count lines of in py file except comments and empty lines

import sys

def main():
    if(len(sys.argv) < 2):
        sys.exit("Too few command-line arguments")
    elif(len(sys.argv) > 2):
        sys.exit("Too many command-line arguments")

    if(sys.argv[1].endswith(".py")):
        lines = countLines(sys.argv[1])
        print(lines)
    else:
        sys.exit("Not a Python file")


def countLines(fileName):
    lineCount = 0
    file = None
    try:
        file = open(fileName)
    except FileNotFoundError:
        sys.exit("File does not exist")


    if(file is not None):
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if(len(line) > 0 and not line.startswith("#")):
                lineCount += 1

    return lineCount


if __name__ == "__main__":
    main()