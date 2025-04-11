# Define the constants
DICTIONARY = {
    "test1" : "this is test 1 value",
    "test2" : "this is test 2 value"
}
DICTIONARY2 = {
    "test1" : ["a", "b", "c"],
    "test2" : [1, 2, 3],
    "test3" : ["a", "b", "c", ["A", "B", "C"]]
}

def view_dictionary(dictionary: dict[str, str]) -> None:
    '''
    Function to view dictionary data based on user's key
    '''
    while True:
        user_key_input = input("Which key's value do you want to view from dictionary or 'back' to return:\nChoice: ").lower()
        if user_key_input == "back":
            break
        if user_key_input in dictionary:
            print(f"For your key '{user_key_input}', the value is: '{dictionary[user_key_input]}'.")
        else: 
            print(f"Try again, this key {user_key_input} doesn't exist in dictionary right now.")

def add_to_dictionary(dictionary: dict[str, str]) -> None:
    '''
    Function to add to the dictionary by the user
    '''
    while True:
        user_key_input = input("Enter key to add to dictionary or 'back' to return:\nKey: ").lower()
        if user_key_input == "back":
            break
        if user_key_input in dictionary:
            print(f"For your key '{user_key_input}', there is already an entry in dictionary'.")
            continue
        user_value_input = input("Value: ").strip()
        dictionary[user_key_input] = user_value_input
        print(f"Added '{user_key_input}': '{user_value_input}'.\nDictionary is now:\n{dictionary}")

def manage_dictionary() -> None:
    '''
    Function to execute the management of dictionary logic
    '''
    while True:
        user_choice = input("Choose from following input choices: 'view' or 'add' or 'quit':\nChoice: ").lower().strip()
        if user_choice == 'quit':
            print("User quit the program. Goodbye!")
            break
        if user_choice == 'view':
            view_dictionary(DICTIONARY)
        elif user_choice == 'add':
            add_to_dictionary(DICTIONARY)
        else:
            print("Error: Please choose 'view', 'add', or 'quit'.")

def main() -> None:
    '''
    Main function to run the program
    '''
    try:
        manage_dictionary()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted by the user. Goodbye!")
    except KeyError:
        print("Error: enter correct number only.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
