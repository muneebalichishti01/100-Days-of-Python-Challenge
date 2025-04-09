import random

# Define the constants
RANDOM_LOWER_LIMIT = 0
RANDOM_HIGHER_LIMIT = 2
ROCK_ASCII = '''rock'''
PAPER_ASCII = '''paper'''
SCISSOR_ASCII = '''scissor'''

def random_computer_output(options_list) -> str:
    '''
    Function to give random computer output from rock paper scissor
    '''
    random_number = random.randint(RANDOM_LOWER_LIMIT, RANDOM_HIGHER_LIMIT)
    computer_output = options_list[random_number]
    return computer_output

def rock_paper_scissor() -> str:
    '''
    Function to implement main logic of rock paper scissor game
    '''
    options_list = [ROCK_ASCII, PAPER_ASCII, SCISSOR_ASCII]
    return random_computer_output(options_list)

def main() -> None:
    '''
    Main function to run the program
    '''
    try:
        print(rock_paper_scissor())
    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted by user. Goodbye!")

if __name__ == "__main__":
    main()