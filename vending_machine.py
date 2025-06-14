# Create a vending machine that sells snacks for 50 cents
# Allow the user to input coins (1, 5, 10, 25) to fill up these 50 cents
# Output the change owed

# Specific checklist
    # Display the amount due
    # Prompt the user to enter a coin
    # Accepted denominations for coins are (1, 5, 10, 25)
    # Program should ignore any input that is not a valid input and re prompt the user to input a coin
    # Process the input and display the updated amount due
    # Once the user has inputted at least 50 cents, output how many cents in change the user is owed
    # End program


# Function to get input from user; Input: Change due; returns an int 1,5,10,25
def get_coins(change):
    acceptable_coins = ["1", "5", "10", "25"]

    # Get input from user; should check that it is an integer and is 1,5,10,25 by just checking if it is in accpetable_coins, composed of strings; If doesn't meet those conditions, reprompt;  Otherwise, return the input
    while True:
        print(f"Amount Due: {change}")
        coin = input("Insert Coin (1, 5, 10, 25): \n")
        if coin in acceptable_coins:
            return int(coin)
        else:
            print("ERROR: Please insert a valid coin value\n")
            continue
    


def main():
    # Initial value of change is the cost of the snack
    change = 50

    # Print "Vending machine"
    print("Vending Machine\n--------------------")

    # Use while loop
    while change > 0:
        # Use input function to get user input
        coin = get_coins(change)

        # If amount owed from user is negative or 0, the while loop breaks
        # Calculate the amount now owed from user
        change -= coin

    # Display change owed
    print(f"Change Owed: {-change}")
    
main()


