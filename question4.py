import numpy as np

# Declaracao dos dados
# Faturamentos
faturamento = {
    "SP": "67836.43",
    "RJ": "36678.66",
    "MG": "29229.88",
    "ES": "27165.48",
    "Outros": "19849.53",
}

# Declaracao de variaveis
somaTotal = 0

# Calculo do total
for i in faturamento.values():
    somaTotal = somaTotal + float(i)

# Exibicao das porcentagens
for i, k in faturamento.items():
    print('%s: %.2f %%' % (i,  (float(k)/somaTotal)*100))
