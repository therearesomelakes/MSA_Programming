# This file demosntrates decision structures and conditions

def main():
    a = 7
    b = 4
    
    # Exploring conditions
    print(f"A is greater than B: {a > b}")
    print(f"B is greater than A: {b > a}")

    # Create decision structure to determine if a and b are equal
    if a>b:
        print("a is larger than b")
    elif a==b:
        print("a is equal to b")
    else:
        print("a is less than b")

    # Create a decision structure to print a letter grade based on a test score
    grade = 130
    if grade > 100:
        letter = "INVALID"
    elif grade >= 90:
        letter = "A"
    elif grade >= 80:
        letter = "B"
    elif grade >= 70:
        letter = "C"
    elif grade >= 60:
        letter = "D"
    elif grade >= 0:
        letter = "F"
    else:
        letter = "INVALID"
    print(f"The letter grade for this test score is a(n): {letter}")

    # Create a decision structure to determine the season: Winter, Spring, Summer, Autumn
    # Ask the user to enterthe number of the month and based on the number, determine the season
    # Winter is 12-2, Spring is 3-5, Summer is 6-8, Autumn is 9-11

    # Input
    while True:
        try:
            month = int(input("What month is it (1-12): "))
            if 1 <= month <= 12:
                break
            else:
                print("ERROR: Please input a number 1-12 for the month")
            continue
        except:
            print("ERROR: Please input a number 1-12 for the month")
    # Decision structure
    if 3 <= month <= 5:
        season = "Spring"
    elif 6 <= month <= 8:
        season = "Summer"
    elif 9 <= month <= 11:
        season = "Autumn"
    else:
        season = "Winter"
    print(f"The current season is {season}")


main()
