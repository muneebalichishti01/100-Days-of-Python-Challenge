import random

# Define the constants
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '"', "'", '<', '>', ',', '.', '?', '/']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def random_list_generator(letter_count: int, symbol_count: int, numbers_count: int) -> tuple[list[int], list[int], list[int]]:
    '''
    Function to generate random letters, symbols, numbers
    '''
    random_letter_list = random.sample(LETTERS, letter_count)
    random_symbol_list = random.sample(SYMBOLS, symbol_count)
    random_numbers_list = random.sample(NUMBERS, numbers_count)
    return random_letter_list, random_symbol_list, random_numbers_list

def unique_password_generator(letter_count: int, symbol_count: int, numbers_count: int) -> None:
    '''
    Function to generate random secured password
    '''
    if not isinstance(letter_count, int) or not isinstance(symbol_count, int) or not isinstance(numbers_count, int):
        raise Exception("Type in numbers only!")
    
    random_letter_list, random_symbol_list, random_numbers_list = random_list_generator(letter_count, symbol_count, numbers_count)
    
    password = random_letter_list + random_symbol_list + random_numbers_list
    random.shuffle(password)

    password_str = ''.join(password)
    print(f"Generated password: {password_str}")

def main() -> None:
    '''
    Main function to run the program
    '''
    print("Welcome to the PyPassword Generator!")
    try:
        letter_count = int(input("How many letters would you like in your password?\n Choice: "))
        symbol_count = int(input("How many symbols would you like?\n Choice: "))
        numbers_count = int(input("How many numbers would you like?\n Choice: "))

        unique_password_generator(letter_count, symbol_count, numbers_count)
    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()