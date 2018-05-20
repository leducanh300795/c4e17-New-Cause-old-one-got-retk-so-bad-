def get_even_list(listenter):
    for i in listenter:
        if i % 2 != 0:
            listenter.remove(i)
    return listenter

even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
