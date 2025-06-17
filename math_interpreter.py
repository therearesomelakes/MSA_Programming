# Prompt user for input

# Split input by spaces to get [int, operation (str), int]
# # Set up function for determining if there is an incorrect format

# First, determine if list length is 3
# Then, use try except to determine if first and last are ints
# Finally, make sure operation is within list of valid operations
# If not, output "Incorrect format" and reprompt

# Set up decision block based on operation
# In decision block, perform operation on the ints
# Outputs result as a float rounded to 1 decimal place


def main():
    # Prompt the user for an expression and check input
    while True:
        expression = input("Enter the math expression you wish to calculate: ")
        expression = expression.split()

        # First, determine if list length is 3
        if len(expression) != 3:
            print("ERROR: Please make sure you have exactly two spaces (before and after the operator)")
            continue

        # Then, use try except to determine if first and last are ints
        try:
            expression[0] = int(expression[0])
            expression[2] = int(expression[2])
        except:
            print("ERROR: Please ensure your two numbers are integers")
            continue

        # Finally, make sure operation is within list of valid operations
        if expression[1] not in ["+", "-", "*", "/"]:
            print("ERROR: Please ensure your operation is valid (+, -, *, /)")
            continue
    
        # if elif block to determine which operation is to be used and apply it
        if expression[1] == "+":
            result = expression[0] + expression[2]
        elif expression[1] == "-":
            result = expression[0] - expression[2]
        elif expression[1] == "*":
            result = expression[0] * expression[2]
        else:
            if expression[2] == 0:
                print("ERROR: You cannot divide by 0")
                continue
            result = expression[0] / expression[2]

        # Print result (rounded to 1 decimal)
        print(f"{expression[0]} {expression[1]} {expression[2]} = {result:.1f}")
        break


main()
