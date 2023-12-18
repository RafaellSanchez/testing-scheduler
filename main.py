import os

# Caminho relativo para o arquivo data_testing.txt
file = 'data_testing.txt'

# Verificar o diretório atual
print("Diretório atual:", os.getcwd())

# Listar o conteúdo do diretório
print("Conteúdo do diretório:", os.listdir())

# Caminho completo para o arquivo baseado no diretório atual
full_path = os.path.abspath(file)
print("Caminho completo do arquivo:", full_path)

# Tente abrir o arquivo
try:
    with open(full_path, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.split(';')
            print(dados)
    print("Teste sucesso!")
except FileNotFoundError:
    print("Arquivo não encontrado:", full_path)
except Exception as e:
    print("Erro:", e)
