from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=550, height=400)
screen.title("Turtle Race Bet")
bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")
print(bet)

turtles = []
colors = ["red", "green", "blue", "pink", "orange", "teal"]

y_cor = -100
for i in range (6):
    turtle_object = Turtle(shape="turtle")
    turtle_object.color(colors[i])
    turtle_object.penup()
    turtle_object.goto(x=-250, y=y_cor)
    turtles.append(turtle_object)
    y_cor += 40

if bet: # if there is a user bet
    game_is_on = True

while game_is_on:
    for j in turtles:
        if j.xcor() > 230: # when the turtle wins/hits the x coordinate
            game_is_on = False
            winning_color = j.pencolor()
            if bet == winning_color:
                print (f"You won. The {winning_color} turtle is the winner.")
            else:
                print (f"You lost. The {winning_color} turtle is the winner.")

        distance_to_cover = randint (0, 5)
        j.forward(distance_to_cover)


screen.exitonclick()