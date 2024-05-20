from dataclasses import dataclass

@dataclass
class Customer:
    name: str
    address: str

    def walk(self):
        print(f'{self.name} is walking')

c = Customer('Ploy', 'BKK')
c.walk()