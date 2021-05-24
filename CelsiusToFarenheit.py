# creating a function to calculate the degrees farenheit.
def calc_farenheit(celsius_num):

    # arithmetic calculation to determine the degrees farenheit.
    farenheit = (celsius_num * 1.8) + 32
    farenheit = round(farenheit, 2)

    # returning the value of farenheit.
    return farenheit

# code to recieve input regarding the degrees celsius to convert into farenheit.
celsius_num = float(input("Enter the value in degrees Celsius:"))

# printing the final output which indicates the degrees farenheit.
print(celsius_num, " degree Celsius is equal to ", str(calc_farenheit(celsius_num)), " degree Farenheit.")