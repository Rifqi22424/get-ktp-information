my_list = [1, 2, 3, 3, 4, 4, 5, 6, 6]

def uniqueList(list_int:list):
    list_int = set(list_int)
    list_int = list(list_int)
    print(list_int)
    return len(list_int)

print(uniqueList(my_list))

