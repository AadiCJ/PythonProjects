from pyfiglet import Figlet
import sys
import random


def main():
    figlet = Figlet()
    if len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            font = sys.argv[2]
            if font in figlet.getFonts():
                figlet.setFont(font=font)
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
    elif len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font)
    else:
        sys.exit("Invalid usage")

    inputStr = input("What is your string? ")

    print(figlet.renderText(inputStr))


if __name__ == "__main__":
    main()
