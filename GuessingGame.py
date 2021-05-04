# AKSHITH KANDIVANAM
### GUESSING GAME ###

# importing random module.
import random

# receiving a number between 1 and 20 from the user as input.
user_num = int(input("Enter a number between 1 and 20 please: "))

# generating a random number that the computer picks from 1 to 20.
# printing the computer's number and the user entered number to the screen.
random_num = random.randint(1, 21)
print("Computer's Number: " + str(random_num))
print("Your Number: " + str(user_num)) 

# if-statement to determine if the number's match to indicate if the game is won or lost.
if user_num == random_num:
    print("You Won!")
else:
    print("Better luck next time.")












