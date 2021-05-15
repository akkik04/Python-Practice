def find_prime(number):
    
    # if-statement to determine if the number is prime.
    if (number % 2 != 0):
        return 'This is a prime number'
    
    # returning not prime if number does not meet requirements.
    return 'This is not a prime number'

# code to prompt the use for a number.
number = int(input("Enter the number you would like to check please: "))

# printing the output.
print(find_prime(number))
