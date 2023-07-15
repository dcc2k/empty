import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Choose one: rock, paper, or scissors.")

    choices = ["rock", "paper", "scissors"]
    user_choice = input("Your choice: ").lower()
    computer_choice = random.choice(choices)

    print("Computer's choice:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif [user_choice, computer_choice] in [["rock", "scissors"], ["paper", "rock"], ["scissors", "paper"]]:
        print("You win!")
    else:
        print("Computer wins!")

    print()

def main():
    play_game()

    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
        print()
        play_game()

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
