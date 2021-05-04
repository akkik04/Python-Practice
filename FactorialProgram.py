# AKSHITH KANDIVANAM

# importing the math module for the 'factorial' function.
import math 

# defining a function as factorial with a parameter 'x'.
def factorial(x):

    return (math.factorial(x))

# prompting the user to enter a number to find its factorial.
user_num = int(input("Enter a number to find the factorial please: "))

# code to print final output indicating the factorial.
print("The factorial of ", user_num , " is", factorial(user_num),".")