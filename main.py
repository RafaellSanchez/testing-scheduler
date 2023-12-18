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

conteudo = ''  # Inicializa uma string vazia para armazenar o conteúdo do arquivo

# Tente abrir o arquivo e ler seu conteúdo
try:
    with open(full_path, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.split(';')
            print(dados)
            conteudo += linha  # Adiciona a linha ao conteúdo a ser salvo
    print("Leitura do arquivo bem-sucedida!")
except FileNotFoundError:
    print("Arquivo não encontrado:", full_path)
except Exception as e:
    print("Erro:", e)

# Diretório de destino para salvar o arquivo
diretorio_destino = 'dados'  # Substitua pelo nome do seu diretório de destino

# Nome do arquivo a ser criado no diretório de destino
nome_arquivo_destino = 'arquivo_salvo.txt'

# Caminho completo para o arquivo de destino
caminho_arquivo_destino = os.path.join(diretorio_destino, nome_arquivo_destino)

# Tenta salvar o conteúdo lido do arquivo no diretório de destino
try:
    with open(caminho_arquivo_destino, 'w') as arquivo_destino:
        arquivo_destino.write(conteudo)
    print(f"Conteúdo do arquivo salvo em '{caminho_arquivo_destino}'.")
except Exception as e:
    print("Erro ao salvar o arquivo:", e)