class Human:
    def Speak(self):
        print('Human speak')

class Manager:
    def Speak(self):
        print('Manager speak')

h = Human()
h.Speak()
print('--------------------')
m = Manager()
m.Speak()