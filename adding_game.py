import random

# Create a game to give the user addition problems

'''
Function to get the game level from the user.
Inputs: none
Outputs: Level (1, 2, 3)
'''
def get_game_level() -> int:
    # while loop until user inputs something in the list of acceptable responses
    levels = range(1,4)
    while True:
        response = input(f"Enter Level 1, 2, 3: ")

        # Convert response to int
        try:
            response = int(response)
        except:
            print("Error: Invalid input!\n")
            continue
        
        # Return response if valid
        if response in levels:
            return response
        else:
            print("Error: Invalid input!\n")


'''
Function to get the number of questions to ask from the user.
Inputs: None
Outputs: Number of questions (3 through 10)
'''
def get_num_of_questions() -> int:
    question_range = range(3,11)
    # while loop until user inputs something in the list of acceptable responses
    while True:
        response = input("Enter number of questions to ask (3 to 10): ")

        # Convert response to int
        try:
            response = int(response)
        except:
            print("ERROR: Please enter an integer between 3 and 10\n")
            continue

        # Return response if valid
        if response in question_range:
            return response
        else:
            print("ERROR: Please enter an integer between 3 and 10\n")

'''
Function to create question, check if right, and also respond
Inputs: difficulty level
Output: Whether the user got it correct or not (boolean)
'''
def ask_question(difficulty:int) -> bool:
    guesses = 3

    # Use random to create a question with two random numbers of the proper difficulties
        # Can use exponentials to make sure the program is expandable to any number of difficulties
    upper_bound = 10**difficulty - 1
    if difficulty == 1:
        lower_bound = 0
    else:
        lower_bound = 10**(difficulty - 1)
    x = random.randint(lower_bound, upper_bound)
    y = random.randint(lower_bound, upper_bound)
    sum = x + y

    for i in range(guesses):
        # Ask question to the user
        # If they get it right, break the for loop and output true.  Otherwise, output false
        if input(f"{x} + {y} = ") == str(sum):
            print("CORRECT!!!\n")
            return True
        else:
            print("WRONG!!!\n")
    print(f"Correct Answer: {x} + {y} = {sum}\n")
    return False
    

def main():
    correct_answers = 0

    # Call function to get game level
    level = get_game_level()

    # Call function to get number of questions
    num_of_questions = get_num_of_questions()

    # Use for loop based on number of questions
    for i in range(num_of_questions):
        # Call function for questions using the game level
        # if correct is true, then add 1 to number of questions correct
        if ask_question(level):
            correct_answers +=1
    
    # Print out percent of questions correct
    print(f"\nYou got {correct_answers} out of {num_of_questions} questions correct on level {level}: {(correct_answers/num_of_questions * 100):.2f}%")


main()