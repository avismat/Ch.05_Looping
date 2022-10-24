'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly chooses a 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.(1 for rock, 2 for paper, 3 for scissors and 4 for quit)
I don't want to be asked to quit each time. I will enter a 4 if I want to quit.
Add conditional statements to figure out who wins and keep the records
Each round tell me what the computer chose, what I chose and also if I won, lost or tied.
When the user quits print an end game message and their win/loss/tie record

'''

import random

def to_symbol(s):
    if s == 1:
        return "Rock"
    elif s == 2:
        return "Paper"
    elif s == 3:
        return "Scissors"
    else:
        return "Nothing"

def decide_winner(user,computer):
    # 0 if computer, 1 if user, -1 if neither

    # 2 Paper
    # 1 Rock

    if user == (computer % 3) + 1:
        return 1
    elif computer == (user % 3) + 1:
        return 0
    else:
        return -1

def main():
    print("Welcome to rock paper scissors!")

    userWins = 0
    computerWins = 0
    tiedWins = 0

    while True:
        userChoice = int(input("Rock (1) paper (2) or scissors (3)? Type 4 to quit."))
        computerChoice = random.randint(1,3)

        if userChoice == 4:
            print("Thanks for playing!\nHere were your stats:")
            print("Wins: {}\nLosses: {}\nTies: {}".format(userWins,computerWins,tiedWins))
            print("Win ratio: {}%".format(round((userWins/(userWins+computerWins+tiedWins)) * 100),4))
            break

        print("You chose {}".format(to_symbol(userChoice)))
        print("The computer chose {}".format(to_symbol(computerChoice)))

        winner = decide_winner(userChoice,computerChoice)

        if winner == 0:
            print("You lost! {} beats {}!".format(to_symbol(computerChoice), to_symbol(userChoice)))
            computerWins += 1
        elif winner == 1:
            print("You win! {} beats {}!".format(to_symbol(userChoice), to_symbol(computerChoice)))
            userWins += 1
        elif winner == -1:
            print("Tie!")
            tiedWins += 1

        print("--------------------------------")

    exit()

main()

