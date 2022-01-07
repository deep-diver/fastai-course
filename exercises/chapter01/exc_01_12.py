from fastcore.all import *

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

@patch
def grow_older(self: _____):
    self.age += 1

@patch(_______=True)
def full_name(self: _____):
    return f'{self.firstname} {self.lastname}'

@patch(__________=True)
def CreatePerson(cls: Person, firstname, lastname, age):
    return Person(firstname, lastname, age)

person = Person.CreatePerson('Chansung', 'Park', 37)
print(f'{person.full_name} 님의 나이는 {person.age}세 입니다.')

print('새해가 밝은 후...')
person.grow_older()
print(f'{person.full_name} 님의 나이는 {person.age}가 되었습니다.')