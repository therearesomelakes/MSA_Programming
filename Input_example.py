# Write a pound to kilogram converter
# A user will be prompted for their weight in pounds and the program will output it into kilograms

# Beginning code before example
# Gather input
#     poundsstr = input("What is your weight in pounds: ")
# Convert input string -> float
#     poundsflt = float(poundsstr)
# Print and convert to kilos
#     print("Your weight in kilograms is", 0.4536 * poundsflt) 



# Class process
def get_positive_float_input():
    # GET INPUT FROM THE USER
    # Convert weight to a float
    # Validate that the input was a number
    # if the weight is not a number, then reprompt the user until the input is correct
    while True:
        try: 
            user_weight = float(input("What is your weight in pounds: "))
            # Make sure that the number is positiver
            if (user_weight <= 0): 
                print("Please give a positive number")
            else:
                break
        except:
            print("ERROR: Please enter just a numerical value")
    return user_weight

def convert_lbs_to_kg(lbs):
    # PROCESSING
    # Use a conversion to convert lbs to kilos: 2.205 lbs = 1 kg
    LBS_TO_KG_CONVERSION = 2.205
    kg = lbs/2.205
    return kg

def output_nicely(output):
    # OUTPUT
    # Print the output to the user in a nice format (to two decimals)
    print(f"You weigh {output:.2f} kg.")

def main():
    user_weight = get_positive_float_input()
    user_weight_in_kg = convert_lbs_to_kg(user_weight)
    output_nicely(user_weight_in_kg)
    
# Call the main function
main()