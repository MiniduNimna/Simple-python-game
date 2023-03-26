import random

user_score = 0
computer_score = 0
signs = ["rock" , "paper" , "scissors"]

# Default function for every pattern in the game
def patterns (sign1,sign2,message,score):
    if user_input == sign1 and computer_choice == sign2:
        print(message)
        score += 1
    return score

while True:
    user_input = input("Type Rock/ Paper/ Scissors or 'Q' to quit : ").lower()

    print()

    if user_input == "q":
        break
    
    if user_input not in signs:
        print("Invalid input")
        continue

    random_num = random.randint(0,2)
    # rock = 0 , paper = 1 , scissor = 2

    computer_choice = signs[random_num]
    print("Computer picked " + computer_choice)
 
    # User winning patterns
    user_score = patterns ("rock","scissors","You Won !",user_score)
    user_score = patterns ("paper","rock","You Won !",user_score)
    user_score = patterns ("scissors","paper","You Won !",user_score)

    # Computer winning patterns
    computer_score = patterns ("rock","paper","You lost !",computer_score)
    computer_score = patterns ("scissors","rock","You lost !",computer_score)
    computer_score = patterns ("paper","scissors","You lost !",computer_score)
    
    # Both equal patterns
    if user_input == computer_choice:
            print("It is a tie")

    print("------------------------------------")
    print()

print("You won" ,user_score, "times.")
print("Computer won" ,computer_score, "times.")
print()
print("Thank you for playing")