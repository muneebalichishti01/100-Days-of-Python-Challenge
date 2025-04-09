import random
import Day3

# Define the constants
RANDOM_LOWER_LIMIT = 0
RANDOM_HIGHER_LIMIT = 2
ROCK_ASCII = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
PAPER_ASCII = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
SCISSOR_ASCII = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
VALID_INPUTS = [0, 1, 2]
OPTIONS = [ROCK_ASCII, PAPER_ASCII, SCISSOR_ASCII]

def get_computer_number() -> int:
    '''
    Function to give random computer number for rock paper scissor
    '''
    computer_random_number = random.randint(RANDOM_LOWER_LIMIT, RANDOM_HIGHER_LIMIT)
    return computer_random_number

def print_computer_choice(choice) -> None:
    '''
    Function to print computer's choice
    '''
    print("Computer's choice:\n", choice)

def print_user_choice(choice) -> None:
    '''
    Function to print user's's choice
    '''
    print("Your choice:\n", choice)

def print_draw() -> None:
    '''
    Function to print draw
    '''
    print("It's a draw!")
    Day3.display_game_over()
    
def print_computer_win() -> None:
    '''
    Function to print computer win
    '''
    print("Computer wins, you lose!")
    Day3.display_game_over()

def print_user_win() -> None:
    '''
    Function to print user win
    '''
    print("You win, yay!!")
    Day3.display_game_over()

def play_rock_paper_scissors(user_input: int) -> None:
    '''
    Function to implement main logic of rock paper scissor game
    '''
    if user_input not in VALID_INPUTS:
        raise Exception("Option chosen cannot be other than 0, 1, 2.")
    
    user_choice = OPTIONS[user_input]
    computer_random_number = get_computer_number()
    computer_choice = OPTIONS[computer_random_number]

    print_computer_choice(computer_choice)
    print_user_choice(user_choice)

    if user_input == computer_random_number:
        print_draw()
    elif user_input == 0 and computer_random_number == 1:
        print_computer_win()
    elif user_input == 1 and computer_random_number == 0:
        print_user_win()
    elif user_input == 1 and computer_random_number == 2:
        print_computer_win()
    elif user_input == 2 and computer_random_number == 1:
        print_user_win()
    elif user_input == 0 and computer_random_number == 2:
        print_user_win()
    elif user_input == 2 and computer_random_number == 0:
        print_computer_win()

def main() -> None:
    '''
    Main function to run the program
    '''
    print("Welcome to Rock Paper Scissor Game")
    try:
        user_input = int(input("What do you choose:\n- Type 0 for Rock\n- Type 1 for Paper\n- Type 2 for Scissors.\n Your choice: "))
        play_rock_paper_scissors(user_input)
    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted by user. Goodbye!")
    except ValueError:
        print("Error: Please enter a number (0, 1, or 2).")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
