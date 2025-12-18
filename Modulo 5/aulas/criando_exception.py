# Para criar uma excessão só herdar da classe exception
class MyError(Exception):
    #raise: Levantando excessão
    # ambos são a mesma coisa
    #throw: Jogando excessão
    ...
    
    
def raise_myError():
    exception_ = MyError('a','b','c')
    raise exception_


try:
    raise_myError()
except MyError as error:
    print(f'Error: {error.args} | Class Error: {error.__class__.__name__}')  