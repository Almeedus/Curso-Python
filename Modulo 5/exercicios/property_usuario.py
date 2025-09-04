# Uma classe Usuário que contenha
# ID, NOME, TIPO, EMAIL, SENHA 
# Fazer em ingles para praticar 
import random


class User:
    def __init__(self, name, mail, password):
        self._name = name
        self._mail = mail
        self._password = password
        self._id = random.randint(1,999)
        self._type = None

    @property
    def user(self):
        user = [self._id, self._name, self._mail, self._password, self._type]
        return user

    @user.setter
    def user(self, id):
        try:
            if id == self._id:
                self._type = 'Admin'
            else:
                raise IndexError
        except IndexError:
            return f'ID fornecido não corresponde ao usuário'

    def user_type(self):
        return self._type

user1 = User("Eduardo", "almeedusa@gmail.com", 123123)
print(user1.user)

id_change = int(input('Informe o ID: '))
user1.user = id_change

print(user1.user_type())