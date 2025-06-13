# Funtion to add 3 numbers; input: (int) number1, (int) number2, (int) number3; output: (int) total
def add_numbers(number1, number2, number3):
    total = number1 + number2 + number3
    c = 18
    return total


def main():
    a = 5
    b = 4
    c = 3

    # Call the add_numbers function and assign the returned value to answer
    answer = add_numbers(a,b,c)
    print(f"{a} + {b} + {c} = {answer}")
    print(f"Variable c = {c}")


main()