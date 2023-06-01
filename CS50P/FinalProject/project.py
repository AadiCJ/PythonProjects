"""
The main menu.
TODO: Make the main menu GUI
TODO: Combine the saves system with the GUI
TODO: after loading/creating new game launch the game
"""
from tkinter import *
from classes.player import Player
from save import load
from game import start

HEIGHT = 518
WIDTH = 900
FONT = ("Helvetica", 25, "bold")
RELIEF = "groove"
BD = 2

# new price = current price + a fixed increase


def main():
    launch()


def launch():
    global mainMenu
    mainMenu = Tk()

    mainMenu.update_idletasks()

    mainMenu.geometry(f"{WIDTH}x{HEIGHT}+0+0")
    mainMenu.title("Main Menu")

    newGame = Button(
        mainMenu,
        text="Start a new Game!",
        font=FONT,
        relief=RELIEF,
        bd=BD,
        command=newGameMenu,
    )
    newGame.place(x=(WIDTH / 2 - 180), y=75)

    load = Button(
        mainMenu,
        text="Load a save?",
        font=FONT,
        relief=RELIEF,
        bd=BD,
        command=loadMenuLaunch,
    )
    load.place(x=(WIDTH / 2 - 138), y=200)

    exitButton = Button(
        mainMenu,
        text="Exit",
        font=FONT,
        relief=RELIEF,
        command=lambda: mainMenu.destroy(),
    )
    exitButton.place(x=(WIDTH / 2) - 70, y=325)

    mainMenu.resizable(False, False)
    mainMenu.mainloop()


def newGameMenu():
    newGame = Toplevel(mainMenu)
    newGame.geometry(f"{round(WIDTH/2)}x{round(HEIGHT/2)}+0+0")

    global label
    label = Label(newGame, font=FONT)
    label.place(x=55)

    global userName
    userName = Entry(newGame, font=FONT)
    userName.place(x=55, y=50)

    button = Button(newGame, text="Begin!", font=FONT, command=callStart)
    button.place(x=55, y=100)


def callStart():
    user = userName.get()
    try:
        p = load(user)
    except ValueError:
        label.config(text="Starting!")
        launchGame(Player(user))
    else:
        label.config(text="Player exists. Try loading instead")


def loadMenuLaunch():
    loadMenu = Toplevel(mainMenu)
    loadMenu.geometry(f"{round(WIDTH/2)}x{round(HEIGHT/2)}+0+0")

    global label
    label = Label(loadMenu, font=FONT)
    label.place(x=55)

    global userName
    userName = Entry(loadMenu, font=FONT)
    userName.place(x=55, y=50)

    button = Button(loadMenu, text="Load!", font=FONT, command=callLoad)
    button.place(x=55, y=100)


def callLoad():
    user = userName.get()
    try:
        p = load(user)
    except ValueError:
        label.config(text="Player not found")
        return

    if p:
        label.config(text="Player loaded.")
        launchGame(p)


def launchGame(player):
    mainMenu.destroy()
    start(player)


if __name__ == "__main__":
    main()
