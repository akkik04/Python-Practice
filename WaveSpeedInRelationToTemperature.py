# creating a function to calculate the speed of the wave given the temperature.
def calcWaveSpeed(temperature):

    # arithmetic calculation to determine the speed of the wave.
    speed = 331.4 + (0.606 * temperature)
    speed = round(speed, 2)

    # returning the value for the speed of the wave.
    return speed

# receiving input regarding the temperature.
temperature = float(input("Enter the temperature outside in celsius please: "))

# printing the final output, which indicates the speed of the wave.
result = calcWaveSpeed(temperature)
print("The speed of the wave at " + str(temperature) + "°C" + " is " + str(result) + " m/s.")