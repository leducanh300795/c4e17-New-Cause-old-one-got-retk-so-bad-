nums = [3, 4, -99, 78, 4, -99]
x = int(input("Enter a integer: " ))
#must not use count() or in or index()

for num in nums:
    if num == x:
        print("Found!!!")
        break
# Neu vong for tren ma chay vao break thi dong else duoi ko dc chay, con neu ko chay vong break nao thi se chay else
else:
    print("Not found!!")
