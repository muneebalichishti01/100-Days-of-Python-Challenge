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
        if user_choice == "encode":
            shifted_position = ALPHABET.index(letter) + user_number_of_shift
        elif user_choice == "decode":
            shifted_position = ALPHABET.index(letter) - user_number_of_shift
        shifted_position %= len(ALPHABET)
        output_text += ALPHABET[shifted_position]
        return output_text

def run_encryption_program() -> None:
    '''
    Function to run the encryptio/decryption flow
    '''
    print(CEASER_CIPHER_ASCII)

    quit_program = False
    while quit_program == False:
        encrypt_decrypt_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'quit' to quit.\nChoice: ").lower()
        user_text_message = input("Type your message.\nMessage: ").lower()
        user_number_of_shift = int(input("Type the shift number.\nShift: "))

        if encrypt_decrypt_choice == 'quit':
            quit_program = True
            print("You chose to quit the program.")
        else:
            output_text = encrypt_or_decrypt(user_text_message, user_number_of_shift, encrypt_decrypt_choice)
            print(f"Here is the {encrypt_decrypt_choice}d result: {output_text}.")
        while True:
            user_confirmation = input("Enter 'yes' to go again, enter 'quit' to quit program.\nChoice: ").lower()
            if user_confirmation == 'yes':
                break
            else:
                print("Choose a valid option.")
            break

def main() -> None:
    '''
    Main function to run the program
    '''
    try:
        run_encryption_program()
    except (KeyboardInterrupt, EOFError):
        print("\nError: Program interrupted by user. Goodbye!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
