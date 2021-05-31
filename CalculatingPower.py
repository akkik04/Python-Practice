# creating a function to calculate the power.
def calc_power(net_work, time):

    # arithmetic calculation to determine the power.
    power = (net_work / time)
    power = round(power, 2)

    # returning the value of power.
    return power

# receiving input from the user.
net_work = float(input("Enter the net work in joules please: "))
time = float(input("Enter the time in seconds please: "))

# code to print the final output which indicates the power.
print("The power is", calc_power(net_work, time),"W")