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
WORD_LIST = [
  "abruptly",
  "absurd",
  "abyss",
  "affix",
  "askew",
  "avenue",
  "awkward",
  "axiom",
  "azure",
  "bagpipes",
  "bandwagon",
  "banjo",
  "bayou",
  "beekeeper",
  "bikini",
  "blitz",
  "blizzard",
  "boggle",
  "bookworm",
  "boxcar",
  "boxful",
  "buckaroo",
  "buffalo",
  "buffoon",
  "buxom",
  "buzzard",
  "buzzing",
  "buzzwords",
  "caliph",
  "cobweb",
  "cockiness",
  "croquet",
  "crypt",
  "curacao",
  "cycle",
  "daiquiri",
  "dirndl",
  "disavow",
  "dizzying",
  "duplex",
  "dwarves",
  "embezzle",
  "equip",
  "espionage",
  "euouae",
  "exodus",
  "faking",
  "fishhook",
  "fixable",
  "fjord",
  "flapjack",
  "flopping",
  "fluffiness",
  "flyby",
  "foxglove",
  "frazzled",
  "frizzled",
  "fuchsia",
  "funny",
  "gabby",
  "galaxy",
  "galvanize",
  "gazebo",
  "giaour",
  "gizmo",
  "glowworm",
  "glyph",
  "gnarly",
  "gnostic",
  "gossip",
  "grogginess",
  "haiku",
  "haphazard",
  "hyphen",
  "iatrogenic",
  "icebox",
  "injury",
  "ivory",
  "ivy",
  "jackpot",
  "jaundice",
  "jawbreaker",
  "jaywalk",
  "jazziest",
  "jazzy",
  "jelly",
  "jigsaw",
  "jinx",
  "jiujitsu",
  "jockey",
  "jogging",
  "joking",
  "jovial",
  "joyful",
  "juicy",
  "jukebox",
  "jumbo",
  "kayak",
  "kazoo",
  "keyhole",
  "khaki",
  "kilobyte",
  "kiosk",
  "kitsch",
  "kiwifruit",
  "klutz",
  "knapsack",
  "larynx",
  "lengths",
  "lucky",
  "luxury",
  "lymph",
  "marquis",
  "matrix",
  "megahertz",
  "microwave",
  "mnemonic",
  "mystify",
  "naphtha",
  "nightclub",
  "nowadays",
  "numbskull",
  "nymph",
  "onyx",
  "ovary",
  "oxidize",
  "oxygen",
  "pajama",
  "peekaboo",
  "phlegm",
  "pixel",
  "pizazz",
  "pneumonia",
  "polka",
  "pshaw",
  "psyche",
  "puppy",
  "puzzling",
  "quartz",
  "queue",
  "quips",
  "quixotic",
  "quiz",
  "quizzes",
  "quorum",
  "razzmatazz",
  "rhubarb",
  "rhythm",
  "rickshaw",
  "schnapps",
  "scratch",
  "shiv",
  "snazzy",
  "sphinx",
  "spritz",
  "squawk",
  "staff",
  "strength",
  "strengths",
  "stretch",
  "stronghold",
  "stymied",
  "subway",
  "swivel",
  "syndrome",
  "thriftless",
  "thumbscrew",
  "topaz",
  "transcript",
  "transgress",
  "transplant",
  "triphthong",
  "twelfth",
  "twelfths",
  "unknown",
  "unworthy",
  "unzip",
  "uptown",
  "vaporize",
  "vixen",
  "vodka",
  "voodoo",
  "vortex",
  "voyeurism",
  "walkway",
  "waltz",
  "wave",
  "wavy",
  "waxy",
  "wellspring",
  "wheezy",
  "whiskey",
  "whizzing",
  "whomever",
  "wimpy",
  "witchcraft",
  "wizard",
  "woozy",
  "wristwatch",
  "wyvern",
  "xylophone",
  "yachtsman",
  "yippee",
  "yoked",
  "youthful",
  "yummy",
  "zephyr",
  "zigzag",
  "zigzagging",
  "zilch",
  "zipper",
  "zodiac",
  "zombie",
]

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
