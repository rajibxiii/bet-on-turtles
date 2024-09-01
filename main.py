from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=550, height=400)

bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")
print(bet)

turtles = []

for i in range (5):
    turtle_object = Turtle(shape="turtle")
    turtle_object.color()
    turtles.append(turtle_object)


turt1.goto(x=-250, y=-100)









screen.exitonclick()