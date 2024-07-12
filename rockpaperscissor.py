import random

while True:
    # Get user input
    user_choice = input("Enter your choice (rock, paper, or scissors): ")

    # Generate computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
