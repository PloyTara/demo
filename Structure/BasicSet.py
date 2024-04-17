# Basic Set

print('Basic Set')
data = {'C++', 'C#', 'Java', 'JavaScript'}
print('data: ', data)
print('type(data): ', type(data))
print('len(data): ', len(data))

print('--------------------')

print('Basic Set: Add data')
print('Basic Set: Add data by add()')
data.add('HTML')
print('data: ', data)
print('type(data): ', type(data))
print('len(data): ', len(data))
print('\n')
print('Basic Set: Add data by update()')
data.update('HTML')
print('data: ', data)
print('type(data): ', type(data))
print('len(data): ', len(data))

print('--------------------')

print('Basic Set: Remove data')
print('Basic Set: Remove data by remove()')
data.remove('H')
data.remove('T')
print('data: ', data)
print('type(data): ', type(data))
print('len(data): ', len(data))
print('\n')
print('Basic Set: Remove data by discard()')
data.remove('M')
data.remove('L')
print('data: ', data)
print('type(data): ', type(data))
print('len(data): ', len(data))

print('--------------------')

print('Basic Set: Intersection')
data1 = {'C++', 'C#', 'Java', 'JavaScript'}
data2 = {'MEAN stack', 'Express', 'JavaScript', 'TypeScript'}
print('data1: ', data1)
print('data2: ', data2)
print('data intersection: ', data1 & data2)
print('data intersection: ', data1.intersection(data2))

print('--------------------')

print('Basic Set: Union')
data1 = {'C++', 'C#', 'Java', 'JavaScript'}
data2 = {'MEAN stack', 'Express', 'JavaScript', 'TypeScript'}
print('data1: ', data1)
print('data2: ', data2)
print('data union: ', data1 | data2)
print('data union: ', data1.union(data2))

print('--------------------')

print('Basic Set: Difference')
data1 = {'C++', 'C#', 'Java', 'JavaScript'}
data2 = {'MEAN stack', 'Express', 'JavaScript', 'TypeScript'}
print('data1: ', data1)
print('data2: ', data2)
print('data differnece: ', data1 - data2)
print('data differnece: ', data1.difference(data2))

print('--------------------')
