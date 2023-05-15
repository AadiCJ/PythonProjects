#!/usr/bin/env python

"""sorter.py:
Sorts a given csv file based on a header provided by the user and outputs it to a new file.
"""
__author__ = "Aadi Jha"

import csv
import sys


def main():
    inFile = input("Input file name: ")
    outFile = input("Output file name: ")
    global sortBy  # set to global for later use
    sortBy = input("Input the header to sort by: ")
    # get user input

    if inFile.endswith(".csv") and outFile.endswith(".csv"):
        sort(inFile, outFile)
    else:
        print("Not csv files")  # exit if files are not csv files
        input()  # to halt program
        sys.exit(1)


def sort(inFile, outFile):
    try:
        with open(inFile) as headerGetter:
            headers = next(csv.reader(headerGetter))
            # get headers from the file to use later
    except FileNotFoundError:
        print(f"{inFile} not found")
        input()  # to halt program
        sys.exit(1)
        # exit if inFile not found

    with open(inFile) as readFile:
        reader = csv.DictReader(readFile)
        lines = []  # list for total lines
        # this is veeeryyyyy memory inefficient but it works
        for line in reader:
            lines.append(line)  # add all the lines to the file
        try:
            sortedList = sorted(lines, key=lambda dict: dict[sortBy], reverse=True)
        except KeyError:
            print("Required column name/dict key not found")
            input()  # to halt program
            sys.exit(1)
        # use the inbuilt sorted function to sort using getAvg as key
    with open(outFile, "w") as writeFile:
        writer = csv.DictWriter(writeFile, fieldnames=headers)
        try:
            writer.writeheader()  # write headers
            writer.writerows(sortedList)
        except:
            print("Error while writing file contact ACJ")
            input()  # to halt program
            sys.exit(1)
            # i dont know what all errors this can raise


if __name__ == "__main__":
    main()  # call main only if running from main thread
