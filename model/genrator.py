import random

def generate_question():
    topics = [
        "Write a function to reverse a string.",
        "Create a program to calculate the factorial of a number.",
        "Write a Python script to check if a number is prime.",
        "Generate a Fibonacci sequence up to a given number.",
        "Write a function to sort a list using bubble sort.",
        "Create a program to find the greatest common divisor (GCD) of two numbers.",
        "Write a script to count the frequency of words in a text file.",
        "Generate a program to convert a decimal number to binary.",
        "Write a function to check if a string is a palindrome.",
        "Create a program to simulate a basic calculator."
    ]

    return random.choice(topics)

if __name__ == "__main__":
    print("Auto-Generated Question:")
    print(generate_question())