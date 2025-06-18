import random
import math

def main():
    trials = 100000000
    total_draws = 0
    for i in range(trials):
        sum = 0
        while sum < 1:
            sum += random.random()
            total_draws += 1
    avg_draws = total_draws / trials
    print(f"Number of trials conducted: {trials}")
    print(f"The experimentally calculated expected value is {avg_draws}")
    print(f"The mathematically calculated answer is e: {math.e}")
    error = abs(math.e - avg_draws)
    percent_error = error / math.e
    print(f"There is an error of {error}")
    print(f"There is a percent error of {percent_error}")


main()