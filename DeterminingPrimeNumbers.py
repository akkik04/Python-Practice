def find_prime(number):

    if (number % 2 != 0):
        return 'This is a prime number'
    
    return 'This is not a prime number'
    
number = int(input("Enter the number you would like to check please: "))

print(find_prime(number))