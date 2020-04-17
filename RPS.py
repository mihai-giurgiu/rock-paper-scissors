import random

comp_wins = 0
user_wins = 0

def Uoptions():
    user_choice = input("Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock", "rock", "r", "R"]: 
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S"]: 
        user_choice = "s"
    else: 
        print("I don't understand")
        Uoptions()
    return user_choice

def Coptions(): 
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice ="r"
    elif comp_choice == 2:
        comp_choice = "p"
    elif comp_choice == 3:
        comp_choice = "s"
    return comp_choice

while True:
    print("")
    user_choice = Uoptions()
    comp_choice = Coptions()

    if user_choice == "r":
        if comp_choice == "r": 
            print("It's a tie")
        elif comp_choice == "p":
            print("The computer chose paper and you chose rock. You lose")
            comp_wins += 1
        elif comp_choice == "s":
            print("You chose rock. The computer chose scissors. You win")
            user_wins +=1   

    
    elif user_choice == "p":
        if comp_choice == "r":
            print("You chose paper. The computer chose rock. You win")
            user_wins +=1

        elif comp_choice == "p": 
            print("It's a tie")
        
        elif comp_choice == "s":
            print("You chose paper. The computer chose scissors. You lose")
            comp_wins += 1

    elif user_choice == "s":
        if comp_choice == "r":
            print("You chose scissors. The computer chose rock. You lose")
            comp_wins +=1 

        elif comp_choice == "s":
            print("It's a tie")

        elif comp_choice == "p":
            print("You chose scissors. The computer chose paper. You win")
            user_wins += 1

    print("")
    print("User wins: " + str(user_wins))
    print("Computer wins: " + str(comp_wins))
    print("")

        
                     


        