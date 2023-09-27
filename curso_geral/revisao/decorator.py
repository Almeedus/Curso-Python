def create_function(func):
    def internal(*args, **kwargs):
        for arg in args:
            is_string(arg)
        return func(*args, **kwargs)
    return internal

@create_function #sinonimo de "inverte_string_checando_parametros = create_function(inverte)"
def inverte(string):
    texto = string
    def invertendo():
        #exemplo de variavel nonlocal, nela eu acesso o valor da variavel escrita no escopo anterior
        nonlocal texto
        return texto[::-1]
    return invertendo()

def is_string(param):
    if not isinstance(param,str):
        raise TypeError('Param deve ser uma string')

invertida = inverte('321')
print(invertida)


