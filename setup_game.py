#!/usr/bin/python3

# Import personal files
from menu.menu import Menu

# Variables
numberOfPlayers = 0

# Functions
def set_number_of_players():
    global numberOfPlayers
    incorrectValue = False

    # Get the user to input the number of players.
    try:
        numP = int(input('How many people are playing? '))
    except ValueError:
        print('Please select between 1 and 5 players.\n')
        return

    # Verify the chosen number is a valid amount.
    if numP < 1 or numP > 5:
        print('Please select between 1 and 5 players.\n')
        return

    # Set how many players will play.
    numberOfPlayers = numP

# Menu Setup
mainMenu = Menu()
mainMenu.options.append(set_number_of_players)

# Run the menu.
while (mainMenu):
    print('Number of Players: {}'.format(numberOfPlayers))
    mainMenu.getMenu()
