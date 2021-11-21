# Rock, Paper, Scissors Game

import random
import sys

print("ROCK, PAPER, SCISSORS")
W = 0
L = 0
T = 0

while True:
    score = str(W) + " Wins, " + str(L) + " Losses " + str(T) + " Ties"
    print(score)
    print()
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit.")
    oppoGame = input()
    game = ["ROCK", "PAPER", "SCISSORS"]
    myGame = random.choice(game)
    if oppoGame == "q":
        sys.exit()
    if oppoGame == "r" and myGame == "ROCK":
        print("ROCK versus....")
        print(myGame)
        print("It is a tie!")
        T = T + 1
        continue
    elif oppoGame == "r" and myGame == "PAPER":
        print("ROCK versus....")
        print(myGame)
        print("You lose!")
        L = L + 1
        continue
    elif oppoGame == "r" and myGame == "SCISSORS":
        print("ROCK versus....")
        print(myGame)
        print("You win!")
        W = W + 1
        continue
    if oppoGame == "p" and myGame == "ROCK":
        print("PAPER versus....")
        print(myGame)
        print("You win!")
        W = W + 1
        continue
    elif oppoGame == "p" and myGame == "PAPER":
        print("PAPER versus....")
        print(myGame)
        print("It is a tie!")
        T = T + 1
        continue
    elif oppoGame == "p" and myGame == "SCISSORS":
        print("PAPER versus....")
        print(myGame)
        print("You lose!")
        L = L + 1
        continue
    if oppoGame == "s" and myGame == "ROCK":
        print("SCISSORS versus....")
        print(myGame)
        print("You lose!")
        L = L + 1
        continue
    elif oppoGame == "s" and myGame == "PAPER":
        print("SCISSORS versus....")
        print(myGame)
        print("You win!")
        W = W + 1
        continue
    elif oppoGame == "s" and myGame == "SCISSORS":
        print("SCISSORS versus....")
        print(myGame)
        print("It is a tie!")
        T = T + 1
        continue
