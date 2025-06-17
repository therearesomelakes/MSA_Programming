'''
Function to get valid expression inputs from the user
Input: none
Output: (int) X, (int) Z, (str) Y
'''
def get_valid_expression_inputs():
    while True:
        expression = input("Enter the math expression you wish to calculate: ")
        expression = expression.split()

        # First, determine if list length is 3
        if len(expression) != 3:
            print("ERROR: Please make sure you have exactly two spaces (before and after the operator)")
            continue
        x, y, z = expression

        # Then, use try except to determine if first and last are ints
        try:
            x = int(x)
            z = int(z)
        except:
            print("ERROR: Please ensure your two numbers are integers")
            continue

        # Finally, make sure operation is within list of valid operations
        if y not in ["+", "-", "*", "/"]:
            print("ERROR: Please ensure your operation is valid (+, -, *, /)")
            continue
        if y == "/" and z == 0:
            print("ERROR: You cannot divide by 0")
            continue
        break
    return x, y, z

'''
Function to evaluate expression
Input: x, y, z
Output: (flt) answer
'''
def evaluate_expression(x: int, y: str, z: int):
    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    else:
        result = x / z
    return result

def main():
    while True:
        # call the get_valid_expression_inputs function to get x, y, and z
        x, y, z = get_valid_expression_inputs()
        
        # call evaluate_expreeion function to get the answer
        answer = evaluate_expression(x, y, z)

        # print the answer
        print(f"{x} {y} {z} = {answer:.1f}")

        # ask the user if they want to evaluate another expression
        if input("Do you want to rerun the program? (Type y if so): ").lower() != "y":
            break

main()