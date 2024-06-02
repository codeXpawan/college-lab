
dict = {'a':10, 'b':200, 'c':300}


def sum_list(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

def sum_key_values(dict):
    sum = 0
    values_list = list(dict.values())
    print(values_list)
    return sum_list(values_list)

print(sum_key_values(dict))