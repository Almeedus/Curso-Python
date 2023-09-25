#escopo da função - local do código que pode ser atingido, ou seja, o que está dentro da função só afeta o que está
#dentro da função

x = 1

def escopo():
    print(x+1)

#print(x) <- ele está definido apenas dentro da função escopo

escopo()