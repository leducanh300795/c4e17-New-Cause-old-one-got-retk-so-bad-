# A Boolean value is either true or false
# 5 == 6 -Produce Fasle
# 6 != 7 -Produce True
# 8 > 9 - Produce Fasle
# flowchart show the exact steps and logic of how the statement executes

print("Ví dụ 1:")
n = float(input("Nhập vào số đầu tiên: "))
m = float(input("Nhập vào số thứ hai: "))
if n==m:
    print("Hai số nhập vào bằng nhau")
elif n > m:
    print("Số thứ nhất lớn hơn")
else:
    print("Số thứ nhất nhỏ hơn")
