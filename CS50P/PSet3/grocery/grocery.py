def main():
    shoppingList = {}
    while True:
        try:
            newItem = input("").upper()  # check50 made me remove the prompt
            if newItem in shoppingList:
                count = int(shoppingList[newItem])
                shoppingList[newItem] = count + 1
            else:
                shoppingList[newItem] = 1
        except EOFError:
            printAll(shoppingList)
            break


def printAll(shoppingList):
    keys = list(shoppingList.keys())
    keys.sort()
    print()
    for key in keys:
        print(shoppingList[key], key)


main()
