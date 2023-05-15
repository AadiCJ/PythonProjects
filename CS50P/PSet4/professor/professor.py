import random


def main():
    level = get_level()

    questions = 10
    correct = 0

    for i in range(questions):
        incorrectAttempt = 0
        x = generate_integer(level)
        y = generate_integer(level)
        while True:
            sum = x + y
            if incorrectAttempt == 3:
                print(f"{x} + {y} = {sum}")
                break
            inputtedInt = int(input(f"{x} + {y} = "))
            if inputtedInt == sum:
                correct += 1
                break
            else:
                print("EEE")
                incorrectAttempt += 1

    print(correct)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randrange(0, 10)
    elif level == 2:
        return random.randrange(10, 100)
    elif level == 3:
        return random.randrange(100, 1000)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
