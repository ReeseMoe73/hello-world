# User input cost of food.
food_charge = float(input('Enter the amount of the food: $'))

# Include tip and tax.
tip = food_charge * 0.18
sales_tax = food_charge * 0.07

# Print the amounts.
print('Charge for the food' % food_charge)
print('The tip amount' % tip)
print('Tax amount' % sales_tax)
print('Total amount' % (food_charge + tip + sales_tax))
