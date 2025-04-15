import random

# Define the constants
GAME_LOGO = '''
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/ 
'''
COMPARISON_LOGO = '''
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
'''
DATA = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 167,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 160,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 145,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Neymar',
        'follower_count': 140,
        'description': 'Footballer',
        'country': 'Brazil'
    },
    {
        'name': 'National Geographic',
        'follower_count': 135,
        'description': 'Magazine',
        'country': 'United States'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 133,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 130,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kendall Jenner',
        'follower_count': 127,
        'description': 'Reality TV personality and model',
        'country': 'United States'
    },
    {
        'name': 'Jennifer Lopez',
        'follower_count': 119,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Nicki Minaj',
        'follower_count': 113,
        'description': 'Musician',
        'country': 'Trinidad and Tobago'
    },
    {
        'name': 'Nike',
        'follower_count': 109,
        'description': 'Sportswear multinational',
        'country': 'United States'
    },
    {
        'name': 'Khloé Kardashian',
        'follower_count': 108,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Miley Cyrus',
        'follower_count': 107,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Katy Perry',
        'follower_count': 100,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Drake',
        'follower_count': 98,
        'description': 'Musician and rapper',
        'country': 'Canada'
    },
    {
        'name': 'Shakira',
        'follower_count': 95,
        'description': 'Musician and dancer',
        'country': 'Colombia'
    },
    {
        'name': 'Virat Kohli',
        'follower_count': 92,
        'description': 'Cricketer',
        'country': 'India'
    },
    {
        'name': 'Rihanna',
        'follower_count': 91,
        'description': 'Musician and entrepreneur',
        'country': 'Barbados'
    }
]

def get_random_data_indexes() -> tuple:
    '''
    Returns 2 random indexes from the DATA list
    '''
    indices = list(range(len(DATA)))
    index_1 = random.choice(indices)
    index_2 = random.choice(indices)
    return index_1, index_2

def print_comparison_data(index_1: int, index_2: int) -> None:
    '''
    Function to print the 2 comparisons
    '''
    print(f'Compare A: {DATA[index_1]["name"]}, a {DATA[index_1]["description"]}, from {DATA[index_1]["country"]}.')
    print(COMPARISON_LOGO)
    print(f'Against B: {DATA[index_2]["name"]}, a {DATA[index_2]["description"]}, from {DATA[index_2]["country"]}.')

def get_higher_follower_count_data(index_1: int, index_2: int, user_guess: str, score:int) -> int:
    '''
    Function to calculate the higher lower difference using indexes
    '''
    if user_guess == "a":
        if DATA[index_1]["follower_count"] > DATA[index_2]["follower_count"]:
            print("You got it right!")
            score += 1
            user_tries -= 1
            return score
        else:
            print(f"You got it wrong. You loose!\nYour final score: {score}")
            raise SystemExit
    elif user_guess == "b":
        if DATA[index_2]["follower_count"] > DATA[index_1]["follower_count"]:
            print("You got it right!")
            score += 1
            user_tries -= 1
            return score
        else:
            print(f"You got it wrong. You loose!\nYour final score: {score}")
            raise SystemExit

def run_higher_lower_game() -> None:
    '''
    Function to state/implement main functionality
    '''
    print(GAME_LOGO)
    score = 0

    while True:
        index_1, index_2 = get_random_data_indexes()
        print_comparison_data(index_1, index_2)
        try:
            user_guess = input("Who has more followers? Type 'A' or 'B': ").lower().strip()
            if user_guess not in ["a", "b"]:
                print("Error: Please input only 'A' or 'B'.")
            else:
                score = get_higher_follower_count_data(index_1, index_2, user_guess, score)
                print(f"Current score: {score}")
        except ValueError:
            print("Error: Use letters 'A' or 'B' only!")

def main() -> None:
    '''
    Main function to run the program
    '''
    try:
        run_higher_lower_game()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted by the user. Goodbye!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
