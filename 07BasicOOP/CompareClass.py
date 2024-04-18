class Person:
    def __init__(self, fullname, age):
        self.FullName = fullname
        self.Age = age

    def __ge__(self, other):
        #function เปรียบเทียบ >=
        return True if self.Age >= other.Age else False
    
    def __gt__(self, other):
        #function เปรียบเทียบ >
        return True if self.Age > other.Age else False
    
    def __le__(self, other):
        #function เปรียบเทียบ <=
        return True if self.Age <= other.Age else False
    
    def __lt__(self, other):
        #function เปรียบเทียบ <
        return True if self.Age < other.Age else False
    
    def __eq__(self, other):
        #function เปรียบเทียบ ==
        return True if self.Age == other.Age else False
    
    def __ne__(self, other):
        #function เปรียบเทียบ !=
        return True if self.Age != other.Age else False
    
p1 = Person('Ploy', 30)
p2 = Person('Top', 30)
print(p1 != p2)