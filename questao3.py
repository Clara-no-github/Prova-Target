import json

# lendo o arquivo
with open('C:\\Users\\Clara\\Downloads\\dados.json', 'r') as f:
    dados = json.load(f)

# inicializando as variaveis
menor_valor = None
maior_valor = None

# variaveis de media e valores maiores que a media
soma = 0
n = 0
contagem = 0

# achando todas as chaves e valores no arquivo json
for item in dados:
    for chave, valor in item.items():
        # achando o menor e maior valor
        if valor != 0 and valor>31:
            if menor_valor is None or valor < menor_valor:
                menor_valor = valor
            if maior_valor is None or valor > maior_valor:
                maior_valor = valor

        # calcula a média dos valores não nulos
        if valor != 0 and valor>31:
            soma += valor
            n += 1

    # calcula a média para cada item
    if n > 0:
        media = soma / n
    else:
        media = 0

    # conta o número de vezes que cada valor é maior que a média
    for chave, valor in item.items():
        if valor > media and valor>31:
            contagem = contagem + 1

            
# printando os resultados
print('Menor valor:', menor_valor)
print('Maior valor:', maior_valor)
print('Número de valores maiores que a média:', contagem)