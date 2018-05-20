from turtle import *

shape ("turtle")

colors = ["red", "blue", "brown", "yellow", "grey"]

for i in range (3,8):
    color(colors[i-3])
    for j in range (i):
        forward (100)
        left(180-(i-2)/i*180)


mainloop()
