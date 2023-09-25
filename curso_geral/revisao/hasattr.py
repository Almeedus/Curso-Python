string ='Eduardo'

#print(dir(string)) -> informa todos os atributos(nomes) existentes para utilizar na variavel
print(dir(string))

#print(hasattr(string)) -> checa se tem  algum método

if hasattr(string, 'upper'):
    print('Existe upper')
    print(string)
else:
    print(string.upper())

#print(getattr(string)) -> adiciona o método para a lista de métodos da variavel
metodo = 'upper'
print(getattr(string, metodo)())