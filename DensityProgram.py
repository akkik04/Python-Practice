# creating a function to calculate the density.
def calc_density(mass, volume):

    # arithmetic calculation to determine the density.
    density = mass / volume
    density = round(density, 2)

    # returning the value of the density.
    return density

# receiving input from the user regarding the mass and volume of the substance.
mass = float(input("Enter the mass of the substance in grams please: "))
volume = float(input("Enter the volume of the substance please: "))

# printing the final output which indicates the density.
print("The density of the object is:", calc_density(mass, volume), "g/cm^3")