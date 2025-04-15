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

def display_tik_tac_toe_move(player_input: int, board_list: list) -> None:
    '''
    Function to execute adding the player input on board
    '''
    if player_input == 1:
        print(f"Game Board:")
        print_game_board(board_list)
    elif player_input == 2:
        print(f"Game Board:")
        print_game_board(board_list)
    elif player_input == 3:
        print(f"Game Board:")
        print_game_board(board_list)
    elif player_input == 4:
        print(f"Game Board:")
        print_game_board(board_list)
    elif player_input == 5:
        print(f"Game Board:")
        print_game_board(board_list)
    elif player_input == 6:
        print(f"Game Board:")
        print_game_board(board_list)
    elif player_input == 7:
        print(f"Game Board:")
        print_game_board(board_list)
    elif player_input == 8:
        print(f"Game Board:")
        print_game_board(board_list)
    elif player_input == 9:
        print(f"Game Board:")
        print_game_board(board_list)

def run_tik_tac_toe() -> None:
    '''
    Function to implement main logic for the fucntionality
    '''
    print("\n"*100)
    print(GAME_LOGO)
    print(f"Game Board:")
    print_game_board(GAME_BOARD_LIST)

    while True:
        player_x_input = input("Player X, enter position (1-9 or 'q' to quit).\nChoice: ").lower().strip()
        if player_x_input.isdigit():
            player_x_input = int(player_x_input)
            if player_x_input >= 1 and player_x_input <=9:
                display_tik_tac_toe_move(player_x_input)
            else:
                print("Please use numerical position number 1 to 9 only.")
        elif player_x_input == 'q':
            print("You chose to quit the game. Goodbye!")
            break
        else:
            print("Please use numerical position number 1 to 9 only.")

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
