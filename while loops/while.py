# This is a program that continuously asks the user to input a number until they type -1 using a while loop.
# Numbers inputted will be added to the list and once the while loop is exited. The sum of the elements is divided by the number of elements to give the average.
# I used the variable ask as the condition for my while loop.
ask = True
list = []
while ask == True:
  number = int(input("Enter a number. "))
  if number == -1:
    ask = False
  else:
    list.append(number)
print(sum(list)/len(list))
  