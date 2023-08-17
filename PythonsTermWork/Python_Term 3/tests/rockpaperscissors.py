import random

win = 0
loss = 0
tie = 0

while True:
    user_choice = input("Rock, paper or scissors? ")
    

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

    if user_choice.lower() == computer_choice: 
        print(f"Both players selected {user_choice.lower()}. It's a tie!")
        tie +=1
    elif user_choice.lower() == "rock":
        if computer_choice == "scissors":
            print("Rock absolutely dominates scissors!")
            win +=1
        else:
            print("Paper blinds rock and smashes it!")
            loss +=1
    elif user_choice.lower() == "paper":
        if computer_choice == "rock":
            print("Paper shrouds rock in darkness and unleashes the pain!")
            win +=1
        else:
            print("Scissors slashes paper to shreds!")
            loss +=1
    elif user_choice.lower() == "scissors":
        if computer_choice == "paper":
            print("Scissors slices and dices paper!")
            win +=1
        else:
            print("Rock obliterates scissors!")
            loss +=1
            
    print(f"Wins: {win}\nLoss: {loss}\nTies: {tie}") 
    play_again = input("Run it back? (y/n): ")
    if play_again.lower() != "y":
        break