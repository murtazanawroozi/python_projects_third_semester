import random

options = ["rock", "paper", "scissors"]
user_choice = input().strip().lower()
computer_choice = random.choice(options)

print(computer_choice)

if user_choice == computer_choice:
    print("draw")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("win")
else:
    print("lose")