# creating a function to calculate the velocity of the wave.
def calc_velocity(wavelength, frequency):

    # arithmetic calculation to determine the velocity of the wave.
    velocity_of_wave = wavelength * frequency
    velocity_of_wave = round(velocity_of_wave, 2)

    # returning the value of the velocity for the wave.
    return velocity_of_wave

# receiving input regarding the wavelength and frequency.
wavelength = float(input("Enter the wavelength in meteres please:"))
frequency = float(input("Enter the frequency in hertz please:"))

# storing the value returned.
result = calc_velocity(wavelength, frequency)

# printing the final output, which indicates the velocity of the wave.
print()
print("The velocity of the wave is: " + str(result) + " m/s")