print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 15 or 20 "))
people = int(input("How many people to split the bill? "))
# bill_with_tip = tip / 100 * bill + bill
# bill_with_tip = bill * tip / 100 + 
bill_with_tip = bill * (1 + tip / 100)
print(round(bill_with_tip, 2))

bill_per_person = bill_with_tip / people

# print(round(bill_per_person, 2))
print(f"Each person should pay: ${round(bill_per_person, 2)}")