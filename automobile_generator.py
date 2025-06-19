# From the file named Automobile, import the class Automobile
from Automobile import Automobile

def main():
    # Create instances of Automobile
    auto1 = Automobile("Honda", "Accord", "23456", 2.2, "Alice", 2017, "Blue")
    auto2 = Automobile("Ferrari", "F-50", "12345", 4.8, "Bob", 2022, "Black")

    # Change auto2 year
    # Even though the variable is "private", as marked by the leading "__", it can still be accessed and changed
    # Python uses name mangling to make it not just "__year" but instead "_Automobile__year"
    # Thus, while it can still be changed, it is difficult to change on accident
    auto2._Automobile__year = 2000
    # Change auto1 owner
    auto1.set_owner("Enzo")

    auto2.set_colour("Red")

    auto_list = []
    auto_list.append(auto1)
    auto_list.append(auto2)

    # Print automobile data
    for car in auto_list:
        car.print_data()

    print(f"Auto 1 is {auto1.get_age()} years old")

main()
