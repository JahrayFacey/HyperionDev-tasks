# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.
# Lion is a string and should be in quotation marks (syntax error)
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16
# The variables in the string are placed in the wrong order (logical error)
# Since it contains variables the string needs to be an f-string(syntax error)
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"
# The print statement should be in brackets. (syntax error)
print(full_spec)

