#0
dictionary={
    "ns": "Noi: phát âm trong một ngôn ngữ bằng thanh quản",
    "r": "Ra: đi về vị trí ở ngoài",
    "pt": "Party: tổ đội để chơi game",
    "h": "Gio: Đơn vị thời gian"
}
list=["ns", "r", "pt", "h"]
print(*list, sep =",")
#0.1
code= str(input("Enter a code: "))
if code in list:
    print(dictionary[code])
else:
    while True:
        d =input(("{0}{1}, would you like to make a new word(Y/N): ".format(code," is not in this dictionary"))).upper()
        if d == "N" :
            print("Thanks")
        elif d == "Y" :
            e= str(input("{0} '{1}': ".format("Enter the meaing of your word: ",code)))
            dictionary[code] = e
            for key, value in dictionary.items():
                print(key, ":", value)
            break
        else:
            print("Wrong command")
