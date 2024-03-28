# This is a program showing a logical error. The while loop will keep iterating regardless of the input.
game = True
while game:
   number = input("pick a number between 1 and 10")
   if number != 6:
    print("No")
   else:
     print("You won")
     game = False
# To correct this would require using the int() method on the input to convert the answer to an int.