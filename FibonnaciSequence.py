# AKSHITH KANDIVANAM

# defining a function with parameter 'n'.
def fibonnaci_recursion(x):

   if x <= 1:
       return x

   else:
       return(fibonnaci_recursion(x-1) + fibonnaci_recursion(x-2))

nterms = int(input("Enter your desired amount of terms in the Fibonnaci Sequence please: "))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")

else:
   print("Fibonacci sequence:")

   # for-loop to iterate for the desired number of terms.
   for i in range(nterms):
       print(fibonnaci_recursion((i)))
      