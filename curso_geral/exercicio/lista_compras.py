import os, time
compras = []

try:
    while True:
        print('[1] Listar Itens')
        print('[2] Adicionar Item')
        print('[3] Remover Item')

        acao = input('O que deseja fazer: ')

        if acao.isdigit() is True:
            acao = int(acao)
        else:
            print('Digite um número presente nas opções')
            time.sleep(2)
            os.system('cls')
            continue
        
        if acao == 1:
            lista_compras = enumerate(compras)
            print('Sua lista de compras:')
            
            for produto in lista_compras:
                print(produto)
            
            
        elif acao == 2:
            item = input('Informe um produto para adicionar a lista: ').capitalize()
            compras.append(item)    
            print(f'{item} adicionado com sucesso')
            

        elif acao == 3:
            item = input('Informe um produto para excluir da lista: ').capitalize()
            if item in compras:
                compras.remove(item)               
                print(f'{item} removido')
                
            else:
                print('Produto não encontrado')
                continue
        
        else:
            
            print('Informe uma opção válida')
            continue
        time.sleep(3)
        os.system('cls')
except:
    print('Caraca, que foi que você fez parceiro!')
