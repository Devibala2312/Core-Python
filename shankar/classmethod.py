class Person:
    x=0
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        cls.x += 1
        current_year = 2025
        age = current_year - birth_year
        return cls(name, age)

# Usage
p = Person.from_birth_year("shankar", 1987)
print(p.name, p.age)
p1=Person("Kaaviyan",6)
print(p1.name, p1.age)
print(p1.x)
