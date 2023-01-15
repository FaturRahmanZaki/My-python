import turtle

turtle.bgcolor('Black')
turtle.speed(100)
turtle.hideturtle()

colors = {"blue", "salmon", "pink", "red"}

for i in range (120):
    for c in colors:
        turtle.color(c)
        turtle.circle(100-i, 100)
        turtle.lt(90)
        turtle.circle(100-i, 100)
        turtle.end_fill()
        
tutle.mainloop()