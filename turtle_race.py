from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)

user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Type in a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y_pos = -65
for turtle_index in range(0,6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-240, y_pos)
    all_turtles.append(new_turtle)
    y_pos +=30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The winning color is: {winning_color}")
            else:
                print(f"You've lost! The winning color is: {winning_color}")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()

