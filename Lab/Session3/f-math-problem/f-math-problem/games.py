from random import randint
from random import choice
import evil
def game(x,op,y,display_result):
    error = randint(-2,2)
    list_operation = ["+","-","*","/"]
    op = choice(list_operation)
    x = randint(1,10)
    y= randint(1,10)
    result = evil.calc(x, y, op)

    display_result = result + error
    # print("*"*20)
    print("{0}{1}{2} = {3}".format(x,op,y,display_result))
# print("*"*20)
# answers = str(input("(Y/N): ")).upper()
# if answers == "Y" and error == 0:
#     print("Yeah, You're right")
# elif answers == "N" and error !=0:
#     print("Yeah, You're right")
# elif answers == "Y" and error !=0:
#     print("Aw, You're wrong, try again")
# elif answers == "N" and error ==0:
#     print("Aw, You're wrong, try again")
# else:
#     print("Wrong Command")
