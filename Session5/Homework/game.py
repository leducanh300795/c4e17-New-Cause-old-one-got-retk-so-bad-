px=1
py=1
bx=2
by=2
while True:
    for y in range(4):
        for x in range (4):
            if x==px  and y == py:
                print("P", end="")
            elif x==bx and y == by:
                print("G", end="")
            elif x==1 and y == 3:
                print("B", end="")
            else:
                print("-", end = "")
        print()


    command=input("Enter command: (W,S,A,D):").upper()

    next_px = px
    next_py = py
    dx = 0
    dy = 0
    next_bx = bx
    next_by = by

    if command == "W":
        dy= -1
    elif command == "S":
        dy= 1
    elif command == "A":
        dx = -1
    elif command == "D":
        dx = 1
    else:
        print("Wrong Command")
    next_px += dx
    next_py += dy
    if 0<= next_px < 4:
        px = next_px
    if 0<= next_py <4:
        py = next_py
    if 0<= next_bx < 4:
        bx = next_bx
    if 0<= next_by <4:
        by = next_by
    if next_px == bx and next_py == by:
        bx += dx
        by += dy
    if bx == 1 and by == 3:
        print("Win")
        for y in range(4):
            for x in range (4):
                if x==px  and y == py:
                    print("P", end="")
                elif x==bx and y == by:
                    print("G", end="")
                elif x==1 and y == 3:
                    print("B", end="")
                else:
                    print("-", end = "")
            print()
        break
