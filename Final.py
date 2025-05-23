import random
def game():
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    user = input("Enter rock, paper, or scissors: ").lower()
    while user not in ["rock","paper","scissors"]:
        user=input("invalid input.please enter rock , paper, or scissors:").lower()
    print(f"\nComputer chose {computer}")
    if user == computer:
        print(f"Both players selected {user}. It's a tie!")
    elif user == "rock":
        if computer == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user == "paper":
        if computer == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scisors cuts paper! You lose.")
    elif user == "scissors":
        if computer == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    play_again = input("Play again? (yes/no): ").lower()
    if play_again == "yes":
        game()
    else:
        print("Thanks for playing!")
game()        
                                           