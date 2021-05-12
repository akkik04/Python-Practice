# CALCULATING THE NET FORCE ACTING ON AN OBJECT, GIVEN THE MASS AND ACCELERATION OF THE OBJECT.
# F = MA (Newton's Second Law of Motion).

# defining a function to calculate the net force and passing the values for mass and acceleration as arguments.
def calc_netforce(mass, acceleration):

    # arithmetic calculation to determine the net force.
    net_force = mass * acceleration
    net_force = round(net_force, 2)

    return (net_force)

# receiving input for the values of the mass and acceleration from the user.
mass = float(input("Enter the mass of the object please: "))
acceleration = float(input("Enter the acceleration of the object please:"))

# code to print the final output, which indicates the net force acting on the object
print("The net force of the object is: " + str(calc_netforce(mass, acceleration)),"N")