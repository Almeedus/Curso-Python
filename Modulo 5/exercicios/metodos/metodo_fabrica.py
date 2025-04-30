# fazer uma lógica para criar um objeto pessoa 
# usando o @classmethod para extender a criação da classe
# levar em consideração o ano atual e a idade da pessoa para criar um filtro de 
# idade <= 10 criança // idade <= 13 jovem //
# idade <= 18 adolescente // idade <= 50 adulto // idade > 50 idoso
import datetime

class Person: 
    CURRENT_YEAR = datetime.datetime.now().year
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.category = None
        
    @classmethod
    def create_child(cls, name, age):
        if age <= 10:
            person = cls(name, age)
            person.category = 'Child'
            return person
        else:
            raise ValueError("Age must be 10 or less for a child.")
        
    @classmethod
    def crate_teen(cls, name, age):
        if 10 < age <= 13:
            person = cls(name, age)
            person.category = "Teen"
            return person
        else:
            raise ValueError("Age must be between 10 and 13 for a teen.")
        
    @classmethod 
    def create_adolescent(cls, name, age):
        if 13 < age <= 18:
            person = cls(name, age)
            person.category = "Adolescent"
            return person
        else:
            raise ValueError("Age must be between 13 and 18 for an adolescent.")
        
    @classmethod
    def create_adult(cls, name, age):
        if 18 < age <= 50:
            person = cls(name, age)
            person.category = "Adult"
            return person
        else:
            raise ValueError("Age must be between 18 and 50 for an adult.")
        
    @classmethod
    def create_senior(cls, name, age):
        if age > 50:
            person = cls(name, age)
            person.category = "Senior"
            return person
        else:
            raise ValueError("Age must be greater than 50 for a senior.")
        

p1 = Person.create_child("Lucas", 10)
p2 = Person.crate_teen("Ana", 12)
p3 = Person.create_adolescent("Carlos", 15)
p4 = Person.create_adult("Maria", 30)
p5 = Person.create_senior("João", 60)

print(f'{p1.name} is a {p1.category} and is {p1.age} years old.')
print(f'{p2.name} is a {p2.category} and is {p2.age} years old.')
print(f'{p3.name} is a {p3.category} and is {p3.age} years old.')
print(f'{p4.name} is a {p4.category} and is {p4.age} years old.')
print(f'{p5.name} is a {p5.category} and is {p5.age} years old.')
        
    