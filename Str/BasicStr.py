print('Basic Str')

fullName = 'Nannaphat S.'
data = 'Python'
print('fullName: ', fullName)
print('data: ', data)
print('type(fullName): ', type(fullName))
print('type(data): ', type(data))

print('--------------------')

print('Basic Str: more line')
data = """Python
Chapter 7
Str"""

print(data)

print('--------------------')

print('Basic Str: len() + +=')

firstName = 'Nannaphat'
lastName = 'S.'
txt = 'Python'
salary = 25000

print('len(firstName): ', len(firstName))
print('len(lastName): ', len(lastName))
print('Name: ', firstName + ' ' + lastName)

print('Before txt: ', txt)
txt += ' Programming'
print('After txt: ', txt)

print('salary: ' + str(salary) + ' thb')

print('--------------------')

print('Basic Str: count()')

txt = 'Python Programming'
print('count all P: ', txt.count('P'))
print('count p ตัวที่ 8 ขึ้นไป: ', txt.count('p', 7))
print('count p ตัวที่ 1 - 9: ', txt.count('p', 0, 8))

print('--------------------')

print('Basic Str: format()')

price = 299.255
amount = 1290

print('price: {} amount: {}'.format(price, amount)) # เลขปกติ
print('price: {} amount: {:,}'.format(price, amount)) # ใส่ , แสดงตำแหน่ง
print('price: {:,.2f} amount: {:,}'.format(price, amount)) # ปัดเลขทศนิยมตามกำหนด

print('--------------------')

print('Basic Str: select char or text')

data = 'Python'

print('data[0]: ', data[0])
print('data[1]: ', data[1])
print('data[2]: ', data[2])
print('data[3]: ', data[3])
print('data[4]: ', data[4])
print('data[5]: ', data[5])
print('data[-1]: ', data[-1])
print('data[-2]: ', data[-2])
print('data[-3]: ', data[-3])
print('data[-4]: ', data[-4])
print('data[-5]: ', data[-5])
print('data[-6]: ', data[-6])
print('txt[0:3]: ', txt[0:3])
print('txt[1:]: ', txt[1:])
print('txt[:4]: ', txt[:4])

print('--------------------')

print('Basic Str: find()')

txt = 'Python Programming'

print('find all P: ', txt.find('P'))
print('find all Y: ', txt.find('Y'))
print('find P ตำแหน่งที่ 8 เป็นต้นไป: ', txt.find('P', 7))
print('find P ตำแหน่งที่ 1-6: ', txt.find('P', 0, 5))
print('find specific word: ', txt.find('C++'))

print('--------------------')

print('Basic Str: text allignment')

txt = 'Python'

print(txt.ljust(8, '*'))
print(txt.center(8, '*'))
print(txt.rjust(8, '*'))

print('--------------------')

print('Basic Str: in, not in')

fullName = 'Nannaphat S.'
print('Na' in fullName)
print('Na' not in fullName)

print('--------------------')

print('Basic Str: start end')

data = 'Python Programming 2024'

print(data.startswith('python'))
print(data.endswith('2024'))

print('--------------------')

print('Basic Str: prefix suffix')

txt = 'HelloPython'
result1  = txt.removeprefix('Hello')
print('result1: ', result1)
result2  = txt.removesuffix('Python')
print('result2: ', result2)