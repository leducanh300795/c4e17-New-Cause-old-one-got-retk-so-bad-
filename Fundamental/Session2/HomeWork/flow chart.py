import webbrowser

name = input("Nhập vào tên một người bạn: ")
if name == "Quan":
    print("Hand some")
elif name == "Tung":
    print("Even more handsome")
    even_more_handsome = True
    print(bool(even_more_handsome))
elif name == "Don":
    print("Hi Don")
else:
    print("Bảng biểu diễn của em đây ạ")
    webbrowser.open("https://realtimeboard.com/app/board/o9J_kz3Y0Iw=/")
