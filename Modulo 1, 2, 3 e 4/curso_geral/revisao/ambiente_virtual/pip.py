"""
Em caso de os comandos não rodarem apenas acrescente
'python -m pip ...'
"""
# O pip é o gerenciador de pacotes do python, muito importante para instalar e desinstalar pacotes

'pip install pacote' 
# ou para baixar uma versão específica
'pip install pacote==1.0.1' 

'pip unistall pacote'
# ou para desinstalar sem perguntar se realmente deseja
'pip install pacote -y'

# Para verificar quais pacotes estão instalados 
'pip freeze'

# ==================================================================================================
# Criando um requirements.txt para instalar dependências em outro ambiente virtual

'pip freeze > requirements.txt'

# Isso irá gerar um arquivo requirements com a entensão .txt
# que salvará todos os pacotes e versões dentro desse arquivo

# ==================================================================================================
# Gerando um ambiente virtual com o requirements criado

'python -m venv .venv'

# Depois de ativar o novo ambiente virtual só realizar a instalação das dependências
'pip install -r requirements.txt'

# Caso realize a instalação ou atualização das dependências é necessário realizar a inserção das
# dependências no arquivo novamente.

'pip freeze > requirements.txt'