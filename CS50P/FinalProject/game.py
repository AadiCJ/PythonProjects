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
    menubar.add_cascade(label = "Game", menu=gameMenu)
    gameMenu.add_command(label="Save", command=lambda:save(player))
    gameMenu.add_command(label="Load", command=loading)
    gameMenu.add_cascade(label="Exit", command=saveAndExit)
    
    itemsMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Items", menu=itemsMenu)
    itemsMenu.add_command(label="Buy", command=setBuyMode)
    itemsMenu.add_command(label="Sell", command=setSellMode)
    
    
    statusBar.grid(column=1, row=3, sticky=(W, E))
    statusText = StringVar()
    statusBar.config(textvariable=statusText)
    statusText.set("Hello")
    
    
    
    
    
    
    
    #TODO: implement the frame
    game.geometry(f"{WIDTH}x{HEIGHT}+0+0")
    game.title(f"{player.user}")
    
    main = Frame(game)
    main.grid(column=0, row=0, sticky=(N, S, E, W))
    game.columnconfigure(0, weight=1)
    game.rowconfigure(0, weight=1)
    

    clickerFrame = Frame(main, bg="red", width=(WIDTH/3), height=(round(2*HEIGHT/3)))
    clicker = Button(clickerFrame, command=lambda:print("clicked"), image=money["noteStack"])
    #clicker.pack()
    clickerFrame.grid(column=0, row=0, rowspan=2, sticky="NW")
    
    
    
    midasFrame = Frame(main, bg="yellow", height=round(HEIGHT/3), width=round(WIDTH/3))
    midas = Button(midasFrame, command=lambda:print("midas"), image=buyable["midas"])
    #midas.pack()
    midasFrame.grid(column=0, row=2, sticky="SW")
    
    
    buyFrames = Frame(main, bg="green", width=(round(2*WIDTH/3)), height=HEIGHT)
    buyFrames.grid(column=1, row=0, columnspan=2, rowspan=3, sticky=(N, S, E))
    
    
    
    
    
    
    
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
    

"""all misc methods start here"""
def setBuyMode():
    buyMode = True

def setSellMode():
    buyMode = False
    
def saveAndExit():
    save(player)
    game.destroy()
"""all misc methods end here"""


""" methods to get resources start here """
def getResources():
    for key in money:
        temp = ImageOps.fit(Image.open(fr"resources\money\{key}.png"), (50, 50))
        money[key] = ImageTk.PhotoImage(temp)
    
    for key in buyable:
        temp = ImageOps.fit(Image.open(fr"resources\buyable\{key}.png"), (50, 50))
        buyable[key] = ImageTk.PhotoImage(temp)
"""methods to get resources end here"""
        
        

if __name__ == "__main__":
    start(Player("new player"))