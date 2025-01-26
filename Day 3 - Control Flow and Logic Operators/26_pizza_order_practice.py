print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L:")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra chese? Y or N: ")

#todo: work out how much they need to pay based on their size choice.

bill = 0

if size == "S" or size == "s":
    bill += 15
elif size == "M" or size == "m":
    bill += 20
elif size == "L" or size == "l":
    bill += 25
else:
    print("You typed the wrong input.")

#todo: Work out how much to add to their bill based on their pepperoni choice.

if pepperoni == "Y" or pepperoni == "y":
    if size == "S" or pepperoni == "s":
        bill += 2
    else:
        bill += 3
    
#todo: work out their final amount based on whether if they want extra chese.

if extra_cheese == "Y" or extra_cheese == "y":
    bill += 1

print(f"Your final bill is: ${bill}.")
