#Function as Parameter

def Add(x, y):
    return x + y

def Sub(x, y):
    return x - y

def Calculator(func, num1, num2):
    return func(num1, num2)

result1 = Calculator(Add, 100, 200)
print('Result 1: ', result1)
result2 = Calculator(Sub, 100, 200)
print('Result 2: ', result2)