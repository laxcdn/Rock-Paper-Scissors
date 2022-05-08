from os import times
import random
from ssl import Options

user_wins = 0
Computer_wins = 0

Options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
            break

    if user_input not in ["rock", "paper", "scissors"]:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = Options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        continue
    
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        continue
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        continue

    else:
        print("You lost!")
        Computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", Computer_wins, "times.")
print("Goodbye")