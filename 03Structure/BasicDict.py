# Basic Dictionary

print('Basic Dictionary')

data = {'A': '80+', 
        'B': '70+', 
        'C': '60+', 
        'D': '50+'
        }

print('data: ', data)
print('type: ', type(data))
print('len: ', len(data))

print('--------------------')

print('Basic Dictionary: Read')
print('data[\'A\']: ', data['A'])
print('data.get(\'A\'): ', data.get('A'))

print('--------------------')

print('Basic Dictionary: Edit')
print('Before edit A: ', data['A'])
data['A'] = '90+'
print('After edit A: ', data['A'])

print('--------------------')
print('Basic Dictionary: Merge')
print('\n')
print('Merge by |')

language = {'js': 'Javascript',
            'vb': 'Visual Basic',
            'cs': 'C#'
            }

result = data | language
print('Merge data and language by |: ', result)
print('type of new dict: ', type(result))
print('\n')
print('Merge by |=')

data1 = {'A': '80+', 
        'B': '70+', 
        'C': '60+', 
        'D': '50+'
        }
data2 = {'A': 'Ant',
         'B': 'Boy',
         'C': 'Cat'}

print('Before Merge')
print('data1: ', data1)
print('type(data1): ', type(data1))
print('data2: ', data2)
print('type(data2): ', type(data2))
print('\n')
data1 |= data2
print('After Merge')
print('data1: ', data1)
print('type(data1): ', type(data1))
print('data2: ', data2)
print('type(data2): ', type(data2))

print('--------------------')
print('Basic Dictionary: remove by pop()')

data = {'A': '80+', 
        'B': '70+', 
        'C': '60+', 
        'D': '50+'
        }

print('Before pop')
print('data: ', data)
data.pop('C')
print('After pop')
print('data: ', data)

print('--------------------')
print('Basic Dictionary: delete by del')
data = {'A': '80+', 
        'B': '70+', 
        'C': '60+', 
        'D': '50+'
        }

print('Before del')
print('data: ', data)
del data['B']
print('After del')
print('data: ', data)
