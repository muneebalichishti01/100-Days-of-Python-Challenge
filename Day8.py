# Define the constants
CEASER_CIPHER_ASCII = '''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88

                                   88                                 
                                   88                                 
                                   88                                 
 ,adPPYba, 8b       d8 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" `8b     d8' 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b          `8b   d8'  88       d8 88       88 8PP""""""" 88          
"8a,   ,aa   `8b,d8'   88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"'     Y88'    88`YbbdP"'  88       88  `"Ybbd8"' 88          
               d8'     88                                             
              d8'      88                                                       
'''
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt_or_decrypt(user_text_message: str, user_number_of_shift: int, user_choice: str) -> str:
    '''
    Function to encrypt or decrypt the messsage as per user choice
    '''
    output_text = ""
    for letter in user_text_message:
        if letter in ALPHABET:
            if user_choice == "encode":
                shifted_position = ALPHABET.index(letter) + user_number_of_shift
            elif user_choice == "decode":
                shifted_position = ALPHABET.index(letter) - user_number_of_shift
            shifted_position %= len(ALPHABET)
            output_text += ALPHABET[shifted_position]
        else:
            output_text += letter
    return output_text

def run_caeser_cipher_program() -> None:
    '''
    Function to run the encryption/decryption program logic flow
    '''
    print(CEASER_CIPHER_ASCII)

    continue_program = True
    while continue_program:
        encrypt_decrypt_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'quit' to quit.\nChoice: ").lower()
        if encrypt_decrypt_choice == 'quit':
            print("You chose to quit the program.")
            break
        elif encrypt_decrypt_choice not in ["encode", "decode"]:
            print("Error: Please type 'encode', 'decode', or 'quit'.")
            continue
        user_text_message = input("Type your message.\nMessage: ").lower()
        user_number_of_shift = int(input("Type the shift number.\nShift: ").strip())
        if user_number_of_shift < 0:
            print("Error: Shift must be a non-negative number.")
        result_text = encrypt_or_decrypt(user_text_message, user_number_of_shift, encrypt_decrypt_choice)
        print(f"Here is the {encrypt_decrypt_choice}d result: {result_text}.")
        
        replay_confirmation = input("Enter 'yes' to go again, 'no' to quit.\nChoice: ").lower()
        if replay_confirmation != 'yes':
            print("You chose to quit the program.")
            continue_program = False

def main() -> None:
    '''
    Main function to run the program
    '''
    try:
        run_caeser_cipher_program()
    except (KeyboardInterrupt, EOFError):
        print("\nError: Program interrupted by user. Goodbye!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
