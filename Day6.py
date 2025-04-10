import random
import Day3
from typing import Optional

def generate_random_number() -> int:
    '''
    Function to generate a random number (1 to 100) for the guess
    '''
    return random.randint(1, 100)

def get_valid_guess() -> Optional[int]:
    '''
    Function to guess the valid number
    '''
    while True:
        user_input = input("I'm thinking of a number between 1 and 100. Guess it or type 'q' to quit.\nYour guess: ").strip().lower()
        if user_input == "q":
            print("You chose to quit the game, see you later!")
            return None
        try:
            user_input = int(user_input)
            if 1 <= user_input <= 100:
                return user_input
            else:
                 print("Error: Guess must be between 1 and 100.")
        except ValueError:
            print("Error: Please enter a valid number or 'q'.")

def play_number_guessing() -> None:
    '''
    Function to play game where players guess a random number
    '''
    target_number = generate_random_number()
    attempts_used = 0
    attempts_allowed = 10

    print(f"Welcome to the Number Guessing Game!\n You have {attempts_allowed} attempts to use.")

    while attempts_allowed > 0:
        user_guess = get_valid_guess()
        if user_guess is None:
            Day3.display_game_over()
            print(f"Target number was {target_number}.")
            return
                
        attempts_used += 1
        attempts_allowed -= 1
                
        if user_guess == target_number:
            print(f"Target number was {target_number} and you got it correct. You have won!")
            return
        elif user_guess < target_number:
            print("Too low!")
        else:
            print("Too high!")
        
        if attempts_allowed > 0:
            print(f"Attempts remaining: {attempts_allowed}")
        else:
            print(f"Game over! You've used all your attempts. The number was {target_number}.")

def main() -> None:
    '''
    Main function to run the program
    '''
    try:
        play_number_guessing()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
