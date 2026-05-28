import random
choices = ["rock", "paper", "scissors"]
uchoice = ["rock", "rocks", "paper", "papers", "scissor", "scissors"]
print("Rock Paper Scissors!")
print("Enter rock, paper, scissors. type 'quit' to exit")

user_score = 0
com_score = 0
user_choice = None

while True:
    user_choice = input("Your choice: ")
    if user_choice == "quit":
        print(f"\nFinal Score - You: {user_score} | computer: {com_score}")
        if com_score > user_score:
            print("The Computer won the game")
        elif com_score < user_score:
            print("You won the game")
        elif com_score == user_score:
            print("This match is a tie!!")
    
                  
        print("Thanks for playing!!")
        break
    if user_choice not in uchoice:
        print("invalid choice. Try again.")
        continue
    com_choice = random.choice(choices)
    print(f"Comp chose:{com_choice}")

    if user_choice == com_choice:
        print("Its a tie!!")
    elif (user_choice == "rock" and com_choice == "scissors") or \
         (user_choice == "scissors" or "scissor" and com_choice == "paper") or \
         (user_choice == "paper" and com_choice == "rock"):
        print("You won this round!")
        user_score += 1
    else:
        print("The computer wins this round!")
        com_score += 1  
    print(f"Score - You: {user_score} | Computer score: {com_score}")    

