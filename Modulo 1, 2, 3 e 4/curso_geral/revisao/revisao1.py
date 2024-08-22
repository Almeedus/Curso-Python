nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")

if not not nome:
    print(f"\nSeu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")

    pesquisa = input("\nPesquise algo no nome: ")
    if pesquisa.upper() in nome.upper():
        print(f"O nome contém {pesquisa.upper()}")
    else:
        print(f"{pesquisa.capitalize()} não existe em {nome}")

    letras = len(nome)
    print(f"\nSeu nome contém {letras} letras")

    primeira = nome[0]
    ultima = nome[-1]
    print(f"\nA primeira letra do seu nome é '{primeira.upper()}'")
    print(f"A ultima letra do seu nome é '{ultima.upper()}'")

    if not idade:
        print("Idade Vazia")
else:
    print("\nNome e Idade estão vazios")

