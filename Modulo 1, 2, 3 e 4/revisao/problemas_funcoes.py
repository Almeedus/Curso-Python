#Problemas dos parametros mutáveis em funções Python

# Criando a função desta forma, caso não seja passado o parametro da 'lista'
# ela cria uma nova lista, caso esteja sendo passado, ela apenas adiciona
def adding_customer(name=str, customer_list=None):
    if customer_list == None:
        customer_list = []
    customer_list.append(name)
    return customer_list
   
   
# Iniciando a lista que vai receber o retorno da função a nivel global 
customer_list1 = adding_customer('Eduardo')
adding_customer('Felipe', customer_list1)

# Agora só adicionar os nomes passando como lista a iniciada anteriormente
customer_list2 = adding_customer('Maria')
adding_customer('Marcia', customer_list2)


print(customer_list1)
print(customer_list2)
