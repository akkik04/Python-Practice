# creating a variable to store the phrase entered by the user.
phrase = input()

# creating a boolean to store the value of the word following the algorithm.
fail = False

# creating a for-loop that iterates for the length of the phrase.
for i in range(len(phrase)):

    # if-statement to determine if the phrase contains the certain letters that fit the algorithm.
     if phrase[i] == 'I' or phrase[i] == 'O' or phrase[i] == 'S' or phrase[i] == 'H' or phrase [i] == 'Z' or phrase[i] == 'X' or phrase[i] == 'N':
         fail = False

    # code to print the final output if the phrase does not follow the 180 degree rule for each letter, boolean of 'fail' is set to true.
     else:
        fail = True
        print("NO")

# code to print the final output if the phrase follows the 180 degree rule for each letter.
if fail == False:
    print("YES")

    
        




