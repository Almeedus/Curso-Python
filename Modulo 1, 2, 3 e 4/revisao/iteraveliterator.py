#Generator expression, iterables e iterators
iterable = ['Eu', 'tenho', '__iter__']
iterator = iter(iterable) #tem __iter__ e __next__

#iteravel = responsavel de ter os valores sequencialmente
#iterator = entregar uma valor por vez, entrega apenas o proximo valor

#print(next(iterator))
#print(next(iterator))
#print(next(iterator))

#se não for possível dar next ele da um excessão
#print(next(iterator))


#generator = funções que sabem pausar

def generator(n=0,maximum=10):
    while True:
        yield n

        if n >= maximum:
            return
        
        n += 1


gen = generator(maximum=10)

for n in gen:
    print(n)
print()



def gen1():
    yield 1
    yield 2
    yield 3


def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6

g = gen2()

for numero in g:
    print(numero)