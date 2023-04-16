import json
import numpy as np

# Declaracao de variaveis
dias = []
valores = []
valoresUteis = []
numDias = 0

# Importacao dos dados
with open('Questoes/dados.json') as f:
    dados = json.load(f)

# Recebendo os dados em vetores
for i in dados:
    dias.append(i['dia'])
    valores.append(i['valor'])
    if i['valor'] != 0:
        valoresUteis.append(i['valor'])

# Maiores e menores valores
print(f'Menor faturamento:{np.min(valores)}')
print(f'Maior faturamento:{np.max(valores)}')

# Contagem dos dias com faturamento maior que a media
for i in dados:
    if i['valor'] > np.mean(valoresUteis):
        numDias += 1

print(f'Dias com faturamento maior que a media: {numDias}')
