# CALCULATING THE FORCE OF GRAVITY GIVEN THE MASS.

# defining a function and passing an argument named 'mass'
def force_of_gravity (mass):

    # arithmetic calculation to determine the force of gravity.

    gravity_force = mass * 9.8
    gravity_force = round(gravity_force, 2)
    

    return (gravity_force)

# prompting the user to enter the mass of the object.
mass = int(input("Enter the mass of the object in kilograms please: "))

# printing the final output indicating the force of gravity.
print(force_of_gravity(mass), "N")