from dataclasses import dataclass

@dataclass
class Human:
    data: str

    def __str__(self):
        return f"Human said: {self.data}"
    
h = Human('Hello @dataclass')
txt = h.__str__()
print(txt)