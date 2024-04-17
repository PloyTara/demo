class Human:
    def __init__(self, fullName, address):
        self.FullName = fullName
        self.Address = address

h = Human('Nannaphat S.', 'BKK')
print('fullname: ', h.FullName)
print('address: ', h.Address)
print('type(h): ', type(h))