# AKSHITH KANDIVANAM

# importing the necessary module.
from datetime import date

# creating a function to find the difference in days.
def calc_difference_of_days(year1, month1, day1, year2, month2, day2):

    # computing the format for the two dates using the module's function.
    first_date = date(year1, month1, day1)
    second_date = date(year2, month2, day2)

    # code to compute the difference in days between both dates.
    diff_days = second_date - first_date

    # returning the value for the difference in days.
    return diff_days

# receiving input for the first date.
year1 = int(input())
month1 = int(input())
day1 = int(input())

# receiving input for the second date.
year2 = int(input())
month2 = int(input())
day2 = int(input())

# code to print the final output, which indicates the difference in days between both dates.
result = calc_difference_of_days(year1, month1, day1, year2, month2, day2)
print(result)