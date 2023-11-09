# Create a console game called "rock, paper, scissors" with the following rules:
# - The game is played against the computer.
# - The computer randomly chooses one of the three options.
# - The user chooses one of the three options.
# - A tie is declared if both choose the same option.
# - Otherwise the winner is determined as follows:
#   - Rock beats scissors.
#   - Scissors beats paper.
#   - Paper beats rock.
# - The game is played until the user chooses to quit.
# - The user's score is displayed after each round.
# - The user's final score is displayed at the end of the game.
# - The user can choose to play again at the end of the game.
# - A warning is displayed if the user enters an invalid option.

import random

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("You will be playing against the computer.")
    print("Choose one of the following options:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")
    print()

    # Get user input
    user_choice = int(input("Enter your choice: "))
    print()

    # Initialize variables
    user_score = 0
    computer_score = 0

    # Play game until user chooses to quit
    while user_choice != 4:
        # Get computer choice
        computer_choice = random.randint(1, 3)

        # Determine winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == 1 and computer_choice == 3:
            print("You win!")
            user_score += 1
        elif user_choice == 2 and computer_choice == 1:
            print("You win!")
            user_score += 1
        elif user_choice == 3 and computer_choice == 2:
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

        # Display scores
        print("Your score:", user_score)
        print("Computer score:", computer_score)
        print()

        # Get user input
        user_choice = int(input("Enter your choice: "))
        print()

    # Display final scores
    print("Final scores:")
    print("Your score:", user_score)
    print("Computer score:", computer_score)

main()