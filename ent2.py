#[1,3,7] -> [1,3], [3,7], [1,3,7], [1], [3], [7]

list = [1,3,5,7,9]
i = len(list) #sub grupos

sum_total = 0

while i > 0:
    
    sum_act = 0
    k = 0

    while i + k <= len(list):

        sum_act += sum(list[k: i+k])
        print("lista_act", list[k: i+k])
        k += 1

    sum_total += sum_act

    print(sum_act, "\n")

    i -= 1

print(sum_total)