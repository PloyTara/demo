class Parent:
    def PublicMethod(self):
        print('Public')

    def _ProtectMethod(self):
        print('Protect')

    def __PrivateMethod(self):
        print('Private')

class Child(Parent):
    def CallParentPrivate(self):
        self.__PrivateMethod()

c = Child()
c.PublicMethod()
c._ProtectMethod()
c._Parent__PrivateMethod()