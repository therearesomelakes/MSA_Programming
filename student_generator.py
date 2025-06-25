from Student import Student
from datetime import datetime

# Read students.csv
# Clean data (get rid of any lines that don't make sense)
    # Not enough data points, too many data points (6 is the right amount)
    # GPA is not a float, credit hours is a whole integer
# Use the rest of the lines to create Student objects
# Place the objects into a list of students
# Use a for loop to print student data

'''
Function to write an error message to a log file
Input: (string) error message
Output: None
'''
def write_to_error_log(message:str) -> None:
    # Open log file in append mode: error_log.txt
    error_writer = open("error_log.txt", "a")
    # Write error in the format
    # Date: message
    # Ex: 6/24/2025: Error in datafile on line 5
    current_date = datetime.now()
    error_writer.write(f"{current_date.month}/{current_date.day}/{current_date.year}: {message}\n")
    # close file
    error_writer.close()

'''
Function to make sure that a line of student data is proper
Input: line_of_data
Output: either -1 or Student object, depending on if it is improper or proper
'''
def convert_line_to_student(line_of_data:str):
    # Turn the line into its components
    list_of_data = line_of_data.split(",")

    # Check if there are 6 components
    if len(list_of_data) != 6:
        return "Did not get 6 items on line"
    
    # Try to convert credit hours into an integer; if fails, return -1
    # Try to convert GPA into a float; if fails, return -1
    try:
        list_of_data[3] = int(list_of_data[3])
    except:
        return "Credit hours not an integer on line"
    
    try:
        list_of_data[4] = float(list_of_data[4])
    except:
        return "GPA not a number on line"
    
    # Check if credit hours and gpa are proper 
    # Credit hours are non-negative
    # GPA is between 0 and 4 inclusive
    if not(list_of_data[3] >= 0):
        return "Negative credit hours on line"
    
    if not(0 <= list_of_data[4] <= 4):
        return "GPA out of bounds on line"
    
    # Get rid of new line character
    list_of_data[5] = int(list_of_data[5])
    
    # Convert list_of_data into a Student object
    student = Student(list_of_data[0], list_of_data[1], list_of_data[2], list_of_data[3], list_of_data[4], list_of_data[5])
    return student
    

def main():
    # Open the file in read mode
    student_file = open("students.csv", "r")

    # Empty students list to be filled later.  : list[Student] makes it so that it is suggested to fill the list with Students, but not required
    students: list[Student] = []

    # Creates Student object for each line of data
    # If the function returns -1, ignore the line
    line_number = 0
    for line_of_data in student_file:
        line_number +=1
        # To skip the header
        if line_number == 1:
            continue

        student = convert_line_to_student(line_of_data)
        # Only outputs a string when something is wrong
        if type(student) == str:
            write_to_error_log(f"ERROR: {student} {line_number}")
            continue

        # Print student data
        student.print_student_data()
        print("")
        students.append(student)

    # Close the data file
    student_file.close()



main()
