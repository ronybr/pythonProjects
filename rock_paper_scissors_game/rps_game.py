from random import randint

#Create a list of play options
play_options = ["rock", "paper", "scissors"]
#Assign a rondom option to the computer
computer_choice = play_options[randint(0, 2)]

#Set player to false
player = False

while player == False:
    player = input("Rock, Paper, Scissors?").lower()
    if player == computer_choice:
        print("Tie!")
    elif player == "rock":
        if computer_choice == "paper":
            print("You loose!", computer_choice, "covers", player, "\n")
        else:
            print("You win!", player, "smashes", computer_choice, "\n")
    elif player == "paper":
        if computer_choice == "scissors":
            print("You loose!", computer_choice, "cut", player, "\n")
        else:
            print("You win!", player, "covers", computer_choice, "\n")
    elif player == "scissors":
        if computer_choice == "rock":
            print("You loose!", computer_choice, "smashes", player, "\n")
        else:
            print("You win!", player, "cut", computer_choice, "\n")
    else:
        print("Option Invalid, choose a valid one!", "\n")

    print("+++++++++++++ NEXT TURN +++++++++++++")
    #PLayer was set tp True, but I want it to be False, so loop continues
    player = False
    computer_choice = play_options[randint(0, 2)]