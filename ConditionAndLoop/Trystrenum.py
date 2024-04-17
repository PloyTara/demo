print('Try StrEnum')
from enum import StrEnum, auto

class Language(StrEnum):
    VB = auto() #return 'VB" via auto class
    HTML = auto() #return 'HTML" via auto class
    CS = auto() #return 'CS" via auto class
    Python = auto() #return 'Python" via auto class

print(Language.CS)
print(type(Language.CS))
print('--------------------')

print('Loop StrEnum')

for l in (Language):
    print('value: ', l.value)
print('--------------------')

print('Condition StrEnum')
data = {}
data[Language.Python.value] = 'easy'

if data == {Language.Python: 'easy'}:
    print('Pythin is easy.')
else:
    print('Python is hard')