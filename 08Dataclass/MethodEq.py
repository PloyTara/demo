from dataclasses import dataclass

@dataclass
class Human:
    fullname: str
    address: str

    def __eq__(self, other):
        return (self.address == other.address)
    
h1 = Human('Nannaphat S.', 'BKK')
h2 = Human('Somchai', 'BKK')
print('Is h1 equal h2? => ', h1 == h2)