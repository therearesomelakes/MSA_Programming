# This file will demonstrate lists in python

def main():
    # Example of how *not* to store a bunch of items
    # nam1 = "John"
    # nam2 = "Mary"

    # Create a list of names
    names = ["John", "Mary", "Alice", "Bob"]
    list_of_integers = [10, 16, 24, 42, 14, 9]
    random_data_type_list = ["Cyd", 15, 22.3, "Frank"]
    list_of_lists = [names, list_of_integers, random_data_type_list]
    print(names)
    print(random_data_type_list)
    print(list_of_lists)

    # Adding an item to the names list
    names.append("Winter")
    print(names)

    # Get number of items in a list
    number = len(list_of_lists)
    print(f"Number of items in list_of_lists is {number}.")

    # Get values from lists
    print(f"First integer in the list is {list_of_integers[0]}")
    print(f"First item in the first item of the list of lists is {list_of_lists[0][0]}")
    print("All items in list of integers:", end=" ")
    for item in list_of_integers:
        if list_of_integers.index(item) == len(list_of_integers) - 1:
            print(item)
        else:  
            print(item, end=", ")
    for item in range(len(list_of_integers)):
        print(f"Item {item} is {list_of_integers[item]}")
main()