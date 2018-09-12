# This is just me messing around late at night.

import random

print("\nWelcome to Rock, Paper, Scissors!\n")
print("(Best 2 out of 3)\n")

gameover = False
your_score = 0
computer_score = 0

while not gameover:
    guess = input("Pick rock, paper, or scissors: ")

    if guess.upper() != "ROCK" and guess.upper() != "PAPER" and guess.upper() != "SCISSORS":
        print("\nYou must pick rock, paper, or scissors!\n")

    else:

        rand = random.randint(1, 3)

        # 1 = rock, 2 = paper, 3 = scissors

        # If you chose rock...
        if guess.upper() == "ROCK" and rand == 1:
            print("Tie!")

        elif guess.upper() == "ROCK" and rand == 2:
            print("Paper beats rock, YOU LOSE\n")
            computer_score += 1

        elif guess.upper() == "ROCK" and rand == 3:
            print("Rock beats scissors, YOU WIN\n")
            your_score += 1

        # If you chose paper...
        elif guess.upper() == "PAPER" and rand == 1:
            print("Paper beats rock, YOU WIN")
            your_score += 1

        elif guess.upper() == "PAPER" and rand == 2:
            print("Tie!")

        elif guess.upper() == "PAPER" and rand == 3:
            print("Scissors beats paper, YOU LOSE\n")
            computer_score += 1

        # If you chose scissors...
        elif guess.upper() == "SCISSORS" and rand == 1:
            print("Rock beats scissors, YOU LOSE")
            computer_score += 1

        elif guess.upper() == "SCISSORS" and rand == 2:
            print("Scissors beats paper, YOU WIN\n")
            your_score += 1

        elif guess.upper() == "SCISSORS" and rand == 3:
            print("Tie!")

        print("Computer's Score = %s" % computer_score)
        print ("Your Score = %s\n" % your_score)

        if computer_score == 3 or your_score == 3:
            print ("GAME OVER")
            gameover = True


## I'd like to go back and figure out how to maximize efficiency on this.