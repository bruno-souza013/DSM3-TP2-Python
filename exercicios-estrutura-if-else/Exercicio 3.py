sexo = input("Digite 'M' para masculino e 'F' para feminino: ")
altura = float(input("Digite sua altura em metros: "))

if sexo.upper() == 'M':
    pesoideal = (72.7 * altura) - 58
    print(f"Seu peso ideal é de: {pesoideal:.2f} Kg")
elif sexo.upper() == 'F':
    pesoideal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é de: {pesoideal:.2f} Kg")
else: 
    print("Digite uma opçaõ válida.")