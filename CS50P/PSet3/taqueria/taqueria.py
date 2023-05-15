def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    order = []
    while True:
        try:
            latestItem = input("What is your order? ")
            if inIgnoreCase(menu, latestItem):
                order.append(latestItem)
                print(total(menu, order))
        except EOFError:
            break


def inIgnoreCase(menu, checkItem):
    for item in menu:
        if checkItem.lower() == item.lower():
            return True
    return False


def total(menu, order):
    totalCost = 0
    for item in order:
        totalCost += menu[item.title()]
    return f"Total: ${totalCost:.2f}"


main()
