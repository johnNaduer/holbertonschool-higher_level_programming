#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    x = 0
    suma = 0
    suma2 = 0
    while x < len(my_list):
        numero = 1
        y = 0
        while y < len(my_list[x]):
            numero1 = my_list[x][y]
            numero = my_list[x][y] * numero
            y = y + 1
            if y < len(my_list[x]):
                suma2 = my_list[x][y] + suma2
        suma = numero + suma
        x = x + 1
    if suma2 != 0:
        return suma/suma2
