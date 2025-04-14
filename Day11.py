import random

# Define the constants
BLACKJACK_ASCII = '''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_| |\__,_|\___|_|\_/
      |  \/ K|                            _/ |                
      '------'                           |__/           
'''
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_random_cards_list(number: int) -> list:
    '''
    Function to generate a list of random cards from the CARDS list
    '''
    random_cards_list = []
    for _ in range(number):
        random_index = int(random.random() * len(CARDS))
        random_cards_list.append(CARDS[random_index])
    return random_cards_list

def evaluate_winner(game_cards: dict) -> None:
    '''
    Function to evaluate the final winner
    '''
    user_score = game_cards["user"]["total_score"]
    computer_score = game_cards["computer"]["total_score"]

    if user_score > 21:
        print("Bust! You went over 21. You lose!")
    elif computer_score > 21:
        print("Computer went over 21. You win!")
    elif user_score > computer_score:
        print("You win!")
    elif user_score < computer_score:
        print("You lose!")
    else:
        print("It's a draw!")

def get_user_next_choice(game_cards: dict) -> None:
    '''
    Function to get user's met choice with valid checks
    '''
    while True:
        user_choice = input("Type 'y' to get another card, type 'n' to pass.\nChoice: ").lower()
        if user_choice == 'n':
            while game_cards["computer"]["total_score"] < 17:
                game_cards["computer"]["current_cards"].extend(get_random_cards_list(1))
                game_cards["computer"]["total_score"] = add_cards(game_cards["computer"]["current_cards"])
            print(f"    Your final hand: {game_cards['user']['current_cards']}, current score: {game_cards['user']['total_score']}")
            print(f"    Computer's final hand: {game_cards['computer']['current_cards']}, current score: {game_cards['computer']['total_score']}")
            evaluate_winner(game_cards)
            break
        elif user_choice == 'y':
            game_cards["user"]["current_cards"].extend(get_random_cards_list(1))
            game_cards["user"]["total_score"] = add_cards(game_cards["user"]["current_cards"])
            print(f"    Your cards: {game_cards['user']['current_cards']}, current score: {game_cards['user']['total_score']}")
            print(f"    Computer's first card: {game_cards['computer']['current_cards'][0]}")

            if game_cards["user"]["total_score"] > 21:
                evaluate_winner(game_cards)
                print(f"    Your final hand: {game_cards['user']['current_cards']}, current score: {game_cards['user']['total_score']}")
                print(f"    Computer's final hand: {game_cards['computer']['current_cards']}, current score: {game_cards['computer']['total_score']}")
                break
        else:
            print("Error: Please type 'y' or 'n'.")
        
def add_cards(card_list: list) -> int:
    '''
    Function to calculate the final total of all cards in the list while handling Aces as 1 or 11
    '''
    card_total = 0
    aces = 0

    for card in card_list:
        if card == 11:
            aces += 1
        else:
            card_total += card

    for _ in range(aces):
        if card_total + 11 <= 21:
            card_total += 11
        else:
            card_total += 1

    return card_total

def play_blackjack() -> None:
    '''
    Function to implement play logic of the game
    '''
    print(BLACKJACK_ASCII)
    
    game_cards = {
        "user": {
            "current_cards" : [],
            "total_score": 0
        },
        "computer": {
            "current_cards" : [],
            "total_score": 0
        }
    }

    game_cards["user"]["current_cards"].extend(get_random_cards_list(2))
    game_cards["user"]["total_score"] = add_cards(game_cards["user"]["current_cards"])
    game_cards["computer"]["current_cards"].extend(get_random_cards_list(1))
    game_cards["computer"]["total_score"] = add_cards(game_cards["computer"]["current_cards"])
    
    print(f"    Your cards: {game_cards['user']['current_cards']}, current score: {game_cards['user']['total_score']}")
    print(f"Computer's first card: {game_cards['computer']['current_cards'][0]}")
    get_user_next_choice(game_cards)


def run_blackjack() -> None:
    '''
    Function to implement main black jack logic
    '''
    while True:
        user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n'.\nChoice: ").lower()
        if user_input == 'n':
            print("You chose to quit to the program. Goodbye!")
            break
        elif user_input == 'y':
            play_blackjack()
        else:
            print("Error: Please type 'y' or 'n'.")

def main() -> None:
    '''
    Main function to run the program
    '''
    try:
        run_blackjack()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted by the user. Goodbye!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
