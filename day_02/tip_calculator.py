#Tip calculator
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?\n"))
tip_percent = float(input("What percentage tip would you like to give?\n"))
people = int(input("How many people to split the bill?\n"))
total = round(((total_bill + (total_bill * tip_percent / 100)) / people), 2)
print(f"Each person should pay: ${total}")
