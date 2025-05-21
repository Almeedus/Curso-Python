# @staticmethod (métodos estáticos)

# Esse tipo de método não tem acesso ao SELF e nem ao CLS 
# Ele não pode acessar atributos de instância ou de classe

class Exemplo:
    @staticmethod
    def metodo_estatico():
        print('Método estático chamado!')
        
        
classe = Exemplo()
classe.metodo_estatico()  # Chamando o método estático através da instância
Exemplo.metodo_estatico()  # Chamando o método estático através da classe
