import datetime

# Three OOP principles: Polymorphism, Inheritance, and Encapsulation
# 
# 
# Encapsulation makes it so that some properties are inaccessible or unable to be changed

class Automobile():

    # Define a constructor, which defines what happens when we create an automobile
    def __init__(self, make, model, vin, engine_size, owner, year, colour):
        # Define class properties with the parameter values
        self.__make = make
        self.__model = model
        self.__vin = vin
        self.__engine_size = engine_size
        self.__owner = owner
        self.__year = year
        self.__colour = colour

    # Create getter and setter methods
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_vin(self):
        return self.__vin
    
    def get_engine_size(self):
        return self.__engine_size
    
    def set_engine_size(self, new_size: float):
        self.__engine_size = new_size
    
    def get_owner(self):
        return self.__owner
    
    def set_owner(self, new_owner:str):
        self.__owner = new_owner
    
    def get_year(self):
        return self.__year
    
    def get_colour(self):
        return self.__colour
    
    def set_colour(self, new_colour: str):
        self.__colour = new_colour

    def print_data(self):
        print(f"{self.__year} {self.__make} {self.__model}")
        print(f"WIN: {self.__vin}, Engine Size: {self.__engine_size}")
        print(f"Owner: {self.__owner}, Colour: {self.__colour}")

    # Create a method to get the automobile's age
    def get_age(self):
        # .now() is a method and requires parenthesis, but .year is a property and doesn't
        current_date = datetime.datetime.now()
        current_year = current_date.year
        return current_year - self.__year 
