"""
The main menu.
TODO: Make the main menu GUI
TODO: Combine the saves system with the GUI
TODO: after loading/creating new game launch the game
"""
from tkinter import *


#since the actual increae can skyrocket, for each buyable, save D
#in the actual game code file. N is already stored in the player class
#price increase = current price + nth term of an ap





def main():
    launch()
    
    
def buttonEnter(e):
    text = f"Hovering over {e.widget.cget('text')}"
    statusBar.config(text=text)


def buttonExit(e):
    statusBar.config(text="")
    
    
    
    
def launch():
    mainMenu = Tk()
    global buttons
    buttons = {
        Button(mainMenu): "dwarf",
        Button(mainMenu): "robot",
        Button(mainMenu): "squirrel"
        
    }
    mainMenu.geometry("500x500+0+0")
    mainMenu.title("Main Menu")
        
    
    for key in buttons:
        key = Button(mainMenu, text=buttons[key], font=("Helvetica", 28, ""), pady=25)
        key.bind("<Enter>", buttonEnter)
        key.bind("<Leave>", buttonExit)
        key.pack()
        
    
    
    global statusBar
    
    statusBar = Label(mainMenu, text="", bd=1, relief=SUNKEN, anchor="e")
    statusBar.pack(fill=X, side=BOTTOM,  ipady=2)
    
    
    mainMenu.mainloop()
        
        

if __name__ == "__main__":
    main()