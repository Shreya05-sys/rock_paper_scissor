import random

def prompt_user_choice():
    while True:
        user_input = input("Please select one: rock, paper, or scissors: ").lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        print("Invalid selection. Try again.")

def generate_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def evaluate_game_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "Congratulations, you win!"
    else:
        return "Sorry, you lose."

def show_game_result(user_choice, computer_choice, result_message):
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(result_message)

def ask_for_rematch():
    return input("Would you like to play another round? (yes/no): ").lower() == "yes"

def main_game():
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = prompt_user_choice()
        computer_choice = generate_computer_choice()
        result_message = evaluate_game_result(user_choice, computer_choice)
        
        if result_message == "Congratulations, you win!":
            user_score += 1
        elif result_message == "Sorry, you lose.":
            computer_score += 1
        
        show_game_result(user_choice, computer_choice, result_message)
        
        print(f"\nScoreboard - You: {user_score}, Computer: {computer_score}")
        
        if not ask_for_rematch():
            break
    
    print("\nThanks for playing!")

if __name__ == "__main__":
    main_game()