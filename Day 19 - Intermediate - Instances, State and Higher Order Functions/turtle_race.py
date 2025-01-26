from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
# print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[turtle_index])
    color = colors[turtle_index]
    new_turtle.color(color)
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You'hv own! The {winning_color} turtle is the winner!")
            else:
                print(f"You'hv lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()