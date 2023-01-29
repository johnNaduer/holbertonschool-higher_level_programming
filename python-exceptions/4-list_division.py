#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    x = 0
    while x < list_length:
        try:
            if my_list_2[x] == 0:
                print("division by 0")
            if type(my_list_1[x]) != type(my_list_2[x]):
                print("wrong type")
            y = my_list_1[x] / my_list_2[x]
            new_list.append(y)
        except IndexError:
            print("out of range")
            new_list.append(0)
        except:
            new_list.append(0)
        x = x + 1
    return (new_list)
