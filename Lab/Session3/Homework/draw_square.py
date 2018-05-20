from turtle import *
def drawsquare(x,y):
    speed(0)
    color(y)
    a = x*10

    for _ in range (4):
        forward(a)
        left(90)

for i in range(30):
    drawsquare(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()
