print('Testando código de agendamento!')


file = '/workspaces/testing-scheduler/data_testing.txt'

with open(file, 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        dados = linha.split(';')  # Divide a linha usando o ponto e vírgula como separador
        print(dados)  # Isso imprimirá uma lista com os dados separados

print("Teste sucesso!")