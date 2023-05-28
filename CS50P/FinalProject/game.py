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
from time import sleep
from threading import Thread

money = {
    "noteSingle": None,
    "noteStack": None,
    "singleNoteWaving": None
}





HEIGHT = 518
WIDTH = 900
IMAGE_WIDTH = 75
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
    global running
    running = True
    getResources()
    frameWork()  
    moneyLoop = Thread(target=makeMoney)
    moneyLoop.start()
    updateLoop = Thread(target=updates)
    updateLoop.start()
    game.mainloop()
    
    # TODO: Make all the labels and text variables.
    # TODO: Make the actual money making logic



"""Major methods start here"""
def frameWork():
    global statusBar
    statusBar = Label(game, text="", bd=1, relief=SUNKEN, anchor="e")

    global menubar
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
    
    
    menubar.add_cascade(label="Money")

    statusBar.pack(fill=X, side=BOTTOM, ipady=2)
    global statusText
    statusText = StringVar()
    statusBar.config(textvariable=statusText)
    statusText.set("Hello, Welcome")


    game.geometry(f"{WIDTH}x{HEIGHT}+0+0")
    game.title(f"{player.user}")

    # frames
    main = Frame(game, bg="red")

    clickerFrame = Frame(
        main, width=WIDTH / 3, height=round(2 * (HEIGHT / 3))
    )
    midasFrame = Frame(main, bg="yellow", width=WIDTH / 3, height=round(HEIGHT / 3))
    buyFrame = Frame(main, bg="green", width=WIDTH * 2 / 3, height=HEIGHT)
    buttonsBuyFrame = Frame(buyFrame, height=HEIGHT, width=WIDTH/3)
    buttonsAmountFrame = Frame(buyFrame, height=HEIGHT, width=WIDTH/3)
    

    # pack frames

    main.pack()
    clickerFrame.grid(column=0, row=0, rowspan=2, sticky=NW)
    clickerFrame.pack_propagate(0)
    midasFrame.grid(column=0, row=2, sticky=SW)
    midasFrame.pack_propagate(0)
    buyFrame.grid(column=1, row=0, columnspan=2, sticky=NE)
    buyFrame.pack_propagate(0)
    buttonsBuyFrame.pack(side="right")
    buttonsBuyFrame.pack_propagate(0)
    buttonsAmountFrame.pack(side="left")
    buttonsAmountFrame.pack_propagate(0)

    # Widgets
    clicker = Button(clickerFrame, image=money["noteStack"], command=clicked, relief=RELIEF)
    
    
    buyButtons = {
        Button(buttonsBuyFrame): "squirrel",
        Button(buttonsBuyFrame): "dwarf",
        Button(buttonsBuyFrame): "plant",
        Button(buttonsBuyFrame): "robot",
        Button(buttonsBuyFrame): "printer",
        Button(buttonsBuyFrame): "goose",
    }
    for button in buyButtons:
        button.config(text=buyButtons[button], font=FONT, width=WIDTH/3, height=IMAGE_WIDTH, image=buyable[buyButtons[button]][3], relief=RELIEF)
        button.bind("<Enter>", buttonEnter)
        button.bind("<Leave>", buttonExit)
        button.bind("<Button-1>", buyableClicked)
        button.pack(side=TOP)
    
    
    global amountLabels
    amountLabels = {
        "squirrel": [Label(buttonsAmountFrame), StringVar()],
        "dwarf": [Label(buttonsAmountFrame), StringVar()],
        "plant": [Label(buttonsAmountFrame), StringVar()],
        "robot": [Label(buttonsAmountFrame), StringVar()],
        "printer": [Label(buttonsAmountFrame), StringVar()],
        "goose": [Label(buttonsAmountFrame), StringVar()],
    }
    
    for key in amountLabels:
        label = amountLabels[key][0]
        label.config(textvariable=amountLabels[key][1], compound=RIGHT, image=empty, font=FONT, width=WIDTH/3, height=IMAGE_WIDTH, relief=RELIEF)
        label.pack(side=TOP)
    

    # pack widgets
    clicker.place(relx=0.5, rely=0.5, anchor=CENTER)
    

    game.protocol("WM_DELETE_WINDOW", saveAndExit) 
    game.resizable(False, False)
    
def makeMoney():
    totalAdd = 0
    while running:
        for key in buyable:
            totalAdd += player.dictionary()[key] * buyable[key][4]
        player.money += totalAdd*player.midas
        sleep(1)


def updates():
    while running:
        update()
        sleep(1)


"""Major methods end here"""


""" All loading methods start here """


def loading():
    loadMenu = Toplevel(game)
    loadMenu.config(width=WIDTH / 2, height=HEIGHT / 2)

    global label
    label = Label(loadMenu, font=FONT)
    label.place(x=69)

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
        label.config(text="Player not found")
        return

    if p:
        label.config(text="Player loaded.")
        game.destroy()
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
    global running
    running = False
    

def clicked():
    #TODO: Make money drop down when clicked. use the other two money sprites.
    player.money += 1
    update()
    
    
def buttonEnter(e):
    text = f"{buyable[e.widget.cget('text')][0]}, price: {buyable[e.widget.cget('text')][1]}"
    statusText.set(text)


def buttonExit(e):
    statusText.set("")
    

def buyableClicked(e):
    name = e.widget.cget('text')
    if(buying):
        price = buyable[name][1]
        if player.money >= price:
            addToPlayer(name)
            player.money-=price
            buyable[name][1] += buyable[name][2]
            update()
        else:
            statusText.set("Not enough money.")
                    
                
def addToPlayer(name):
    match(name):
        case "squirrel":
            player.squirrel+=buyAmount
        case "dwarf":
            player.dwarf+=buyAmount
        case "plant":
            player.plant+=buyAmount
        case "robot":
            player.robot+=buyAmount
        case "printer":
            player.printer+=buyAmount
        case "goose":
            player.goose+=buyAmount
        case "midas":
            player.midas*=2
            
            
def update():
    global menubar
    menubar.entryconfig(3, label=f"{player.money}")
    for key in amountLabels:
        textVar = amountLabels[key][1]
        match(key):
            case "squirrel":
                textVar.set(f"{player.squirrel}")
            case "dwarf":
                textVar.set(f"{player.dwarf}")
            case "plant":
                textVar.set(f"{player.plant}")
            case "robot":
                textVar.set(f"{player.robot}")
            case "printer":
                textVar.set(f"{player.printer}")
            case "goose":
                textVar.set(f"{player.goose}")
    

"""all game methods end here"""


""" methods to get resources start here """


def getResources():
    #this dict contains all necesarry information about the buyables.
    global buyable
    buyable = {
        "squirrel": ["Squirrels. Small, cheap and reliable.", 5+player.squirrel*10, 10, None, 1],
        "dwarf": ["Dwarves. they craft money out of rocks for you", 100+player.dwarf*200, 200, None, 5],
        "plant": ["Money plants. It's very leaves are money", 500+player.plant*1000, 1000, None, 100],
        "robot": ["Robots. Manual labour is quite effective.", 5000+player.robot*10000, 10000, None, 250],
        "printer": ["Printers. Prints money.", 100000+player.printer*200000, 200000, None, 5000],
        "goose": ["Geese. These geese lay very expensive golden eggs", 500000+player.goose*1000000, 1000000, None, 10000],
        "midas": ["For every midas you own, your money production doubles", 1000000+player.midas*2000000, 2000000, None, 0],
    }
    #The lists:
    #The 0th index has the description
    #the 1st index has => base price + amount of thing * increase per buy of thing.
    #the 2nd index has increase to base price per buy.
    #the 3rd index contains the image for the buyable.
    #the 4th index contains the money added per buyable
    
    for key in money:
        temp = ImageOps.fit(Image.open(rf"resources\money\{key}.png"), (IMAGE_WIDTH, IMAGE_WIDTH))
        money[key] = ImageTk.PhotoImage(temp)

    for key in buyable:
        temp = ImageOps.fit(Image.open(rf"resources\buyable\{key}.png"), (IMAGE_WIDTH, IMAGE_WIDTH))
        buyable[key][3] = ImageTk.PhotoImage(temp)
        
    global empty
    temp = ImageOps.fit(Image.open(rf"resources\empty\empty.png" ), (1, 1))
    empty = ImageTk.PhotoImage(temp)

"""methods to get resources end here"""


if __name__ == "__main__":
    try:
        start(load("debug"))
    except ValueError:
        start(Player("debug"))
