# Albert Hong
# Intro to Programming - Block 4
# Meal Calculator

# Main Function
def main():
	# Establish values of constants
	NJ_TAX_RATE = 0.0625
	MEAL_COST = 45
	TIP_PERCENTAGE = 0.2
	
	# Define variables 
	tipAmount = TIP_PERCENTAGE * MEAL_COST
	taxAmount = NJ_TAX_RATE * MEAL_COST
	totalBill = taxAmount + tipAmount + MEAL_COST

	# Print values for meal cost, tax, tip, and total for the meal
	print("Meal Cost: " + "$" + str(MEAL_COST))
	print("Tax Amoubnt: " + "$" + str(taxAmount))
	print("Tip Amount: " + "$" + str(tipAmount))
	print("Total Bill: " + "$" + str(totalBill))

# Calling main
main()
