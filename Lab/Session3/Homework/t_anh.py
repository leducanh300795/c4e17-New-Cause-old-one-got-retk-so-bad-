from draw_square import drawsquare
for i in range(30):
    drawsquare(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
