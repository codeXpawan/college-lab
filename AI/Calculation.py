import math
x = float(input('Input the first number: '))
y = float(input('Input the Second number: '))



def calculation(x,y):
    add = x+y
    subtract = x-y
    multiply = x*y
    try:
        divide = x/y
    except ZeroDivisionError:
        print('Denominator is Zero.')
        divide = math.inf
    
    return (add,subtract,multiply,divide)
    
    
print(calculation(x,y))