# Get input from user and make sure it is in the right format
#   Number, non-negative, less than or equal to 24

# Multiply hours worked by hourly wage by 350 days by tax (12% reduction)
# Print the a Pay Advice containing:

    # hours worked
    # hourly wage
    # wages before taxes
    # tax amount
    # annual wages after taxes
    # money values should be printed with a $ sign and all numbers should be rounded to 2 decimal places

# Use previously made function to get positive float input.  Modify to make it <=24 hours
def get_positive_float_input(question):
    # GET INPUT FROM THE USER
    # Convert weight to a float
    # Validate that the input was a number
    # if the weight is not a number, then reprompt the user until the input is correct
    while True:
        try: 
            number = float(input(question))
            # Make sure that the number is positiver
            if (number <= 0): 
                print("Please give a positive number")
                continue
            else:
                break
        except:
            print("ERROR: Please enter just a numerical value")
    return number


# Calculate yearly wage without including taxes
def calculate_yearly_wage(hours, hourly_wage, days):
    return hours * hourly_wage * days


# Takes yearly wage to get amount after taxes
def apply_taxes(yearly_wage, tax):
    return yearly_wage * (1 - tax)


# Gives pay advice and calculations
def calculation():
    #INPUT
    # Get input from user
    # if the input for hours worked is greater than 24 hours, run the function again
    while True:
        daily_hours = get_positive_float_input("Enter the number of hours worked daily: ")
        if daily_hours <= 24:
            break
        else:
            print("Please ensure your daily hours do not exceed 24.")
    hourly_wage = get_positive_float_input("Enter your hourly wage: ")

    # Define tax and days worked
    tax = 0.12
    days_worked = 350

    #CALCULATIONS
    # Calculate yearly wage
    yearly_wage = calculate_yearly_wage(daily_hours, hourly_wage, days_worked)

    # Apply taxes
    taxed_yearly_wage = apply_taxes(yearly_wage, tax)

    # Round values to 2 decimal points
    yearly_wage = round(yearly_wage, 2)
    taxed_yearly_wage = round(taxed_yearly_wage, 2)

    # Calculate tax amount
    tax_amount = yearly_wage - taxed_yearly_wage

    # Print result in a nice way
    print()
    print("Pay advice")
    print("--------------------")
    print(f"Hours worked: {daily_hours:.2f}")
    print(f"Hourly wage: ${hourly_wage:.2f}")
    print(f"Annual wage before taxes: ${yearly_wage:.2f}")
    print(f"Tax amount: ${tax_amount:.2f}")
    print(f"Annual wage after taxes: ${taxed_yearly_wage:.2f}")


#Prompts user if they want to do another calculation
def repeat():
    while True:
        response = input("Do you want to run the calculation again? (Type y or n): ").lower()
        if response == "y" or response == "n":
            return response
        else:
            print("Please input \"y\" or \"n\"")


def main():
    response = "y"
    while response == "y":
        calculation()
        response = repeat()

main()