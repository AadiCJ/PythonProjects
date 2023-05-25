"""
The actual working game. 
#TODO: Implement the game frame
"""
from tkinter import *
from PIL import Image
from PIL import ImageOps
from PIL import ImageTk
from save import save
from save import load
from classes.player import Player

money = {
    "noteSingle": None,
    "noteStack": None,
    "singleNoteWaving": None,
}

buyable = {
    "dwarf": None,
    "goose": None,
    "midas": None,
    "plant": None,
    "printer": None,
    "robot": None,
    "squirrel": None,
}


HEIGHT = 518
WIDTH = 900
FONT = ("Helvetica", 25, "bold")
RELIEF = "groove"
BD = 2
buying = True
buyAmount = 1


def start(playerIn):
    global game
    game = Tk()
    global player
    player = playerIn
    getResources()

    statusBar = Label(game, text="", bd=1, relief=SUNKEN, anchor="e")

    menubar = Menu(game)
    game.config(menu=menubar)

    gameMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Game", menu=gameMenu)
    gameMenu.add_command(label="Save", command=lambda: save(player))
    gameMenu.add_command(label="Load", command=loading)
    gameMenu.add_cascade(label="Exit", command=saveAndExit)

    itemsMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Items", menu=itemsMenu)
    itemsMenu.add_command(label="Buy", command=setBuyMode)
    itemsMenu.add_command(label="Sell", command=setSellMode)

    statusBar.pack(fill=X, side=BOTTOM, ipady=2)
    statusText = StringVar()
    statusBar.config(textvariable=statusText)
    statusText.set("Hello, Welcome")

    # TODO: Make all the labels and text variables.
    # TODO: Make the clicker button
    # TODO: Make the actual money making logic

    game.geometry(f"{WIDTH}x{HEIGHT}+0+0")
    game.title(f"{player.user}")

    # frames
    main = Frame(game, bg="red")

    clickerFrame = Frame(
        main, bg="blue", width=WIDTH / 3, height=round(2 * (HEIGHT / 3))
    )
    midasFrame = Frame(main, bg="yellow", width=WIDTH / 3, height=round(HEIGHT / 3))
    buyFrame = Frame(main, bg="green", width=WIDTH * 2 / 3, height=HEIGHT)

    # pack frames

    main.pack()
    clickerFrame.grid(column=0, row=0, rowspan=2, sticky=NW)
    clickerFrame.pack_propagate(0)
    midasFrame.grid(column=0, row=2, sticky=SW)
    midasFrame.pack_propagate(0)
    buyFrame.grid(column=1, row=0, columnspan=2, sticky=NE)
    buyFrame.pack_propagate(0)

    # Widgets
    clicker = Button(clickerFrame, image=money["noteStack"], command=clicked)

    # pack widgets
    clicker.pack()

    game.resizable(False, False)
    game.mainloop()


""" All loading methods start here """


def loading():
    loadMenu = Toplevel(game)
    loadMenu.config(width=WIDTH / 2, height=HEIGHT / 2)

    global errLabel
    errLabel = Label(loadMenu, font=FONT)
    errLabel.place(x=69)

    global userName
    userName = Entry(loadMenu, font=FONT)
    userName.place(x=69, y=100)

    button = Button(loadMenu, text="Load!", font=FONT, command=callLoad)
    button.place(x=69, y=150)


def callLoad():
    user = userName.get()
    try:
        p = load(user)
    except ValueError:
        errLabel.config(text="Player not found")
        return

    if p:
        errLabel.config(text="Player loaded.\nYou may now close this")
        start(p)


""" all loading methods end here """


"""all game methods start here"""


def setBuyMode():
    buyMode = True


def setSellMode():
    buyMode = False


def saveAndExit():
    save(player)
    game.destroy()
    

def clicked():
    player.money += 1
    print(player.money)


"""all game methods end here"""


""" methods to get resources start here """


def getResources():
    for key in money:
        temp = ImageOps.fit(Image.open(rf"resources\money\{key}.png"), (50, 50))
        money[key] = ImageTk.PhotoImage(temp)

    for key in buyable:
        temp = ImageOps.fit(Image.open(rf"resources\buyable\{key}.png"), (50, 50))
        buyable[key] = ImageTk.PhotoImage(temp)


"""methods to get resources end here"""


if __name__ == "__main__":
    start(load("new player"))
