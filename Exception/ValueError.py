try:
    data1 = float(input('Num1: '))
    data2 = float(input('Num2: '))
    print('data is: ', data1, data2)
except ValueError as e:
    print('Exception due to: ', e)