from dataclasses import dataclass

@dataclass
class Human:
    fullname: str
    address: str

h = Human('Nannaphat S.', 'BKK')
print('Name-Surname: ', h.fullname)
print('Address: ', h.address)
print(type(h))