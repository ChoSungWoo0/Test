class Person:
    def __init__(self):
        name = ''
        age = 0
        gender = ''
    
    def introduce(self):
        print(f'{self.name}, {self.age}, {self.gender}')

class Wizard(Person):
    def dormitory(self):
        dormitory = ''
    
    def introduce(self):
        print(f'{self.name}, {self.age}, {self.gender}')