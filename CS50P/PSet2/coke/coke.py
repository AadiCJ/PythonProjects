def main():
    total = 50
    while total > 0:
        print("Amount Due:", total)
        coinGiven = int(input("Input coin"))
        if coinGiven == 25 or coinGiven == 10 or coinGiven == 5:
            total -= coinGiven

    print("Change Owed:", abs(total))


main()
