def BandNameGenerator(cityName, petName):
    '''
    Function concatinates 2 variables together to give a unique name
    '''
    bandName = cityName + " " + petName
    return bandName

def main():
    '''
    Main function that runs program
    '''
    print("Welcome to the Band Name Generator")
    cityName = input("What's the name of the city you grew up in:\n")
    petName = input("What's your pet's name?\n")
    bandName = BandNameGenerator(cityName, petName)
    print(f"Your band name could be {bandName}!")

if __name__ == "__main__":
    main()
    