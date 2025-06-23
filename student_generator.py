from Student import Student

# Read students.csv
# Clean data (get rid of any lines that don't make sense)
    # Not enough data points, too many data points (6 is the right amount)
    # GPA is not a float, credit hours is a whole integer
# Use the rest of the lines to create Student objects
# Place the objects into a list of students
# Use a for loop to print student data

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
        return -1
    
    # Try to convert credit hours into an integer; if fails, return -1
    # Try to convert GPA into a float; if fails, return -1
    try:
        list_of_data[3] = int(list_of_data[3])
        list_of_data[4] = float(list_of_data[4])
    except:
        return -1
    
    # Check if credit hours and gpa are proper 
    # Credit hours are non-negative
    # GPA is between 0 and 4 inclusive
    if not(list_of_data[3] >= 0) or not(0 <= line_of_data[4] <= 4):
        return -1
    
    # Convert list_of_data into a Student object
    student = Student(list_of_data[0], list_of_data[1], list_of_data[2], list_of_data[3], list_of_data[4], list_of_data[5])
    return student
    

def main():
    # Open the file in read mode
    student_file = open("students.csv", "r")
    
    # The first line is just the header, so skip it
    student_file.readline()

    # Empty students list to be filled later
    students = []

    # Creates Student object for each line of data
    # If the function returns -1, ignore the line
    for line_of_data in student_file:
        student = convert_line_to_student(line_of_data)
        if student == -1:
            continue
        # Print student data
        student.print_student_data()
        students.append(student)

    # Close the data file
    student_file.close()



main()