#Divisão do maio número pelo menor
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    total = num1 / num2
    print(f"A divisão de {num1} por {num2}, é {total:.2f}")
else:
    total = num2 / num1
    print(f"A divisão de {num2} por {num1}, é {total:.2f}")
