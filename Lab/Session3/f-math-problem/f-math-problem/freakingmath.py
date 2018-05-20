from random import *
from evil import calc

def generate_quiz():

    x = randint(1,10)
    y= randint(1,10)
    op=choice(["+","-","*","/"])
    # Hint: Return [x, y, op, result]
    result=calc(x,y,op)
    error=choice([-1,0,0,0,1])
    display_result= result + error

    return [x, y, op, display_result]

def check_answer(x, y, op, result, user_choice):
    # user_choice: True, False
    if calc(x,y,op) == result:
        if user_choice == True:
            return True
        elif user_choice == False:
            return False
    if calc(x,y,op)!= result:
        if user_choice == True:
            return False
        if user_choice == False:
            return True
