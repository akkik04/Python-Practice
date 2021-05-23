# HEART RATE PROGRAM TO DETERMINE IF BPM IS NORMAL FROM AGES 6 AND ABOVE.
# INFORMATION IS VALIDATED THROUGH CLEVELANDCLINIC.ORG.

# function to determine the age and bpm.
def calc_heart_rate(age, bpm):

    # if-statement to determine whether the bpm is normal or not normal.
    if (6 <= age <= 17) and (70 <= bpm <= 100) or (age >= 18) and (60 <= bpm <= 100):
        return 'Normal.'

    else:
        return 'Off the normal range.'

# code to recieve input regarding the age and bmp of the user.
age = int(input("Enter your age in years please: "))
bpm = int(input("Enter your BPM please: "))

# printing the final output which indicates if the BPM is normal or not.
print(calc_heart_rate(age, bpm))