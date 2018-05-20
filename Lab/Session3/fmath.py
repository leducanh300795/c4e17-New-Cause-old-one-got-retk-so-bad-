from evil import calc
x = int(input("x= "))
op = input('Operation(+,-,*,/): ')
y = int(input("y = "))
result = calc(x, y, op)
# result = 0
# if op == '+':
#     result = x + y
# elif op == '-':
#     result = x - y
# elif op == '*':
#     result = x * y
# elif op == '/':
#     result = x / y
print('*' * 20)
# print(x,op,y,"=",result)
print("{0} {1} {2} = {3}".format(x, op, y, result))
print('*' * 20)
