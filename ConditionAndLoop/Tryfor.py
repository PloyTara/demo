print('basic for')
for i in range(10):
    print(i)
print('--------------------')

print('for with list')
data = [100, 200, 300, 400, 500]

print(type(data))

for d in data:
    print(d)
print('--------------------')

print('for with enumerate')
data = [5, 10, 15, 30, 40, 50]

for index, d in enumerate(data):
    print(index, d)
print('--------------------')

print('for with break')
data = [100, 200, 300, 400, 500]

for d in data:
    if d == 300:
        print('found 300')
        break
    print(d)
print('--------------------')

print('for with continue')
data = [100, 200, 300, 400, 500]

for d in data:
    if d == 300:
        print('found 300')
        continue
    print(d)
print('--------------------')

print('for with else')
data = [100, 200, 300, 400, 500]

for d in data:
    print(d)
else:
    print('end loop')
print('--------------------')

print('for with _')
for _ in range(3):
    print('Python')