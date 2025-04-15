# Define the constants
GAME_LOGO = '''
___________.__ __           ___________                     ___________            
\__    ___/|__|  | __       \__    ___/____    ____         \__    ___/___   ____  
  |    |   |  |  |/ /  ______ |    |  \__  \ _/ ___\   ______ |    | /  _ \_/ __ \ 
  |    |   |  |    <  /_____/ |    |   / __ \\  \___  /_____/ |    |(  <_> )  ___/ 
  |____|   |__|__|_ \         |____|  (____  /\___  >         |____| \____/ \___  >
                   \/                      \/     \/                            \/ 
'''
GAME_BOARD_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9]
PLAYERS = ["X", "Y"]

def print_game_board(board_list: list) -> None:
    '''
    Function to print the board based on the list
    '''
    game_board = f'''
---+---+-----
| {board_list[0]} | {board_list[1]} | {board_list[2]} |
---+---+-----
| {board_list[3]} | {board_list[4]} | {board_list[5]} |
---+---+-----
| {board_list[6]} | {board_list[7]} | {board_list[8]} |
---+---+-----
'''
    print(game_board)

def run_tik_tac_toe_move(player_input: int, board_list: list, user_x_or_y: str) -> list:
    '''
    Function to execute adding the player input on board
    '''
    if player_input == 1:
        print(f"Game Board:")
        board_list[0] = user_x_or_y
        print_game_board(board_list)
    elif player_input == 2:
        board_list[1] = user_x_or_y
        print(f"Game Board:")
        print_game_board(board_list)
    elif player_input == 3:
        board_list[2] = user_x_or_y
        print(f"Game Board:")
        print_game_board(board_list)
    elif player_input == 4:
        board_list[3] = user_x_or_y
        print(f"Game Board:")
        print_game_board(board_list)
    elif player_input == 5:
        board_list[4] = user_x_or_y
        print(f"Game Board:")
        print_game_board(board_list)
    elif player_input == 6:
        board_list[5] = user_x_or_y
        print(f"Game Board:")
        print_game_board(board_list)
    elif player_input == 7:
        board_list[6] = user_x_or_y
        print(f"Game Board:")
        print_game_board(board_list)
    elif player_input == 8:
        board_list[7] = user_x_or_y
        print(f"Game Board:")
        print_game_board(board_list)
    elif player_input == 9:
        board_list[8] = user_x_or_y
        print(f"Game Board:")
        print_game_board(board_list)

    return board_list

def call_player_turn(player_chosen:str, game_board_list: list) -> list:
    '''
    Function to run the player's turn
    '''
    while True:
        print(f"Player {player_chosen}, enter position 1 to 9.\n")
        player_input = input("Choice: ").lower().strip()
        if player_input.isdigit():
            player_input = int(player_input)
            if player_input >= 1 and player_input <=9:
                updated_board_list = run_tik_tac_toe_move(player_input, game_board_list, player_chosen)
                return updated_board_list
            else:
                print("Please use numerical position number 1 to 9 only.")
        else:
            print("Please use numerical position number 1 to 9 only.")

def evaluate_winner(player_chosen: str, game_board_list: list) -> bool:
    '''
    Function to evaludate the winner after every step
    '''
    winner = False
    if game_board_list[0] == player_chosen and game_board_list[1] == player_chosen and game_board_list[2] == player_chosen:
        print(f"Player {player_chosen} wins!")
        winner = True
    elif game_board_list[3] == player_chosen and game_board_list[4] == player_chosen and game_board_list[5] == player_chosen:
        print(f"Player {player_chosen} wins!")
        winner = True
    elif game_board_list[6] == player_chosen and game_board_list[7] == player_chosen and game_board_list[8] == player_chosen:
        print(f"Player {player_chosen} wins!")
        winner = True
    elif game_board_list[0] == player_chosen and game_board_list[3] == player_chosen and game_board_list[6] == player_chosen:
        print(f"Player {player_chosen} wins!")
        winner = True
    elif game_board_list[1] == player_chosen and game_board_list[4] == player_chosen and game_board_list[7] == player_chosen:
        print(f"Player {player_chosen} wins!")
        winner = True
    elif game_board_list[2] == player_chosen and game_board_list[5] == player_chosen and game_board_list[8] == player_chosen:
        print(f"Player {player_chosen} wins!")
        winner = True
    elif game_board_list[0] == player_chosen and game_board_list[4] == player_chosen and game_board_list[8] == player_chosen:
        print(f"Player {player_chosen} wins!")
        winner = True
    elif game_board_list[2] == player_chosen and game_board_list[4] == player_chosen and game_board_list[6] == player_chosen:
        print(f"Player {player_chosen} wins!")
        winner = True
    return winner

def play_tik_tac_toe(game_board_list: list) -> None:
    '''
    Function to play the game for 2 users
    '''
    while True:
        game_board_list_1 = call_player_turn(PLAYERS[0], GAME_BOARD_LIST)
        winner = evaluate_winner(PLAYERS[0], game_board_list_1)
        if winner == True:
            break
        game_board_list_2 = call_player_turn(PLAYERS[1], GAME_BOARD_LIST)
        winner = evaluate_winner(PLAYERS[1], game_board_list_2)
        if winner == True:
            break
    print("Final Game Board:")
    print_game_board(game_board_list)
    
def run_tik_tac_toe() -> None:
    '''
    Function to implement main logic for the fucntionality
    '''
    print("\n"*100)
    print(GAME_LOGO)
    print(f"Game Board:")
    print_game_board(GAME_BOARD_LIST)

    while True:
        try:
            user_option = input("Do you want to play the game? Type 'y' or 'n'.\nChoice: ").lower().strip()
            if user_option == 'n':
                print("You chose to quit the game, Goodbye!")
                break
            elif user_option == 'y':
                play_tik_tac_toe(GAME_BOARD_LIST)
            else:
                print("Choose the correct option: 'y' or 'n'.")
        except ValueError:
            print("Error: Please use numerical position number 1 to 9 only.")

def main() -> None:
    '''
    Main function to run the program
    '''
    try:
        run_tik_tac_toe()
    except (KeyboardInterrupt, EOFError):
        print("\nPorgram interrupted by the user. Goodbye!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
