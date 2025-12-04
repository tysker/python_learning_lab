print("Wlecome to the tip calculator!")
total_bill = float(input("What was the total bill? $ "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
total_tip_amout = (tip / 100) * total_bill
amount = round((total_bill + total_tip_amout) / people, 2)
print(f"Each person should pay ${amount}")
