#Calculo de grandezas elétricas

print(f"*" * 50)
print("Cáluclo de Grandezas Elétricas")
print(f"*" * 50)

op = int(input(" 1. Tensão (em Volt) ----- U = R * I \n 2. Resistencia (em Ohm) ----- R = U / I \n 3. Corrente (em Ámpere) ----- I = U / R \n Digite a opção desejada: \n"))

match op:
    case 1: 
        r = float(input("Digite o valor da Resistência 'R': "))
        i = float(input("Digite o valor da Corrente 'I' : "))
        u = r * i
        print(f"A tensão é de {u:.2f} Volts.")
    case 2: 
        u = float(input("Digite o valor da Tensão 'U': "))
        i = float(input("Digite o valor da Corrente 'I' : "))
        r = u / i
        print(f"A resistência é de {r:.2f} Ohms.")
    case 3: 
        u = float(input("Digite o valor da Tensão 'U': "))
        r = float(input("Digite o valor da Resistência 'R' : "))
        i = u / r
        print(f"A corrente é de {i:.2f} Ampéres.")
    case _:
        print("Digite uma opção válida!")
        exit