# importing the math module to gain access to the functions.
import math

# creating a function to calculate the kinetic energy.
def calc_kinetic_energy(mass, velocity):

    # arithmetic formula to calculate the kinetic energy.
    kinetic_energy = (mass * math.pow(velocity, 2)) / 2
    kinetic_energy = round(kinetic_energy, 2)

    # returning the value of the kinetic energy.
    return kinetic_energy

# receiving input regarding the mass and velocity.
mass = int(input("Enter the mass in kilograms please: "))
velocity = int(input("Enter the velocity in m/s please: "))

# printing the output which indicates the kinetic energy.
print("The kinetic energy is:", calc_kinetic_energy(mass, velocity),"J")