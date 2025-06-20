import random

def main():
    # Create a random number generator
    random_generator = random.Random()
    print(random_generator.randint(1,10))

    # Generate 20 random numbers
    print("Generate 20 random numbers")
    for i in range(20):
        print(random_generator.randint(1,100))

main()