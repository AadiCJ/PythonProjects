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

HEIGHT = 900
WIDTH = 1200
FONT = ("Helvetica", 25, "bold")
RELIEF = "groove"
BD = 2

#since the actual increae can skyrocket, for each buyable, save D
#in the actual game code file. N is already stored in the player class
#price increase = current price + nth term of an ap


def main():
    launch()


def launch():
    global mainMenu 
    mainMenu = Tk()
        
    mainMenu.update_idletasks()
    
    
    mainMenu.geometry(f"{WIDTH}x{HEIGHT}+0+0")   
    
    newGame = Button(mainMenu, text="Start a new Game!", font=FONT, relief=RELIEF, bd=BD)
    newGame.place(x=(WIDTH/2-191), y=75)
    
    load = Button(mainMenu, text="Load a save?", font=FONT, relief=RELIEF, bd=BD, command=loadMenuLaunch)
    load.place(x=(WIDTH/2-138), y=200)

    mainMenu.resizable(False, False)
    mainMenu.mainloop()
        
        
def loadMenuLaunch():
    loadMenu = Toplevel(mainMenu)    
    loadMenu.config(width=WIDTH/2, height=HEIGHT/2)
    
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
        launchGame(p)


def launchGame(player):
    start(player)
    
    


if __name__ == "__main__":
    main()