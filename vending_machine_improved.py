# Challenge?? take previous vending machine program and make it so that it:
# Outputs the change in coin amounts
# Asks the user if they want to buy another snack

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

# Function to turn the cents into coin values (1,5,10,25); inputs: change; ouputs: list of coin values due that add up to change owed
def cents_to_coins(cents):
    acceptable_coins = [1, 5, 10, 25]

    cents_in_coins = []
    # Goes through acceptable_coins from greatest value to least
    # Checks whether the greatest value can fit into cents owed
    # If so, adds it to the list of coin values due
    for i in range(len(acceptable_coins)):
        while cents >= acceptable_coins[len(acceptable_coins)-1-i]:
            cents_in_coins.append(acceptable_coins[len(acceptable_coins)-1-i])
            cents -= acceptable_coins[len(acceptable_coins)-1-i]
    return cents_in_coins

def main():
    run_again = "y"
    while run_again == "y":
        # Initial value of change is the cost of the snack
        change = 50

        # Print "Vending machine"
        print("\nVending Machine\n--------------------")

        # Use while loop
        while change > 0:
            # Use input function to get user input
            coin = get_coins(change)

            # If amount owed from user is negative or 0, the while loop breaks
            # Calculate the amount now owed from user
            change -= coin

        # Display change owed
        print(f"Change Owed: {-change}")
        # Call change_in_coins() to turn change into coins
        change_in_coins = cents_to_coins(-change)
        # Display change owed in coin amounts
        print(f"This change whil be given using: {change_in_coins}")
        run_again = input("Would you like another snack? (Type y if so): ").lower()

    
main()


