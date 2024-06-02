import math

prime_numbers = []

start_number = int(input('Enter the starting number : '))
end_number = int(input('Enter the ending number : '))


def calculate_prime(start_number,end_number):
    if(start_number > end_number):
        print('start_number is greater than end number.')
        return []
    else:
        for i in range(start_number,end_number+1):
            root = int(math.sqrt(i))
            flag = False
            if(i == 1):
                continue
            for j in range(2,root+1):
                if(i%j == 0):
                    flag = True
                    break
                
            if flag == False:
                prime_numbers.append(i)
    
    return prime_numbers


print(calculate_prime(start_number,end_number))