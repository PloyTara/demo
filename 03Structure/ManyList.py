# Many List

print('read many list by zip()')

book = ['VB', 'VB#', 'Python']
price = [300, 199, 345]

for b, p in zip(book, price):
    print(f'{b} {p}')

print('--------------------')

print('List comparison')
data1 = [1, 2, 3]
data2 = [100, 200, 300]

print('data1: ', data1)
print('data2: ', data2)
print('data1 > data2: ', data1 > data2)
print('\n')

data3 = ['a', 'b', 'c']
data4 = ['A', 'B', 'C']
print('data3: ', data3)
print('data4: ', data4)
print('data3 == data4: ', data3 == data4)

print('--------------------')

print('read list by map()')

data5 =['aa', 'bb', 'cc', 'dd']
result = map(str, data5)
print('list(result): ', list(result))
