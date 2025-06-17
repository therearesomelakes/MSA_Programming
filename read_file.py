def main():
    # Open file.txt: Create a file handler in read mode
    data_file = open("file.txt", "r")
    
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
        
    print(menu_items)




main()