# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.
# The print statement needs to have its argument in brackets. (Syntax error)
print("Welcome to the error program")
# The lines of code are indented. This a syntax error
print("\n")

    # Variables declaring the user's age, casting the str to an int, and printing the result
    # Declaring a variable only needs one = sign. (Syntax error)
    #age_str cannot be converted because it contains characters that are not numbers. (Logical error)
    # Strings cannot be concatenated with int values. It needs to output a f-string. (runtime error)
age_Str = "24" 
age = int(age_Str) 
print(f"I'm {age} years old.")

    # Variables declaring additional years and printing the total years of age
    # The years_from_now variable should contain an int rather than string to perform caluclations with it. (runtime error).
    # To reach 330, years_from_now should be equal to 3.5 (logical error)
years_from_now = 3.5
total_years = age + years_from_now
    # Print statement needs to be in brackets and it's accurate for total_years to be in this statement. (logical error)
    # Print statement should contain a f-string. (runtime error)
print(f"The total number of years: {total_years}")

# Variable to calculate the total amount of months from the total amount of years and printing the result
# The total variable has not been defined. (runtime error)
# Print statement needs to be in brackets. (syntax error)
# Cannot concatenate strings with int values. Print statement needs to contain a f-string. (runtime error)
total = total_years
total_months = total * 12
print(f"In 3 years and 6 months, I'll be {total_months} months old")

#HINT, 330 months is the correct answer