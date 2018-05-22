from random import choice
x = ["champion","meticulous","hexagon"]
for _ in range(len(x)):
    a = choice(x)
    b = list(a)
    x.remove(a)
    for i in range(len(a)):
        c = choice(b)
        print(c, end = " ")
        b.remove(c)
    print()

    run = True
    while run:
        e = input("Your Answer: ")
        if e == a:
            print("Hura")
            run = False
        else:
            print("Again :(!")
