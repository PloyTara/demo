class Human:
    def __init__(self, id, name):
        self.ID = id
        self.Name = name

    def Speak(self):
        print('Human speak')

h = Human('001', 'Nannaphat S.')
print('id: ', h.ID)
print('fullName: ', h.Name)