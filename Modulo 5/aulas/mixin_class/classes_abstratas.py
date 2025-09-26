from abc import ABC, abstractmethod

# para ser considerada uma classe abstrata, ela DEVE herdar de ABC
class Log(ABC):
    # também DEVE ter PELO MENOS UM método com um decorator @abstractmethod
    @abstractmethod
    def _log(self, msg): ...
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg}: ({self.__class__.__name__})')
        

# dessa forma, não é possível instanciar ela
# l = Log()

l = LogPrintMixin()
l.log_error('Oi')