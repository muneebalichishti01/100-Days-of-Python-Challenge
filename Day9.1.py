# Define the constants
BIDDING_LOGO = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
BIDDING_DICT = {}

def get_user_name() -> str:
    '''
    Function to get the user name as a string with valid checks
    '''
    while True:
        user_name = input("What is your name?\nEnter Name: ").lower()
        if not user_name.isalpha():
            print("Enter your name using alphabetic characters only (no digits or special characters).")
        else:
            return user_name

def get_user_bid() -> int:
    '''
    Function to get the valid user bid as an integer with valid checks
    '''
    while True:
        try:
            user_bid = int(input("What is your bid?\nEnter Bid: $").strip())
            if user_bid <= 0:
                print("Bid must be a positive number. Enter at least $1.")
            else:
                return user_bid
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def run_bid_logic(bidding_dict: dict) -> None:
    '''
    Function to determine the highest bidder and their bid
    '''
    if not bidding_dict:
        print("No bids have bee placed.")
        return
    
    highest_bidder = None
    highest_bid = 0

    for bidder, bid in bidding_dict.items():
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = bidder
    print(f"Highest Bidder is {highest_bidder} with a bid of ${highest_bid}.")

def bidder() -> None:
    '''
    Function for main implementation of bidding system
    '''
    print("\n"*2)
    print(f"{BIDDING_LOGO}\n\nWelcome to the secret auction program.")
    while True:
        user_name = get_user_name()
        user_bid = get_user_bid()
        BIDDING_DICT[user_name] = user_bid

        bid_confirmation = input("Are there any other bidders? Type 'yes' or 'no'.\nChoice: ").lower()
        if bid_confirmation == "yes":
            print("\n" * 100)
            print("Enter your information below.")
            continue
        elif bid_confirmation == "no":
            print("Bidding is over. Here are the results:")
            run_bid_logic(BIDDING_DICT)
            break
        else:
            print("Enter from the given choice only: yes or no.")

def main() -> None:
    '''
    Main function to run the program
    '''
    try:
        bidder()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram inturrupted by user. Goodbye!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
