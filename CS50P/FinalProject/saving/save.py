"""
Python script to handle saving and loading of game
"""
import csv
import sys

sys.path.insert(0, "../classes")
from player import Player

with open("saves.csv") as readFile:
    reader = csv.DictReader(readFile)
    lines = [row for row in reader]


def main(option, player1):
    if option == "save":
        save(player1)
    elif option == "load":
        print(load(player1.user))


def save(playerObj):
    data = playerObj.dictionary() # get dictionary from the player object
    headers = ["user","money","squirrel","dwarf","plant","robot","printer","goose","midas"]
    #headers
    
    found = False # is true if the user already exists
    for line in lines: 
        if line["user"] == data["user"]:
            line = data # replace the line, writing new data
            found = True
    if not found:
        lines.append(data) # add the new user

    with open("saves.csv", "w") as saveFile:
        writer = csv.DictWriter(saveFile, fieldnames=headers)
        writer.writeheader() # write headers as they are erased
        writer.writerows(lines) # write the new file
    
    #this solution is inefficient but i could not come up with a better solution


def load(username):
    # TODO: implement loading
    for line in lines:
        if line["user"] == username:
            return Player.make(line)


if __name__ == "__main__":
    main("load", Player("Doggo"))
