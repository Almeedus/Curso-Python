# DIFERENÇA ENTRE: @staticmethod e @classmethod

# @classmethod - tem acesso ao cls e o método da classe
# @staticmethod - não tem acesso nem ao cls nem ao self, é um método comum


class Connection:
    def __init__ (self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
    
    
    def set_user(self, user):
        self.user = user
        
    def set_password(self, password):
        self.password = password
        
    @classmethod
    def create_user_auth(cls, user, password):
        connection = cls()
        connection.set_user(user)
        connection.set_password(password)
        return connection
    
    @staticmethod
    def get_host():
        return 'localhost'
        
        
c1 = Connection.create_user_auth('Luiz','12345678')
print(c1.user)  # Luiz
print(c1.password)  # 12345678

print(c1.get_host())  # localhost