# Define the constants
CALCULATOR_LOGO = '''
 _____________________
|  _________________  |
| |              0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
'''
POSITION = ["first", "second"]

def get_valid_number(position: str) -> float:
    '''
    Function to get the valid number with the valid checks
    '''
    while True:
        try:
            number = float(input(f"Choose your {position} number: "))
            break
        except ValueError:
            print("Error: Please enter a valid number.")
    return number

def get_valid_operand() -> None:
    '''
    Function to validate the valid operand with checks
    '''
    while True:
        operand = input("Choose one operand: '+' '-' '*' '/': ").strip()
        if operand == "+" or operand == "-" or operand == "*" or operand == "/":
            return operand
        else:
            print("Error: Please choose a valid operand ('+', '-', '*', '/').")

def calculate_result(first_number: float, second_number: float, operand: str) -> float:
    '''
    Function to calculate the results based on the user's operand and numbers
    '''
    if operand == "+":
        result = first_number + second_number
    elif operand == "-":
        result = first_number - second_number
    elif operand == "*":
        result = first_number * second_number
    elif operand == "/":
        while second_number == 0:
            print("Error: Division by zero is not allowed, try another number.")
            second_number = get_valid_number(POSITION[1])
        result = first_number / second_number
    return round(result, 2)

def continue_calculation(first_number: float, result: float) -> None:
    '''
    Function to store final result and continue the calculations
    '''
    while True:
        confirmation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if confirmation == 'y':
            first_number = result
            operand = get_valid_operand()
            second_number = get_valid_number(POSITION[1])
            result = calculate_result(first_number, second_number, operand)
            print(f"{first_number:.2f} {operand} {second_number:.2f} = {result}")
        elif confirmation == 'n':
            print("\n"*100)
            print(CALCULATOR_LOGO)
            break
        else:
            print("Error: Please use 'y' or 'n' only.")

def run_calculator() -> None:
    '''
    Function to implement the calculator logic
    '''
    print(CALCULATOR_LOGO)
    result = 0
    while True:
        first_number = get_valid_number(POSITION[0])
        operand = get_valid_operand()
        second_number = get_valid_number(POSITION[1])

        result = calculate_result(first_number, second_number, operand)
        print(f"{first_number:.2f} {operand} {second_number:.2f} = {result}")
        continue_calculation(first_number, result)

def main() -> None:
    '''
    Main function to run the program
    '''
    try:
        run_calculator()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted by the user. Goodbye!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
