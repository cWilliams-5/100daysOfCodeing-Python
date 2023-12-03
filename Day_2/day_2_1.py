# Tip Calculator
# 100 Days Of Python Day 2

print("Welcome to the tip calculator.")
subTotal = float(input("what was the total bill? $"))
split = int(input("How many people to split the bill? "))
percent = int(input("What percentage tip would you like to give? "))
total = (subTotal * (1+(percent/100)))/split
tip = (subTotal * (percent/100))
print("The total tip will be: " + str(round(tip, 2)))
print("Each person should pay (including tip): " + str(round(total, 2)))
print("Each person should pay (no tip): " + str(round((subTotal/split), 2)))