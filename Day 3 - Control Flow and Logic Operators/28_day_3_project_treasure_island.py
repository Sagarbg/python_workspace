print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You're at the crossroad, where do you want to go? Type 'Left' or 'Right'. \n").lower()

if choice1 == "left":
    # Continue the game
    choice2 = input("You'hv come to a lake,"
          "there is an island in the middle of the lake."
           "Type 'wait' to wait for boat. Type 'swim' to swim across \n").lower()
    if choice2 == "wait":
        # Continue the game
        choice3 = input("Your arrive at the island unharmed."
                        "There is a house with three doors."
                         "One red, one yellow and one blue. Which color do you choose \n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game over.")
        elif choice3 == "yellow":
            print("You find the treasure. You win!")
        elif choice3 == "blue":
            print("Enter a room of beasts. Game over.")
        else:
            print("You choose a door that doesn't exist. Game over.")
    else:
        print("You got attacked by an angry trout. Game over.")
else:
    print("You fell in to a hole. Game over.")
