def multiplicacao(*args):
    mult = 1
    for numero in args:
        mult *= numero

    return mult

print(multiplicacao(1,2,3,4,5))
print()
print(1*2*3*4*5)