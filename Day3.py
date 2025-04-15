# Define the constants
CHOICE_LEFT = "left"
CHOICE_RIGHT = "right"
CHOICE_WAIT = "wait"
CHOICE_SWIM = "swim"
CHOICE_RED = "red"
CHOICE_YELLOW = "yellow"
CHOICE_BLUE = "blue"

TREASURE_CHEST_ART = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
'''

def welcome_display() -> None:
    """
    Function to print the welcome message and chest ASCII image
    """
    print(f"{TREASURE_CHEST_ART}\nWelcome to Treasure Island.\nYour mission is to find the treasure.")

def display_game_over() -> None:
    """
    Function to display the game over text
    """
    print("Game Over!")

def treasure_hunt_story() -> None:
    """
    Function to implement logic of treasure hunt game story
    """
    print("You're at a cross road. Where do you want to go?")
    user_input_1st = input("Choose to move: Type 'left' or 'right'\nChoice: ")
    user_input_1st = user_input_1st.lower()     # Lowercase the output for consistent validation

    if user_input_1st != CHOICE_LEFT and user_input_1st != CHOICE_RIGHT:     # Error detection if input is not correct for first input
        print("You chose to die. Type 'left' or 'right' only.")
        display_game_over()

    if user_input_1st == CHOICE_RIGHT:
        print("Oh no, you fell into a hole.")
        display_game_over()
    elif user_input_1st == CHOICE_LEFT:
        print("You've come to a lake. There is an island in the middle of the lake.")
        user_input_2nd = input("Choose to move:\n- Type 'wait' to wait for a boat.\n- Type 'swim' to swim across.\nChoice: ")
        user_input_1st = user_input_1st.lower()     # Lowercase the output for consistent validation

        if user_input_2nd != CHOICE_WAIT and user_input_2nd != CHOICE_SWIM:      # Error detection if input is not correct for seconf input
            print("You chose to die. Type 'wait' or 'swim' only.")
            display_game_over()

        if user_input_2nd == CHOICE_SWIM:
            print("Oh no, you got attached by trout.")
            display_game_over()
        elif user_input_2nd == CHOICE_WAIT:
            print("You arrived at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose?")
            user_input_3rd = input("Choose to move: Type 'red' or 'yellow' or 'blue'\nChoice: ")
            user_input_3rd = user_input_3rd.lower() # Lowercase the output for consistent validation

            if user_input_3rd != CHOICE_RED and user_input_3rd != CHOICE_YELLOW and user_input_3rd != CHOICE_BLUE:     # Error detection if input is not correct for first input
                print("You chose to die. Type 'red' or 'yellow' or 'blue' only.")
                display_game_over()

            if user_input_3rd == CHOICE_RED:
                print("Oh no, you got burnt by fire.")
                display_game_over()
            elif user_input_3rd == CHOICE_YELLOW:
                print("CONGRATULATIONS!! You have made it. You win!")
            elif user_input_3rd == CHOICE_BLUE:
                print("Oh no, you got eaten by beasts.")
                display_game_over()

def main() -> None:
    '''
    Main function to run the program
    '''
    welcome_display()
    treasure_hunt_story()

if __name__ == "__main__" :
    main()