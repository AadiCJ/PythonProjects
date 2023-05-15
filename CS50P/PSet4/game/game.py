import random


def main():
    level = getInput("What is your level? ")
    secret = random.randint(1, level)
    guess = -1
    while guess != secret:
        guess = getInput("Guess: ")
        if guess > secret:
            print("Too large!")
        elif guess < secret:
            print("Too small!")
        else:
            print("Just right!")
            break


def getInput(message):
    inputted = -1
    while inputted < 1:
        try:
            inputted = int(input(message))
        except ValueError:
            pass
    return inputted


if __name__ == "__main__":
    main()
