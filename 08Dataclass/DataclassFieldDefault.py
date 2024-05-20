from dataclasses import dataclass, field

@dataclass
class Customer:
    name: str
    address: str = field(default='BKK')

    def walk(self):
        print(f'{self.name} is walking')

c = Customer('Ploy')
print(c.address)