# Print hello world
print("hello world")

# Create a variable to store my name
first_name = "Steven"
last_name = "Shaw"

# print first name
print("My name is " + first_name)

print("My full name is", first_name, last_name, sep="---")

# variables to store age, height, and weight
age = 15
height = 68
weight = 145.5

# f allows for things like {first_name} to be directly put in, and \n creates a line break
# f is called string interpolation (fstring)
# Putting the {} puts the variables into strings and allows you to smoothly put concatenate
print(f"My name is {first_name} {last_name}\nI am {age} years old and I weigh {weight} lbs")

# finding out data types
print(type(weight))

# Using string interpolation print(f) and type() to print out variables and variable types
print(f"Variable {age} (age) is {type(age)}")
print(f"Variable {height} (height) is {type(height)}")
print(f"Variable {weight} (weight) is {type(weight)}")

# Operations
number_1 = 5
number_2 = 7
total = number_1 + number_2
print(f"Total is {total}")

number_1 = "5"
number_2 = "7"
total = number_1 + number_2
print(f"Total is {total}")

