# This is a program that takes a string and outputs a string where every alternate letter is capitalized and another where every other word in a string is uppercase.
def alternative(words):
 t_String = ""
 b = True
#message = input(str("Please type in a string. "))
 # A for loop and and an if statement to iterate through the given word(s) and constantly alternate between upper and lower case.
 for i in words:
      if b:
        t_String += i.upper()
      else:
        t_String += i.lower()
# When the loop reaches a position that doesn't contain an empty space, the b variable is switched to allow the next character to be the opposite case.
      if i !=  ' ':
        b = not b
 # Another for and if statement is used but with a list that contains the split of the given String so each word can have its own position.
 list = words.split()
 for char in range(0, len(list)):
# If the index of the list is an even number, then the program will switch to uppercase and vice versa
  if char % 2 == 0:
   list[char] = list[char].upper()
# The whole list is then converted to a single string.
 every_Word = " ".join(list) 
 print(every_Word)
 print(t_String) 
 return t_String, every_Word
 
print(alternative("Hello world I'm here"))





