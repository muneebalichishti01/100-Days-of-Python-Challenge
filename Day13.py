def debug_code_learning() -> None:
    '''
    Function to state/implement main functionality
    '''
    print("DEBUGGING PRACTICES DONE")

def main() -> None:
    '''
    Main function to run the program
    '''
    try:
        debug_code_learning()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram inyerrupted by the user. Goodbye!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
