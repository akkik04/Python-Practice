# CALCULATING THE WORK ON AN OBJECT, GIVEN THE FORCE AND DISPLACEMENT OF THE OBJECT.

# creating a function to calculate the work.
def calc_work (force, displacement):

    # arithmetic calculation to determine the work on an object.
    work = force * displacement
    work = round(work, 2)

    # returning the value of work to print as output.
    return work

# code to receive input regarding the values for force and displacement.
force = int(input("Enter the amount of force in Newtons please:"))
displacement = int(input("Enter the amount of displacement in meters please:"))

# code to print the final output which indicates the work on the object in joules.
print("The work on the object is:", calc_work(force, displacement),"J")