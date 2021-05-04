# AKSHITH KANDIVANAM

# receiving input from the user.
str = input("Please enter a string as you wish: ")

# declaring variables to store the number of vowels and consonants.
vowels = 0 
consonants = 0

# for-loop to iterate for every vowel in the string.
for i in str:

    # nested if-statement to determine if the phrase contains the library of vowels or consonants.
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
       i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
           vowels = vowels + 1
    else:
        consonants = consonants + 1

# code to print out the number of vowels and consonants.
print("The number of vowels in this string are: ", vowels)
print("The number of consonants in this string are: ", consonants)