def w_1(list_1):
    arr_1 = set(list_1)
    answ = False
    if len(list_1) == len(arr_1):
        answ = True
    return answ


def w_2(list_1):
    list_2 = []
    for i in list_1:
        if (list_1.count(i) > 1):
            list_2.append(i)
    return list_2


def w_3(list_1):
    list_3 = []
    x = list_1[0]
    for i in range(1, len(list_1)):
        if list_1[i] == x:
            list_3 += [list_1[i]]
        x = list_1[i]
    return list_3


list_1 = [1, 2, 2, 2, 54, 56, 3, 3, 18, 22, 'df', 'df', 897, 879, 44, 18, ]
print(list_1)
print(w_1(list_1))
print(w_2(list_1))
print(w_3(list_1))
