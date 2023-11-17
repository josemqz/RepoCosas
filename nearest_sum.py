''''
Cuando tengas listo el desafío, envía el archivo con tu respuestas a humanos@nursoft.cl 
con el asunto "Nursoft Challenge 2021/22 - José Quezada". 
Por favor respeta el formato para hacer el proceso más fácil.

Considera dos listas de enteros, ```list_1``` y ```list_2```, y un número entero, ```value```. 
Debes escribir la función ```get_nearest_sum``` que busque el par de elementos, uno de ```list_1``` 
y otro de ```list_2```, cuya suma sea la más cercana a ```value```.

Algunos ejemplos:

list_1 = [7, 6, 10, -1]
list_2 = [8, 10, 29, 12]
value = 19
>>> get_nearest_sum(list_1, list_2, value)
(7, 12)

list_1 = [24, 29, 9, 4, 21, 13, -2, 9, 10, 20]
list_2 = [14, 16, -3]
value = 23
>>> get_nearest_sum(list_1, list_2, value)
(9, 14)

list_1 = [8, 13, 19, 24, 30]
list_2 = [20, 7, 28, 0]
value = 23
>>> get_nearest_sum(list_1, list_2, value)
(24, 0)
'''

# primera combinación con dif == 0 -> break
# tiene que recorrer ambas listas sí o sí, lo importante es cómo

# ordenar -> O(2n + n logn)
# búsqueda binaria

#busqueda binaria en sort_list
def nearest_sum_helper(l, sort_list, value, izq, der, med):

    actValue = value - l
    medItem = sort_list[med]
    print("med:", med, "mi:", medItem, "actValue:", actValue)

    # par exacto
    if medItem == actValue:
        print("item encontrado:", medItem, "diff:", 0)
        return (medItem, 0)

    # final de búsqueda
    if (der - izq) < 1:
        print("\nfinal búsqueda")

        diff1 = abs(medItem - actValue)

        #comparar con vecino para saber cuál es el más cercano
        if medItem < actValue and med != (len(sort_list) - 1):
            print("actValue es mayor")
            delta = 1   # elemento siguiente

        elif medItem > actValue and med != 0:
            print("actValue es menor")
            delta = -1 # elemento anterior
        
        else:
            return (medItem, diff1)

        diff2 = abs(sort_list[med + delta] - actValue)

        if diff1 < diff2:
            print("item encontrado:", medItem, "diff1:", diff1, "diff2:", diff2)
            return (medItem, diff1)
        else:
            print("item encontrado:", sort_list[med+delta], "diff2:", diff2, "diff1:", diff1)
            return (sort_list[med + delta], diff2)


    # búsqueda en segunda mitad
    elif medItem < actValue:

        # borde superior
        if med == (len(sort_list) - 1):
            print("borde superior")
            izq = der
            
        else:
            print("segunda mitad")
            izq = med + 1
            med = (der + izq) // 2

        return nearest_sum_helper(l, sort_list, value, izq, der, med)

    # búsqueda en primera mitad
    else:

        # borde inferior
        if med == 0:
            print("borde inferior")
            der = izq

        else:
            print("primera mitad")
            der = med - 1   
            med = (der + izq) // 2
        
        return nearest_sum_helper(l, sort_list, value, izq, der, med)


def get_nearest_sum(list_1, list_2, value):

    min_diff = 999999
    item_1 = -1
    item_2 = -1

    # ordenar lista más pequeña
    if len(list_1) < len(list_2):
        
        list_2.sort()

        izq = 0
        der = len(list_2) - 1
        med = round(len(list_2)/2)

        # búsqueda binaria
        for l in list_1:
            print("\nl1 actual:", l)
            act_item, diff = nearest_sum_helper(l, list_2, value, izq, der, med)

            if diff == 0:
                print("\npar exacto!")
                return (l, act_item)

            elif diff < min_diff:
                item_1 = l
                item_2 = act_item
                min_diff = diff
                print("nuevo min diff:", diff, "| elementos:", item_1, item_2)

    else:

        list_1.sort()

        izq = 0
        der = len(list_1) - 1
        med = round(len(list_1)/2)

        # búsqueda binaria
        for l in list_2:
            print("\nl2 actual:", l)
            act_item, diff = nearest_sum_helper(l, list_1, value, izq, der, med)

            if diff == 0:
                print("\npar exacto!")
                return (act_item, l)

            elif diff < min_diff:
                item_2 = l
                item_1 = act_item
                min_diff = diff
                print("nuevo min diff:", diff, "| elementos:", item_1, item_2)

    return (item_1, item_2)


list_1 = [8, 13, 19, 24, 30]
list_2 = [20, 7, 28, 0]
value = 23
print(get_nearest_sum(list_1, list_2, value))


list_1 = [7, 6, 10, -1]
list_2 = [8, 10, 29, 12]
value = 19
print(get_nearest_sum(list_1, list_2, value))

# >>> get_nearest_sum(list_1, list_2, value)
# (7, 12)

# >>> get_nearest_sum(list_1, list_2, value)
# (9, 14)

list_1 = [24, 29, 9, 4, 21, 13, -2, 9, 10, 20]
# [-2, 4, 9, 9, 10, 13, 20, 21, 24, 29] -> 9 -> med = 5
list_2 = [10, 16, -3]
value = 22
print(get_nearest_sum(list_1, list_2, value))

