num1 = int(input("Digite o primeiro número inteiro positivo: "))
num2 = int(input("Digite o segundo número inteiro positivo: "))

op = int(input("Digite a opção desejada: \n 1 - Média ponderada, com pesos 2 e 3 respectivamente. \n 2 - Quadrado da soma dos dois números. \n 3 - Cubo do menor número. \n"))

if op == 1:
    media = (num1 * 2 + num2 * 3) / (2 + 3)
    print(f"A média ponderado entre {num1} e {num2} é {media}")
elif op == 2:
    quadrado = (num1 + num2) ** 2
    print(f"O quadrado da soma entre {num1} e {num2} é {quadrado}")
elif op == 3:
    if num1 > num2:
        cubo = num2 ** 3
        print(f"O cubo do menor número {num2}, é: {cubo}")
    else: 
        cubo = num1 ** 3
        print(f"O cubo do menor número {num1}, é: {cubo}")
else:
    print("Opção inválida, encerrando o programa...")