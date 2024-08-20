nome1 = input("Digite o nome da primeira pessoa: ")
peso1 = float(input(f"Digite o peso do {nome1}: "))
nome2 = input("Digite o nome da segunda pessoa: ")
peso2 = float(input(f"Digite o peso do {nome2}: "))

if peso1 > peso2:
    print(f"{nome1} é mais pesado(a) que {nome2}")
elif peso1 == peso2:
    print("Ambos possuem o mesmo peso!")
else:
    print(f"{nome2} é mais pesado(a) que {nome1} ")