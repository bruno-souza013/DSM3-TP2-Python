#algoritmo para ler o nome do cliente, valor do depósito. Depois dizer se o saldo está positivo ou negativo.

nome = input("Digite o nome: ")
op = int(input(f"Olá {nome}, o que gostaria de fazer hoje? \n 1- Sacar \n 2- Depositar \n"))

if op == 1:
    saldo_atual = 800
    saque = float(input("Digite o valor para saque: R$"))
    saldo_atual = 800 - saque
    if saldo_atual == 0:
        print(f"Nome: {nome}")
        print(f"Saldo atual: R${saldo_atual:.2f}")
        print("Saldo Limite!")
    elif saldo_atual > 0:
        print(f"Nome: {nome}")
        print(f"Saldo atual: R${saldo_atual:.2f}")
        print("Saldo Positivo!")
    else:
        print(f"Nome: {nome}")
        print(f"Saldo atual: R${saldo_atual:.2f}")
        print("Saldo negativo!")
elif op == 2:
    saldo_atual = 800
    dep = float(input("Digite o valor para depósito: R$"))
    saldo_atual = 800 + dep
    if saldo_atual == 0:
        print(f"Nome: {nome}")
        print(f"Saldo atual: R${saldo_atual:.2f}")
        print("Saldo Limite!")
    elif saldo_atual > 0:
        print(f"Nome: {nome}")
        print(f"Saldo atual: R${saldo_atual:.2f}")
        print("Saldo Positivo!")
    else:
        print(f"Nome: {nome}")
        print(f"Saldo atual: R${saldo_atual:.2f}")
        print("Saldo negativo!")
