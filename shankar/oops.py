class TestClass:
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age  # attribute

    # Method
    def print_method(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

test=TestClass('shankar', 20)
test.print_method()
test=TestClass('Kaaviyan', 6)
test.print_method()