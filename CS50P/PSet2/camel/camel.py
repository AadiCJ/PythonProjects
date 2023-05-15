def main():
    varName = input("What is the name of your variable? ")
    out = ""
    for i in range(len(varName)):
        if varName[i].isupper():
            out += "_" + varName[i].lower()
        else:
            out += varName[i]

    print(out)


main()
