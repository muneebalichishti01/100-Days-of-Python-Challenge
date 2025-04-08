def band_name_generator(city_name: str, pet_name: str) -> str:
    '''
    Function concatenates 2 variables together to give a unique name
    '''
    band_name: str = city_name + " " + pet_name
    return band_name

def main() -> None:
    '''
    Main function that runs program
    '''
    print("Welcome to the Band Name Generator")
    try:
        city_name = input("What's the name of the city you grew up in:\n")
        pet_name = input("What's your pet's name?\n")
        band_name = band_name_generator(city_name, pet_name)
        print(f"Your band name could be {band_name}!")
    except (KeyboardInterrupt, EOFError):
        print("\Program interrupted by user. Goodbye!")

if __name__ == "__main__":
    main()
    