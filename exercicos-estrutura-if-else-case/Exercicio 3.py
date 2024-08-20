n1 = float(input("Digite um número real: "))
n2 = float(input("Digite mais um número real: "))

op = input("Escolha uma das seguintes operações: \n + - adição \n - - subtração \n * - multiplicação \n / - divisão \n")

match op: 
    case "+":
        tot = n1 + n2
        print(f"{n1} + {n2} = {tot}")
    case "-":
        tot = n1 - n2
        print(f"{n1} - {n2} = {tot}")
    case "*":
        tot = n1 * n2
        print(f"{n1} * {n2} = {tot}")
    case "/":
        if n2 == 0:
            print("Não é possível dividir por 0!")
        else:
            tot = n1 / n2
            print(f"{n1} / {n2} = {tot:.2f}")