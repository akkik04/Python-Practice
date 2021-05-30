# creating a function to calculate the gravitational potential energy. 
def calc_gravitational_energy(mass, GRAVITY, height):

    # arithmetic calculation to determine the gravitational potential energy.
    gravitational_energy = mass * GRAVITY * height
    gravitational_energy = round(gravitational_energy, 2)

    return gravitational_energy

# receiving input regarding the mass and height.
mass = float(input("Enter the mass in kilograms please: "))
GRAVITY = 9.8
height = float(input("Enter the height in meters please: "))

# printing the value of the gravitational potential energy.
print("The value of the gravitational potential energy is: ", calc_gravitational_energy(mass, GRAVITY, height))