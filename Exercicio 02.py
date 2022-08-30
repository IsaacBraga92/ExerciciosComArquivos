# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
# Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários,
# e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu
# gerar o seguinte arquivo, chamado "usuarios.txt":

lista_de_dados = []


def transformar_em_mb(tamanho_bytes) -> float:
    return int(tamanho_bytes) / (2 ** 10) ** 2


with open('usuarios.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        usuario = linha[:15]
        tamanho_em_disco = transformar_em_mb(linha[16:])
        lista_de_dados.append((usuario, tamanho_em_disco))

cabecalho = '''ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
'''
with open('relatorio.txt', 'w') as arquivo:
    tamanho_total_utilizado = sum([tamanho for _, tamanho in lista_de_dados])
    media = tamanho_total_utilizado / len(lista_de_dados)
    arquivo.writelines(cabecalho)
    for indice, dados in enumerate(lista_de_dados, start=1):
        usuario, tamanho_em_disco = dados
        arquivo.writelines(f'{indice:<4} {usuario}{tamanho_em_disco:9.2f} MB         {tamanho_em_disco/tamanho_total_utilizado:>6.2%}\n')

    arquivo.writelines('\n')
    arquivo.writelines(f'Espaço total ocupado: {tamanho_total_utilizado:.2f} MB\n'),
    arquivo.writelines(f'Espaço médio ocupado: {media:.2f} MB')
