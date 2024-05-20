from dataclasses import dataclass

@dataclass
class Customer:
    name: str
    address: str

    def walk(self):
        print(f'{self.name} is walking')

c = Customer('Ploy', 'BKK')
print(c.__dataclass_fields__)