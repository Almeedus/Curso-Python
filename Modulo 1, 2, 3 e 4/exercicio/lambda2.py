def executa(funcao, *args):
    return funcao(*args)

#função lambda que soma dois numeros
print(
    executa(
        lambda x, y:  x + y,
        2, 3
    )
)

#funcao lambda que retorna uma funcao
#função lambda que utiliza uma outra função lambda
duplica = executa(
        lambda m : lambda n: n*m, 2
    )

print(duplica(3))



