# from turtle import Turtle, Screen
# timmy = Turtle()
#
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.fillcolor('yellow')
# # timmy.circle(180)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
#
# for steps in range(100):
#     for c in ('blue', 'red', 'green', 'black', 'purple'):
#         timmy.color(c)
#         timmy.forward(steps)
#         timmy.right(30)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electronic", "Water", "Fire"])

table.align = "l"

print(table)
