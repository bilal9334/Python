availableExists = ["north", "south", "east", "west"]

chosenExit = ""
while chosenExit not in availableExists:
    chosenExit = input("Please choose a direction: ")
    if chosenExit.casefold() == "quit":
        print("Game Over")
        break

else:
    print("aren't you glad you got out of there")
