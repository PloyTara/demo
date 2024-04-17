print('number enum')
from enum import Enum

class Season(Enum):
    Hot = 1
    Cold = 2

print('Enum Member: ', Season.Hot)
print('Enum name', Season.Hot.name)
print('Enum value: ', Season.Hot.value)
print('Enum type: ', type(Season.Hot))
print('Enum with value: ', Season(2).name)
print('--------------------')