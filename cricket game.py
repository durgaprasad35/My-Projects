import random

my_list = ["head", "tail"]

toss_choice = input("Enter your choice HEAD or TAIL: ").lower()

toss = random.choice(my_list)

if toss_choice == toss:
    print("You won the toss!")
    choice_to_bat_or_bowl = input("Do you want to bat or bowl? ").lower()
    if choice_to_bat_or_bowl == "bat":
        print("You chose to bat!")
    else:
        print("You chose to bowl!")
else:
    print("You lost the toss.")

score = 0
wickets = 0

while wickets < 10:
    user_choice = int(input("Enter the runs you want to score (1, 2, 4, or 6): "))
    choice2 = random.choice([1, 2, 4, 6])
    if user_choice == choice2:
        print("Oh no! You lost your wicket!")
        break
    else:
        print("You scored", choice2, "runs!")
        score += choice2

print("Your total score is:", score)






