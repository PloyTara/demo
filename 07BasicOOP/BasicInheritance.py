class Human:
    # Parent class
    def __init__(self, id, name):
        self.ID = id
        self.Name = name

class Manager(Human):
    # Child class
    # empty class inheeritance from class Human
    pass

h = Human('001', 'Ploy')
print('ID: ', h.ID)
print('name: ', h.Name)
print('--------------------')
m = Manager('555', 'Top')
print('ID: ', m.ID)
print('name: ', m.Name)