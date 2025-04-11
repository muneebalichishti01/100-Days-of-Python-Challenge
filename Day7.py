import random

# Define the constants
HANGMAN_ASCII = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/
'''
WORD_LIST = ["water", "annual", "iceberg", "electric", "abandoned", "jackhammer"]

def get_word_by_length(length: int, word_list: list[str]) -> str:
    '''
    Function to get a specific word from word list by user's length choice
    '''
    valid_words = []
    index = 0
    while index < len(word_list):
        if len(word_list[index]) == length:
            valid_words.append(word_list[index])
        index += 1
    return random.choice(valid_words) if valid_words else random.choice(word_list)

def get_valid_length() -> int:
    '''
    Function to get a valid length from user (5 to 10)
    '''
    while True:
        try:
            user_length_choice = int(input("Choose how long the word you want (from 5 to 10): ").strip())
            if 5 <= user_length_choice <= 10:
                return user_length_choice
            print("Error: Choose a number betewwen 5 and 10 only.")
        except ValueError:
            print("Error: Please enter a valid number.")

def get_valid_guess(guess_letters: set) -> str:
    '''
    Function to get a valid signle letter guess from user
    '''
    while True:
        user_guess = input(f"Guess a letter: ").strip().lower()
        if len(user_guess) != 1:
            print("Error: Enter exactly one letter.")
        elif not user_guess.isalpha():
            print("Error: Enter a letter (a-z).")
        elif user_guess in guess_letters:
            print("Error: You already guessed that letter.")
        else:
            return user_guess

def play_hangman_game() -> None:
    '''
    Function to run the hangman game
    '''
    print(HANGMAN_ASCII)
    lives_count = 6
    guessed_letters = set()

    user_length_choice = get_valid_length()
    secret_word = get_word_by_length(user_length_choice, WORD_LIST)
    current_state = ["_" for _ in secret_word]

    while lives_count > 0:
        print(f"Word to guess: {' '.join(current_state)}")
        print(f"Lives remaining: {lives_count}")
        user_guess = get_valid_guess(guessed_letters)

        if user_guess in secret_word:
            print(f"Good guess: '{user_guess}' is in the word!")
            index = 0
            while index < len(secret_word):
                if secret_word[index] == user_guess:
                    current_state[index] = user_guess
                index += 1
            if "_" not in current_state:
                print(f"Congratulations, you won! The word was '{secret_word}'.")
                return
        else:
            print(f"'{user_guess}' is not in the word. You lose a life.")
            lives_count -= 1

        if lives_count == 0:
            print(f"Game over! The word was '{secret_word}'.")
    
def main() -> None:
    '''
    Main function to run the program
    '''
    try:
        play_hangman_game()
    except (KeyboardInterrupt, EOFError): 
        print("\nPorgam interrupted by user. Goodbye!")
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == "__main__":
    main()
