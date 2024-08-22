# Ambientes virtuais em python sõa chamadas de VENV
# Um ambiente virtual carrega todas as instalações num diretório escolhido
# Serve para separar os pacotes em diferentes projetos
# E não afeta as dependências globais do python
# Separando eles em 'pastas'

# Exemplo: em um projeto posso trabalhar com pandas e em outro com flask
# instalando em venvs diferentes, nenhum ambiente afeta o outro

# Nomes para venvs comum: venv   env   .venv   .env

# Criar ambiente virtual:
# (o nome do ambiente virtual será .venv)
'python -m venv .venv'

# Ativar o ambiente virtual:
'.venv/Scripts/activate'

# Desativar o ambiente:
'deactivate' 