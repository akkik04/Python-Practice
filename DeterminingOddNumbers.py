def find_odd(number):
    
    # if-statement to determine if the number is odd.
    if (number % 2 != 0):
        return 'This is an odd number'
    
    # returning not odd if number does not meet requirements.
    return 'This is not an odd number'

# code to prompt the user for a number.
number = int(input("Enter the number you would like to check please: "))

# printing the output.
print(find_odd(number))
