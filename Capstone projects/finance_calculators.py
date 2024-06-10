import math
# This is a capstone python project using variables and control structures.
# It begins with presenting the user to choose either investment or bond from the menu.
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
choice = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()
# If the user chooses investment they will be prompted with 4 questions.
# Used the round function to make outputs more readable.
# The answers provided will be used to calculate either simple or compund interest based on their respective formulas.
if choice == 'investment':
    deposit_amount = int(input("How much money are you depositing? "))
    interest_rate = float(input("What is the interest rate? Do not enter percentage sign. "))
    years = int(input("How many years do you plan on investing? "))
    interest = input("Do you want simple or compound interest? ").lower()
    interest_rate = interest_rate/100
    if interest == "simple":
        Total_amount = round(deposit_amount * (1 + interest_rate*years))
        print((f"Total amount after interest: {Total_amount}"))
    elif interest == "compound":
        Total_amount = round(deposit_amount * math.pow((1+interest_rate),years))
        print(f"Total amount after interest: {Total_amount}")
# If the user chooses bond then they will be presented with 3 questions.
# The answers provided will be used to calculate the repayment per month based on the bond repayment formula
elif choice == "bond":
   deposit_amount = int(input("What is the present value of the house? "))
   monthly_interest_rate =  float(input("What is the interest rate? Do not enter percentage sign. "))
   months =  int(input("Please enter the number of months you plan to take to repay the bond "))
   
   monthly_interest_rate = monthly_interest_rate/100/12
   repayment = round((monthly_interest_rate * deposit_amount)/(1 - (1 + monthly_interest_rate) **(-months)))
   print(f"you will have to pay £{repayment} per month")
else:
   print("Error. Please enter an option from the menu.")
        

    
