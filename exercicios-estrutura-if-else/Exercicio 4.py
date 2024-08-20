#Verificar se o numero é par ou impar para calcular seu quadrado ou cubo
num = int(input("Digite um número inteiro positivo: "))

if num %2 == 0:
    quad = num ** 2
    print(f"O número {num} é par, seu quadrado é: {quad}")
elif num %2 != 0:
    cubo = num ** 3
    print(f"O número {num} é ímpar, seu cubo é: {cubo}")