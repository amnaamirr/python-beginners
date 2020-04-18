# rockpaperscissorsgame
import random
name = input("ENTER YOUR NAME: ")
print("Hi! Welcome,", name)

user_choice = False
while user_choice == False:
    print("ROCK,PAPER OR SCISSORS")
    user_choice = input("ENTER YOUR CHOICE: ").lower()

    # computerchoice
    comp_choice = random.randint(0, 2)
    if comp_choice == 0:
        comp_choice = "rock"
    elif comp_choice == 1:
        comp_choice = "paper"
    else:
        comp_choice = "scissor"
    print(f"YOUR CHOICE: {user_choice}")
    print(f"COMPUTER'S CHOICE: {comp_choice}")
# deciding the winner
# ROCK BLUNTS SCISSORS
# SCISSORS CUTS PAPER
# PAPER COVERS ROCK
# IF PLAYER AND COMP CHOOSE SAME, ITS A DRAW

    if user_choice == comp_choice:
        winner = "draw"
# if user chooses rock
    elif user_choice == "rock":
        if comp_choice == "paper":
            winner = "computer"
            print("PAPER COVERS ROCK")
        else:
            winner = "user"
            print("ROCK BLUNTS SCISSORS")
# if user chooses scissors
    elif user_choice == "scissors":
        if comp_choice == "paper":
            winner = "user"
            print("SCISSORS CUT PAPER")
        else:
            winner = "computer"
            print("ROCK BLUNTS SCISSORS")
# if user chooses paper
    elif user_choice == "paper":
        if comp_choice == "rock":
            winner = "user"
            print("PAPER COVERS ROCK")
        else:
            winner = "computer"
            print("SCISSORS CUT PAPER")
    else:
        print("INVALID CHOICE! CHECK YOUR SPELLINGS.")

    if (winner == "draw"):
        print("IT'S A DRAW!")
    elif (winner == "user"):
        print("CONGRATULATIONS! YOU WIN!")
    else:
        print("YOU LOOSE!\nBETTER LUCK NEXT TIME!")
    print("\n")
    print("DO YOU WANT TO PLAY AGAIN? TYPE BELOW [Y/N]: ")
    ans = input("> ").upper()
    if ans == "N":
        print("THANKYOU FOR PLAYING!")
        exit()
    # setting the choice to false so the loop runs again
    else:
        user_choice = False
