print('basic while loop')

x = 1
while(x <= 5):
    print('x: ', x)
    x = x + 1
print('end loop')
print('--------------------')

print('cumulative while loop')
i = 1
total = 0
while i <= 10:
    print('i: ', i)
    total += i
    i += 1
print('Total: ', total)
print('--------------------')

print('while loop with range()')
i = 1
total = 0 
while i in range(1, 4):
    print('i: ', i)
    total += i
    i += 1
print('Total: ', total)