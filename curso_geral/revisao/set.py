s1 = set('Luiz') # vazio
s1 = {1 ,1 ,2, 3, 3, 3} # com dados


#bons para retirar valores duplicados
print(s1, type(s1)) # irá retornar apenas 1,2,3

l1 = [1,2,3,4,5,1,2,3,4,1,2,3,4]
l2 = set(l1)
print(l2)

verificacao = 3 in s1
print('Está' if verificacao == True else 'Não está')


# Operações

s1.add(4) #envia apenas um valor

#s1.update('Olá Mundo') #letra por letra, posso enviar mais de um valor pelo update
s1.update(('Eduardo',))
print(s1)

s1.discard(('Eduardo')) #elimina o valor que foi passado 
print(s1)


# uniao
s1 = {1 ,1 ,2, 3, 3, 3, 4}
s2 = {3,4,5,6,7}
s3 = s1 | s2 
print('união: ', s3)

#intersecção
s3 = s1 & s2
print('intersecção: ', s3)

#diferença (itens presentes apenas no da esquerda)
s3 = s1 - s2
print('diferença no da esquerda: ', s3)

s3 = s2 - s1
print('diferença no da esquerda: ', s3)

#diferença simetrica (itens presentes em ambas listas)
s3 = s1 ^ s2
print('diferença simetrica: ', s3)


#exemplo de uso
letras = set()
while True:
    letra = input('Digite letra: ')

    if letra.__len__() == 1:
        letras.add(letra)
        print(letras)

    else:
        continue
    
