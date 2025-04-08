def welcome_display() -> None:
    """
    Function to print the welcome message and chest ASCII image
    """
    treasure_chest = '''*******************************************************************************
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
*******************************************************************************'''
    print(f"{treasure_chest}\nWelcome to Treasure Island.\nYour mission is to find the treasure.")

def treasure_hunt_story() -> None:
    """
    Function to implement logic of treasure hunt game story
    """
    print("You're at a cross road. Where do you want to go?")
    user_input_1st = input("Choose to move: Type 'left' or 'right'\nChoice: ")
    user_input_1st = user_input_1st.lower()     # Lowercase the output for consistent validation

    if user_input_1st != "left" and user_input_1st != "right":     # Error detection if input is not correct for first input
        print("You chose to die. Type 'left' or 'right' only. Game Over, try again!")

    if user_input_1st == "right":
        print("Oh no, you fell into a hole. Game Over, try again!")
    elif user_input_1st == "left":
        print("You've come to a lake. There is an island in the middle of the lake.")
        user_input_2nd = input("Choose to move:\n- Type 'wait' to wait for a boat.\n- Type 'swim' to swim across.\nChoice: ")
        user_input_1st = user_input_1st.lower()     # Lowercase the output for consistent validation

        if user_input_2nd != "wait" and user_input_2nd != "swim":      # Error detection if input is not correct for seconf input
            print("You chose to die. Type 'wait' or 'swim' only. Game Over, try again!")

        if user_input_2nd == "swim":
            print("Oh no, you got attached by trout. Game Over, try again!")
        elif user_input_2nd == "wait":
            print("You arrived at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose?")
            user_input_3rd = input("Choose to move: Type 'red' or 'yellow' or 'blue'\nChoice: ")
            user_input_3rd = user_input_3rd.lower() # Lowercase the output for consistent validation

            if user_input_3rd != "red" and user_input_3rd != "yellow" and user_input_3rd != "blue":     # Error detection if input is not correct for first input
                print("You chose to die. Type 'red' or 'yellow' or 'blue' only. Game Over, try again!")

            if user_input_3rd == "red":
                print("Oh no, you got burnt by fire. Game Over, try again!")
            elif user_input_3rd == "yellow":
                print("CONGRATULATIONS!! You have made it. You win!")
            elif user_input_3rd == "blue":
                print("Oh no, you got eaten by beasts. Game Over, try again!")

def main() -> None:
    '''
    Main function to run the program
    '''
    welcome_display()
    treasure_hunt_story()

if __name__ == "__main__" :
    main()