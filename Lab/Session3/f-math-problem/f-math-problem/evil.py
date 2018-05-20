from random import randint, choice
# define
def calc(x, y, op):
    result = 0

    # x = randint(0,20)
    # y = randint(1,20)
    # op = choice(list_operation)
    if op == '+':
        result = x + y
    elif op == '-':
        result = x - y
    elif op == '*':
        result = x * y
    elif op == '/':
        result = x / y

    return result
print(__name__)
if __name__ == "__main__":
    print('eval.py imported')


# print(result)

#usage/call
# calc(3,7,"-")
# result = calc(1,2, '+')
#
# print(result)
