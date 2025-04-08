def tip_calculator(total_bill: float, tip_received: float, split_people_count: float) -> float:
    '''
    Function to calculate the cost per head with tip
    '''
    if total_bill < 0 or tip_received < 0:
        raise Exception("Bill and tip amounts cannot be negative!")
    if tip_received not in [10, 12, 15]:
        raise Exception("Tip must be $10, $12, or $15!")
    if split_people_count < 0:
        raise Exception("Number of people must be postive!")
    
    combined_bill: float = total_bill + tip_received
    new_bill_per_person: float = (combined_bill/split_people_count)
    return new_bill_per_person

def main() -> None:
    '''
    Main function to run the program
    '''
    print("Welcome to the tip calculator")
    try:
        total_bill = float(input("What was your total bill?\nBill amount($): "))
        tip_received = float(input("How much tip would you like to give?\nChoose $10, $12, or $15\nTip amount($): "))
        split_bill_count = float(input("How many people to split the bill?\nPeople count: "))

        final_amount_per_person = tip_calculator(total_bill, tip_received, split_bill_count)
        print(f"Each person should pay: ${final_amount_per_person:.2f}")
    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted by user. Goodbye!")

if __name__ == "__main__":
    main()
    