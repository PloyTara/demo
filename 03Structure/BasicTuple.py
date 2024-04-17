# Basic Tuple

print('Basic Tuple')

data = ('Javascript', 'Java', 'HTML')

print('data: ', data)
print('type: ', type(data))
print('len: ', len(data))

print('--------------------')

print('Basic Tuple: Change List to Tuple')

data = [100, 200, 300, 400]
print('data: ', data)
print('data type: ', type(data))
print('data len: ', len(data))
t = tuple(data)
print('t: ', t)
print('t type: ', type(t))
print('t len: ', len(t))

print('--------------------')

print('Basic Tuple: Create tuple data: number')

t = tuple(range(1, 20, 2))
print('tuple t: ', t)
print('t type: ', type(t))

print('--------------------')

print('Basic Tuple: Find max min')

data = (5, 10, 15, 20)
print('max: ', max(data))
print('min: ', min(data))

print('--------------------')

print('Basic Tuple: Find index')

data1 = ('Javascript', 'Java', 'HTML')
print('Find index Java: ', data1.index('Java'))

print('--------------------')

print('Basic Tuple: in, not in')
print('Java in data1: ', 'Java' in data1)
print('Java not in data1: ', 'Java' not in data1)

print('--------------------')

print('Basic Tuple: Read Data in Tuple')

print('Order start by 0')
print('data1[0]: ', data1[0])
print('data1[1]: ', data1[1])
print('data1[2]: ', data1[2])
print('\n')
print('Order start by -1')
print('data1[-1]: ', data1[-1])
print('data1[-2]: ', data1[-2])
print('data1[-3]: ', data1[-3])

print('--------------------')

print('Basic Tuple: Select range')

data2 = ('Javascript', 'Java', 'HTML', 'C++', 'C#')
print('[start:stop]: ', data2[1:4])
print('[start:]: ', data2[2:])
print('[:stop]: ', data2[:2])

print('--------------------')

print('Basic Tuple: Sorting')
print('sort: ', sorted(data2))
print('sort (reverse): ', sorted(data2, reverse = True))

print('--------------------')
