# Rock Paper Scissors is a hand game usually played between two people. In this game, scissors can beat paper, paper can beat rock, and rock beat
#scissors 

# To create and play rock paper scissors, I will be using the if and elif statements in python. I will prepare this game to be played between two
# players. Player -1 will be user, and Player-2 Will be the computer. Player one manually select the rock paper or scissor, while player 2 will 
# choose randomly. So I will also use the random module in python to create this game.

import random

player1 = input("Select Rock, Paper, or Scissor: ").lower()
player2 = random.choice(["Rock","Paper","Scissor"]).lower()

print("Player 2 Selected: ", player2)

if player1 == "rock" and player2 == "paper":
    print("Player 2 Won!")
elif player1 == "paper" and player2 =="scissor":
    print("Player 2 Won!")
elif player1 == "scissor" and player2 == "rock":
    print("Player 2 Won!")
elif player1 == player2:
    print("Tie")
else:
    print("Player 1 Won")
