# rolling the dice game
import random

name = input(("ENTER YOUR NAME: "))
print(f"Hi {name}! Welcome,")
user_choice = False
while user_choice == False:
    user_choice = input("Enter 'ROLL' to roll the dice: ").lower()
    if user_choice == "roll":
        dice_roll1 = random.randint(1, 6)
        dice_roll2 = random.randint(1, 6)
        print("THE VALUEs ARE:")
        print(dice_roll1)
        print(dice_roll2)
    else:
        print("SORRY, I DIDNT GET WHAT YOU SAID!")
    print("DO YOU WANT TO ROLL THE DICES AGAIN?")
    print("MENTION [Y/N] BELOW: ")
    play_again = input(">").lower()
    if play_again == "y":
        user_choice = False
    else:
        print("THANKS FOR PLAYING!")
        exit()
