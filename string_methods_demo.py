def main():
    my_name = "steven"

    # Capitalise a string
    print(my_name.capitalize())

    # Make a string upercase
    print(my_name.upper())

    # Make a string lowercase
    last_name = "SHAW"
    print(f"{my_name.lower()} {last_name.lower()}")

    print(my_name.startswith("S") or my_name.startswith("s"))

    if (not my_name.startswith("ste") and not my_name.startswith("Ste")):
        print(f"You spelled {my_name} incorrectly")
    else:
        print(f"You spelled {my_name} correctly")

    search_letter = "ven"
    print(f"The {search_letter} is at index {my_name.find(search_letter)}")


    # Code to find the number of mentions of a word
    sentence = "I have a dog. My dog is cute. Do you wang a dog?"
    start_index = 0
    number_of_dogs = 0
    search_word = "dog"
    while True:
        dog_index = sentence.find(search_word, start_index)
        if dog_index == -1:
            break
        else:
            number_of_dogs +=1
            start_index = dog_index + 1
    print(f"\nThere are {number_of_dogs} instances of '{search_word}' in: '{sentence}'")
    

    # Split method
    car_info = "Ferrari,f-50,2021,500000,4.8"
    car_data = car_info.split(",")
    # Get individual pieces of data
    make = car_data[0]
    model = car_data[1]
    year = int(car_data[2])
    price = float(car_data[3])
    engine_size = float(car_data[4])
    print(f"{year} {make} {model}")
    print(f"Price: ${price} - Engine: {engine_size}L")


main()
