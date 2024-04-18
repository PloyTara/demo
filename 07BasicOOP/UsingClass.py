from models.human import *
from models.programmer import *

h = Human('Nannaphat S.')
print('fullname: ', h.Name)
h.Speak()

print('--------------------')
p = Programmer('Top')
print('fullname: ', p.Name)
p.Programming()