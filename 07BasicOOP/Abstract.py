from abc import abstractmethod

class Member:
    @abstractmethod
    def Discount(self):
        pass

class VIP(Member):
    def Discount(self):
        return 0.10
    
class VVIP(Member):
    def Discount(self):
        return 0.20
    
v1 = VIP()
print('VIP: ', v1.Discount())

v2 = VVIP()
print('VVIP: ', v2.Discount())