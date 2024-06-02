import numpy as np

random_number_list = np.random.randint(0,1000,100)

print(random_number_list)

def largest_number(list):
    largest_number = 0
    for number in list:
        if number > largest_number:
            largest_number = number
    return largest_number

print(largest_number(random_number_list))