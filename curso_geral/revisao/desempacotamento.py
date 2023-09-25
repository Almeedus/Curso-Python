lista = ['Eduardo', 'Maria', 'Clara']
_, nome1, *_ = lista

#boa pratica *_ o underline informa que a variavel criada foi ignorada


print(nome1, *_)
