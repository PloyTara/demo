x = 100
y = 0

try:
    result = x / y
except ZeroDivisionError:
    print('cannot divide because denominator is 0')
finally:
    result = 0

print(result)