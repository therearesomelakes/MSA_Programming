# This file will demonstrate the workings of a for loop

def main():
    # Print integers between 0 and 10
    # Range is numbers up to 11 (exclusive).  Default start is 0 (inclusive) and default step is 1.
    # Alternatively, you can use an array/list, and the variable will equal each value in the array
    print("Numbers 1 through 10")
    for i in range(11):
        print(i)
    
    # Print integers between 5 and 10
    print("\n\nNumbers 5 through 10")
    for i in range(5,11):
        print(i)

    # Print evens between 0 and 10
    print("\n\nEven numbers 0 through 10")
    for i in range(0,11,2):
        print(i)

    #Print odds between 0 and 10
    print("\n\nOdd numbers 0 through 10")
    for i in range(1,11,2):
        print(i)
    
    # Prompt user for start and stop values
    # Print the numbers between start and stop
    # Get values, convert to integers
    start = int(input("What number do you want to start (inclusive) at: "))
    stop = int(input("What number do you want to stop (inclusive) at: "))
    print(f"Output numbers {start} through {stop}")
    for i in range(start, stop+1):
        print(i)

    # Use nested for loops to print multiplication tables from user input (User will provide start and stop)
    start = int(input("Where do you want your multiplcation table to start: "))
    stop = int(input("Where do you want your multiplcation table to stop: "))
    print(f"\nDisplaying multiplication tables from 1 through 12 between {start} and {stop}")
    for i in range(start,stop+1):
        print(f"Displaying the {i} multiplication table")
        for n in range(1, 13):
            if n == 12:
                print(f"{i} x {n} = {i*n}")
            else:
                print(f"{i} x {n} = {i*n}", end=", ")


main()