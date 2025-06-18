'''
Function to load menu item and price into a dictionary
Inputs: file name
Outputs: dictionary
'''
def get_file_dictionary(file_name: str) -> dict:
    # Open file.txt: Create a file handler in read mode
    data_file = open(file_name, "r")
    
    # Create an empty dictionary to store item:price entries
    menu_items = {}

    # Use a loop to read the contents of the file line by line
    for line_of_data in data_file:
        # Split the data at the comma
        item_name_and_price = line_of_data.split(",")
        # Get the menu item and price from the list
        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])
        # Create an entry in the dictionary for the item and price
        menu_items[item_name] = item_price
    data_file.close()
    return menu_items
    
def display_cart(cart:dict, menu_items:dict) -> None:
    # Loop through cart
    for item, quantity in cart.items():
        
        print(f"{quantity} {item}(s) @ ${menu_items[item]:.2f} each: ${(menu_items[item] * quantity):.2f}")

def main():
    menu_items = get_file_dictionary("file.txt")
    total_cost = 0
    # Create a cart dictionary
    item_cart = {}
    
    # While loop to keep user ordering
    # Check whether input is a key
    # Keep a total value of cost
    # Check whether input is "end" in any case
    while True:
        # Prompt user for input
        # Item
        order = input("Item: ").title()
        # Break loop if user types end
        if order == "End":
            print()
            break
        # Check if order is valid (don't necessarily need the .keys(); can just have "in menu_items")
        elif order not in menu_items.keys():
            print(f"Error: {order} is not on the menu\n")
            continue

        # Quantity
        try:
            quantity = int(input("Quantity: "))
            if quantity < 1:
                print("ERROR: Enter a positive number for quantity\n")
                continue
        except:
            print("ERROR: Enter number for quantity\n")
            continue

        # Add item into cart (don't necessarily need the .keys(); can just have "in item_cart")
        if order in item_cart.keys():
            item_cart[order] += quantity
        else:
            item_cart[order] = quantity
        # Add cost to total cost
        total_cost += menu_items[order] * quantity
        print(f"Total: ${total_cost:.2f}\n")

    # Print out card
    display_cart(item_cart, menu_items)
    print(f"Total: ${total_cost}")


main()