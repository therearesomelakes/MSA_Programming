def main():
    # The need for dictionaries
    
    scores = [55, 75, 87, 82, 91]
    students = ["Alice", "Bob", "Jerry", "Jane", "Bill"]
    
    # Print student name and score together
    for index in range(len(students)):
        print(f"{students[index]}: {scores[index]}")

    # Create a dictionary of names and scores
    # Note: Entries don't have to be on multiple lines, but it is that way here for readability
    # Each entry is composed of Key: Value
    student_scores = {
        "Alice": 55,
        "Bob": 75,
        "Jerry": 87,
        "Jane": 82,
        "Bill": 91
    }
    print(student_scores["Bob"])
    print(student_scores["Alice"])

    # Print all student data in student_scores
    for student in student_scores:
        print(f"{student}: {student_scores[student]}")

    # Create a car dictionary to store the make, model, year, value, and engine size
    car_1 = {"make": "Ferrari", "model": "F-50", "year": 2021, "value": 500000, "engine": 4.8}

    # Get all my car information
    print("\nGet the car information")
    # Doesn't necessarily have to be called key and value
    for key, value in car_1.items():
        print(f"{key}: {value}")
    
    # Create a list of dictionaries
    car_2 = {"make": "Honda", "model": "Accord", "year": 2015, "value": 15000}
    dictionary_list = [car_1, car_2]

    print("\nDisplay all cars information")
    for car in dictionary_list:
        print(f"Information for car: {dictionary_list.index(car) + 1}")
        for feature, value in car.items():
            print(f"{feature}: {value}")

    print("\n\n")

    # Create a dictionary of dictionaries
    car_dictionary = {"Ferrari": car_1, "Honda": car_2}
    # Write a for loop to display car information
    for car in car_dictionary:
        print(f"Information on car: {car}")
        for feature, value in car_dictionary[car].items():
            print(f"{feature}: {value}")


main()