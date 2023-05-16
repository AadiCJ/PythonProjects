"""
The main menu.
TODO: Make the main menu GUI
TODO: Combine the saves system with the GUI
TODO: after loading/creating new game launch the game
"""
from tkinter import *
from classes.player import Player
from save import load

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
    
    load = Button(mainMenu, text="Load a save?", font=FONT, relief=RELIEF, bd=BD, command=callLoad)
    load.place(x=(WIDTH/2-138), y=200)
    
    

    
    mainMenu.resizable(False, False)
    mainMenu.mainloop()
        
        
def callLoad():
    loadMenu = Toplevel(mainMenu)    
    loadMenu.config(width=WIDTH/2, height=HEIGHT/2)
    
    userName = Entry(loadMenu, font=FONT)
    userName.place(x=69, y=100)
    
    button = Button(loadMenu, text="Load!", font=FONT)
    button.place(x=69, y=150)
    


if __name__ == "__main__":
    main()