import numpy as np

random_number = np.random.randint(1,100,5)

print(random_number)

def sum_list(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

print(sum_list(random_number))