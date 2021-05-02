# declaring variables to store the value for the number of votes and letters.
num_votes = int(input())
letters = input()

# declaring variables to store the value for the number of 'A votes' or 'B votes'.
count_of_a = 0
count_of_b = 0

# creating a for-loop that iterates for the number of letters entered.
for i in range (0, len(letters)):

    # determining the number of 'A votes' or 'B votes'.
    if letters[i: i +1] == 'A'.upper():
        count_of_a += 1

    elif letters[i: i + 1] == 'B'.upper():
        count_of_b += 1

# if-statement to determine if the vote for A is greater than B or a tie.
if count_of_a > count_of_b:

    print("A")

elif count_of_b > count_of_a:

    print("B")

else:

    print("Tie")






        



