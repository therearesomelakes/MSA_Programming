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
    grade = 67
    if grade >= 90:
        letter = "A"
    elif grade >= 80:
        letter = "B"
    elif grade >= 70:
        letter = "C"
    elif grade >= 60:
        letter = "D"
    else:
        letter = "F"
    print(f"The letter grade for this test score is a(n): {letter}")

main()