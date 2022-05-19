#!/usr/bin/env python3

"""
Play rock, paper, scissors against the PC in your terminal.
"""
import random


class Player:
    """
    One Player is user, another is pc
    
    1 - Rock
    2 - Paper
    3 - Scissors

    Attributes:
    name - user choose name in the beggining of the game, pc name is PC
    score - points from won games

    Methods:
    userAction - user choice is saved in userChoice
    pcAction - py chioce is saved in pcChoice
    """

    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    # Define what user chooses and print it
    def userAction(self):
        global userChoice
        while True:
            userChoice = input(f"{user.name} what is your choice?\n 1 - Rock\n 2 - Paper\n 3 - Scissors\n")
            # Incorrect input handling
            # Is the input a number?
            try:
                userChoice = int(userChoice)
                pass
            except:
                print("Please, type a number")
                continue
            # Is the input valid number?
            if 0 < userChoice < 4:
                break
            else:
                print("Please, type a valid nember")
                continue
        # Print what user chose
        if userChoice == 1:
            print("You chose rock!")
        elif userChoice == 2:
            print("You chose paper!")
        elif userChoice == 3:
            print("You chose scissors!")

    # Define what PC chooses
    def pcAction(self):
        global pcChoice
        # pc chooses by random module number 1, 2 or 3
        pcChoice = random.randint(1,3)

        if pcChoice == 1:
            print("PC chose rock!")
        elif pcChoice == 2:
            print("PC chose paper!")
        elif pcChoice == 3:
            print("PC chose scissors!")

    # Add 1 to Player.score
    def win(self):
        self.score += 1


# Define if play again after the end of the game
def playAgain():
    while True:
        again = input("Do you want to play again?\n 1 - Yes\n 2 - No\n")
        # Incorrect input handling
        # Is the input a number?
        try:
            again = int(again)
        except:
            print("Please, type a number")
            continue
        # Is the input valid number?
        if 0 < again < 3:
            break
        else:
            print("Please, type a valid number")
            continue

    return again

# Creat the user from Player class
user = Player(input("Hello! What is your name?\n"), 0)
# Creat the pc from Player class
pc = Player("PC", 0)

# The Game
while True:
    # User's round to choose
    user.userAction()
    # PC's round to choose
    pc.pcAction()

    # Logic of the game - who wins?
    if pcChoice == userChoice:
        print("It is a tie!\n")
    elif userChoice == 1: # Rock
        if pcChoice == 2: # Paper
            print("Paper covers rock! You lose!\n")
            pc.win()
        elif pcChoice == 3: # Scissors
            print("Rock beats scissors! You win!\n")
            user.win()
    elif userChoice == 2: # Paper
        if pcChoice == 1: # Rock
            print("Paper covers rock! You win!\n")
            user.win()
        elif pcChoice == 3: # Scissors
            print("Scissors cuts paper! You lose!\n")
            pc.win()
    elif userChoice == 3: # Scissors
        if pcChoice == 1: # Rock
            print("Rock beats scissors! You lose!\n")
            pc.win()
        elif pcChoice == 2: # Paper
            print("Scissors cuts paper! You win!\n")
            user.win()
    
    # Print the score
    print("Score is:")
    print(f"{user.name} = {user.score}")
    print(f"{pc.name} = {pc.score}\n")
    
    # Does the user want to play again?
    again = playAgain()
    if again == 1:
        continue
    elif again == 2:
        break