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
    

def main():
    menu_items = get_file_dictionary("file.txt")
    total_cost = 0
    
    # While loop to keep user ordering
    # Check whether input is a key
    # Keep a total value of cost
    # Check whether input is "end" in any case
    while True:
        order = input("Item: ")
        order = order.title()
        if order in menu_items.keys():
            total_cost += menu_items[order]
            print(f"Total: ${total_cost:.2f}")
        elif order.lower() == "end":
            break




main()