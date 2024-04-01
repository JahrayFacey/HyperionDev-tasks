# This is a program modelling a cafe shop. I created a menu with the available products.
menu = ["Jerk", "Pork", "Curry", "Patty"]
# I also created two dictionaries that contains the stock and price of the items.
stock = {"Jerk":5,
        "Pork":10,
         "Curry":15,
          "Patty":20 }
price = {"Jerk":4.75,
         "Pork":4.75,
         "Curry":5.50,
         "Patty":1.50}
total_stock = 0
jerk_Value = stock["Jerk"] * price["Jerk"]
pork_Value = stock["Pork"] * price["Pork"]
curry_Value = stock["Curry"] * price["Curry"]
patty_value = stock["Patty"] * price["Patty"]
print(jerk_Value,pork_Value,curry_Value,patty_value)
total_value = jerk_Value + pork_Value + curry_Value + patty_value
# The total value of all of the menu's items multiplied by the stock held.
print(total_value)
# Here we loop through menu to access the keys and gain the values of the stock dictionary.
for i in menu:
    total_stock += stock[i]
# The values are added until the menu list is iterated and the total stock is calculated.
print(total_stock)