# Function to get input from user about month; Inputs: none; Outputs: (int) month_number
def get_month_number():
    # Validate the input is 1-12
    # Reprompt user if input is invalid
    while True:
        try:
            month_number = int(input("What month is it (1-12): "))
            if 1 <= month_number <= 12:
                break
            else:
                print("ERROR: Please input a number 1-12 for the month")
            continue
        except:
            print("ERROR: Please input a number 1-12 for the month")
    return month_number
    
# Function to output season name; Inputs: (int) number of the month; Outputs: (str) season name
# Having :int makes it so that it signals to the programmer that month_number should be an int
def get_season_name(month_number:int):
    if 3 <= month_number <= 5:
        season = "Spring"
    elif 6 <= month_number <= 8:
        season = "Summer"
    elif 9 <= month_number <= 11:
        season = "Autumn"
    else:
        season = "Winter"
    return season

# Function to output season name; Inputs: (int) number of the month; Outputs: (str) season name
def get_season_name_2(month_number:int):
    if month_number in [3,4,5]:
        season = "Spring"
    elif month_number in [6,7,8]:
        season = "Summer"
    elif month_number in [9,10,11]:
        season = "Autumn"
    else:
        season = "Winter"
    return season


def main():
    # Call get_month_number to prompt and get month number from user
    # Call get_season_name to get name of season based on number
    # Print output
    # Ask the user if they want to run the program again
    # If y or Y, rerun the program.  Otherwise, end the program.
    while True:
        month_number = get_month_number()
        season_name = get_season_name(month_number)
        print(f"The currrent season is {season_name}")
        rerun = input("\nWould you like to rerun this program? \n(Type y if you would): ").lower()
        if rerun != "y":
            break


main()