class Student():
    
    # Create an instance
    def __init__(self, first_name, last_name, major, credit_hours, gpa, id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__id = id

    # Get and set methods
    # Only ID doesn't have a set method
    def get_first_name(self) -> str:
        return self.__first_name
    
    def set_first_name(self, changed_first_name:str):
        self.__first_name = changed_first_name
    
    def get_last_name(self) -> str:
        return self.__last_name
    
    def set_last_name(self, changed_last_name:str):
        self.__last_name = changed_last_name
    
    def get_major(self) -> str:
        return self.__major
    
    def set_major(self, changed_major:str):
        self.__major = changed_major
    
    def get_credit_hours(self) -> int:
        return self.__credit_hours
    
    def set_credit_hours(self, changed_credit_hours:int):
        self.__credit_hours = changed_credit_hours
    
    def get_gpa(self) -> float:
        return self.__gpa
    
    def set_gpa(self, changed_gpa:float):
        self.__gpa = changed_gpa
    
    def get_id(self) -> str:
        return self.__id
    
    # Additional methods
    # To get class level based on credit hours
    def get_class_level(self):
        if self.__credit_hours <= 30:
            return "Freshman"
        elif self.__credit_hours <= 60:
            return "Sophomore"
        elif self.__credit_hours <= 90:
            return "Junior"
        else:
            return "Senior"
    
    # To add additional credit hours
    def update_credit_hours(self, additional_hours:int):
        self.__credit_hours += additional_hours
    
    # To print all of the student's data
    def print_student_data(self):
        print(self.__first_name, self.__last_name)
        print(f"Class level: {Student.get_class_level(self)}, Major: {self.__major}")
        print(f"GPA: {self.__gpa:.2f}, ID: {self.__id}")

    