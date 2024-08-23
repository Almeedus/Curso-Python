nome = 'a'
nome_repetido = nome

print(id(nome))
print(id(nome_repetido))

if id(nome) == id(nome_repetido): print('\nIgual')
else: print('\nDiferente')