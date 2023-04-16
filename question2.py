# Declaracao de variaveis
n1, n2 = 0, 1
count = 0

print("Busca na Seguencia de Fibonacci!")

# validacao de dados de entrada
while True:
    n = int(input("Digite o numero de referência: "))
    if n >= 0:
        break

# calculo da sequencia de fibonacci
while n1 <= n:

    np = n1 + n2
    n1 = n2
    n2 = np

    # comparacao de valores
    if n1 == n or n == 0:
        print(f'O valor {n} pertence a sequência de Fibonacci!')
        break
    elif n1 > n:
        print(f'O valor {n} não pertence a sequência de Fibonacci!')
