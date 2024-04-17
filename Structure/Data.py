# Immutable Data

print('Immutable Data')
# ตัวแปรเดิมเปลี่ยนไปชี้ที่ตำแหน่งใหม่ใน memory

name = 'Ploy'
print('Data: ', name)
print('Address: ', id(name)) # Address in memory

name = 'Top'
print('Data: ', name)
print('Address: ', id(name)) # Address in memory

print('--------------------')

# Mutable Data
# เปลี่ยนแปลงค่าในตัวแปรเดิม เก็บที่เดิม

print('Immutable Data')

data = ['Python']
print('Data: ', data)
print('Address: ', id(data)) # Address in memory

data[0] = 'Pyplot'
print('Data: ', data)
print('Address: ', id(data)) # Address in memory
