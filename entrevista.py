# posiciones par (no informáticos) 1, 3
# corre iterativamente hasta que quede un elemento.
list = ["a","b", "c", "d", "e"]

while len(list) > 1:


    list_aux = []
    for i, _ in enumerate(list):
        if i % 2 != 0:
            list_aux.append(list[i])

    print(list_aux)
    list = list_aux

print("final:", list)