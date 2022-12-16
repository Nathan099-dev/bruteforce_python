import sys
import dns.resolver

argumentos = sys.argv #passando e lendo os argumentos
try:
    dominio = argumento[1]
    lista = argumento[2]
except:
    print('Faltam argumentos no comando')
    sys.exit(1)

#abrindo uma lista de palavras chave
try:
    arquivo.open(lista)
    linhas = arquivo.read().splitlines()
except:
    print('Arquivo não encontrado ou inválido')
    sys.exit(1)

for linha in linhas:
    subdominio = linha + 'bancocn.com'
    try:
        resposta = dns.resolver.query(subdominio, 'a')
        for resultado in resposta:
            print(subdominio, resultado)
        except:
            pass