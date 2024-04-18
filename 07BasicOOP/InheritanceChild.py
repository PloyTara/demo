class Human:
    # Parent class
    def __init__(self, id, name):
        self.ID = id
        self.Name = name

class Manager(Human):
    def __init__(self, id, name, salary):
        Human.__init__(self, id, name)
        self.Salary = salary

h = Human('001', 'Ploy')
print('ID: ', h.ID)
print('name: ', h.Name)
print('--------------------')
m = Manager('555', 'Top', 20000)
print('ID: ', m.ID)
print('name: ', m.Name)
print('salary: ', m.Salary)