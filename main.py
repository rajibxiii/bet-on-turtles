from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=550, height=400)

bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")
print(bet)

turtles = []
colors = ["red", "green", "blue", "pink", "orange"]

y_cor = -100
for i in range (5):
    turtle_object = Turtle(shape="turtle")
    turtle_object.color(colors[i])
    turtle_object.penup()
    turtle_object.goto(x=-250, y=y_cor)
    turtles.append(turtle_object)
    y_cor += 50

screen.exitonclick()