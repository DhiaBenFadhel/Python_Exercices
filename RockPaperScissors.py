import random

print("Rock Paper Scissors Game 🔥")
user_wins=0
computer_wins=0
options=["rock", "paper", "scissors"]

while True:
    user_input=input("Type Rock/Paper/Scissors or Q to Quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number= random.randint(0,2)
    #rock: 0,paper: 1,scissors: 2
    computer_choice=options[random_number]
    print("Computer choose",computer_choice,".")

    if user_input == "rock" and computer_choice == "scissors":
        print("You Won!")
        user_wins+=1
    elif user_input == "paper" and computer_choice == "rock":
        print("You Won!")
        user_wins+=1
    elif user_input == "scissors" and computer_choice == "paper":
        print("You Won!")
        user_wins+=1
    elif user_input == computer_choice:
        print("You Tied!")
    else:
        print("You Lost!")
        computer_wins+=1

print("You Won:",user_wins,"Times, And the computer won:",computer_wins,"times")
print("Goodbye!")
