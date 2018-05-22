from turtle import *

shape ("turtle")

colors = ["red", "blue", "brown", "yellow", "grey"]

for i in range (5):
    begin_fill()
    color(colors[i])
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)

    end_fill()

mainloop ()
