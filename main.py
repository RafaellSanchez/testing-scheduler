import os

file = '/workspaces/testing-scheduler/data_testing.txt'

# Verificar o diretório atual
print("Diretório atual:", os.getcwd())

# Listar o conteúdo do diretório
print("Conteúdo do diretório:", os.listdir())

# Tente abrir o arquivo
try:
    with open(file, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.split(';')
            print(dados)
    print("Teste sucesso!")
except FileNotFoundError:
    print("Arquivo não encontrado:", file)
except Exception as e:
    print("Erro:", e)