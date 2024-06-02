x = int(input('Enter the number :'))


def factorial(x):
    factorial = 1
    while x > 1:
        factorial = factorial * x
        x -= 1
    return factorial

print(factorial(x))