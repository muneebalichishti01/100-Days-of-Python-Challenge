# Define the constants
GAME_LOGO = '''
___________.__ __           ___________                     ___________            
\__    ___/|__|  | __       \__    ___/____    ____         \__    ___/___   ____  
  |    |   |  |  |/ /  ______ |    |  \__  \ _/ ___\   ______ |    | /  _ \_/ __ \ 
  |    |   |  |    <  /_____/ |    |   / __ \\  \___  /_____/ |    |(  <_> )  ___/ 
  |____|   |__|__|_ \         |____|  (____  /\___  >         |____| \____/ \___  >
                   \/                      \/     \/                            \/ 
'''
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
    if str(board_list[player_input - 1]) in PLAYERS:
        print("That position is already taken. Try again.")
    else:
        board_list[player_input - 1] = user_x_or_y
        print("Game Board:")
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
            if 1 <= player_input <= 9:
                if str(game_board_list[player_input - 1]) in PLAYERS:
                    print("Position already taken. Try a different one.")
                    continue
                updated_board_list = run_tik_tac_toe_move(player_input, game_board_list, player_chosen)
                return updated_board_list
            else:
                print("Please use numerical position number 1 to 9 only.")
        else:
            print("Please use numerical position number 1 to 9 only.")

def evaluate_winner(player_chosen: str, game_board_list: list) -> bool:
    '''
    Function to check if the chosen player has won
    '''
    win_conditions_list = [
        (0, 1, 2),  # top row
        (3, 4, 5),  # middle row
        (6, 7, 8),  # bottom row
        (0, 3, 6),  # left column
        (1, 4, 7),  # middle column
        (2, 5, 8),  # right column
        (0, 4, 8),  # main diagonal
        (2, 4, 6)   # anti-diagonal
    ]

    for position_1, position_2, position_3 in win_conditions_list:
        if game_board_list[position_1] == game_board_list[position_2] == game_board_list[position_3] == player_chosen:
            print(f"Player {player_chosen} wins!")
            return True
    return False

def play_tik_tac_toe(game_board_list: list) -> None:
    '''
    Function to play the game for 2 users
    '''
    game_board_list[:] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Game Board:")
    print_game_board(game_board_list)

    while True:
        for player in PLAYERS:
            updated_board = call_player_turn(player, game_board_list)
            if evaluate_winner(player, updated_board):
                print("Final Game Board:")
                print_game_board(game_board_list)
                return
            if all(str(position) in PLAYERS for position in game_board_list):
                print("It's a draw!")
                print("Final Game Board:")
                print_game_board(game_board_list)
                return
    
def run_tik_tac_toe() -> None:
    '''
    Function to implement main logic for the fucntionality
    '''
    print("\n"*100)
    print(GAME_LOGO)

    while True:
        try:
            user_option = input("Do you want to play the game? Type 'y' or 'n'.\nChoice: ").lower().strip()
            if user_option == 'n':
                print("You chose to quit the game, Goodbye!")
                break
            elif user_option == 'y':
                game_board_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                play_tik_tac_toe(game_board_list)
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
        print("\nProgram interrupted by the user. Goodbye!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
