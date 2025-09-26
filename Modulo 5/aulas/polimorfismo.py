# Polimorfismo permite que classes derivadas tenham métodos e assinaturas iguais
# tenham comportamentos diferentes.
from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem) -> None: #<- Retorno
        self.mensagem = mensagem
    
    @abstractmethod
    def enviar(self) -> bool: # Meu método 'enviar' deve retornar um boleano (True/False)
        ...
        
        
class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool: # Meu método 'enviar' deve retornar um boleano (True/False)
        print(f'E-mail: Enviando... [{self.mensagem}]')
        return True

        
class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool: # Meu método 'enviar' deve retornar um boleano (True/False)
        print(f'SMS: Enviando... [{self.mensagem}]')
        return False

def notificar(notificacao:Notificacao):
    notificacao_enviada = notificacao.enviar()
    
    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação não enviada')

notificacao_email = NotificacaoEmail('Testando email')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('Testando SMS')
notificar(notificacao_sms)

