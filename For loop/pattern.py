# This is a python project that outputs strings in a pattern using a if-else statement and for loop
# When i is less than 5 it will ouput strings of asterisks in ascending order.
# When it is more, it does the opposite by eliminating the last character every iteration.

pattern = ""
for i in range(10):
    if i < 5:
       pattern = pattern + "*"
       print(pattern)
    else:
        pattern = pattern[:-1]
        print(pattern)
