def BandNameGenerator(cityName: str, petName: str) -> str:
    '''
    Function concatenates 2 variables together to give a unique name
    '''
    bandName: str = cityName + " " + petName
    return bandName

def main():
    '''
    Main function that runs program
    '''
    print("Welcome to the Band Name Generator")
    try:
        cityName = input("What's the name of the city you grew up in:\n")
        petName = input("What's your pet's name?\n")
        bandName = BandNameGenerator(cityName, petName)
        print(f"Your band name could be {bandName}!")
    except (KeyboardInterrupt, EOFError):
        print("\Program interrupted by user. Goodbye!")

if __name__ == "__main__":
    main()
    