import math

# getting input of the a, b, and c values from the user.
a = int(input("Enter the 'a' value of the quadratic equation please: "))
b = int(input("Enter the 'b' value of the quadratic equation please: "))
c = int(input("Enter the 'c' value of the quadratic equation please: "))

print()

# discriminant to determine the roots of the quadratic.
discriminant = (b ** 2) - (4 * a * c)
root1 = (-b + math.sqrt(discriminant)) / (2 * a)
root2 = (-b - math.sqrt(discriminant)) / (2 *a)
print("The roots of this quadratic equation are: " + str(root1) + " and " + str(root2))

print()

# printing the vertex of the quadratic equation using the appropriate algorithm.
print ("The vertex of this quadratic equation is at point: (" , (-b / (2 * a)) , ", " ,(((4 * a * c) - (b * b)) / (4 * a)) , ")" )         