import random

def ropasc():
    print(" Game rules :\n (a) This Game require 2 players. It is a game of chance that depends on random luck similar to flipping coins.\n (b) The game is played with three possible signals that represent a rock, paper, and scissors.\n (c) Winning Criteria: Rock wins against scissors; paper wins against rock; and scissors wins against paper. If both players choose same, it is considered a tie.")

    L = ['Rock', 'Paper', 'Scissors']
    computer = random.choice(L)
    user = input('Enter either Rock or Paper or Scissors : ')
    print("computer choice is:", computer)
    print("Your choice is: ", user)
   
    if user == "Rock" or user == "rock" or user == "ROCK" and computer == "Rock":
        print("The Game is Tie.")

    elif user == "Rock" or user == "rock" or user == "ROCK" and computer == "Paper":
        print("You Loss")

    elif user == "Rock" or user == "rock" or user == "ROCK" and computer == "Scissors":
        print("You Win")

    elif user == "Paper" or user == "paper" or user == "PAPER" and computer == "Paper":
        print("The Game is Tie.")

    elif user == "Paper" or user == "paper" or user == "PAPER" and computer == "Rock":
        print("You Win.")

    elif user == "Paper" or user == "paper" or user == "PAPER" and computer == "Scissors":
        print("You Loss.")

    elif user == "Scissors" or user == "scissors" or user == "SCISSORS" and computer == "Scissors":
        print("The Game is Tie.")

    elif user == "Scissors" or user == "scissors" or user == "SCISSORS" and computer == "Rock":
        print("You Loss.")

    elif user == "Scissors" or user == "scissors" or user == "SCISSORS" and computer == "Paper":
        print("You win.")

    else :
        print("Incorrect spelling, Please Enter Correct spelling(Rock, Paper, Scissors)")

    play = input("Do you want to play again, press Y for Yes and N for No.: ")
    if play == "Y" or play == "y":
        return ropasc()
    else:
        print("****Thank you for playing game!****")

ropasc()