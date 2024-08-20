#Cálculo do peso em relação a gravidade de outros planetas.

peso = float(input("Digite seu peso em Kg: "))
op = int(input("Escolha um planeta para saber quanto pesaria se estivesse nele: \n 1 - Mercúrio (gravidade relativa: 0,37) \n 2 - Vênus (gravidade relativa: 0,88) \n 3 - Marte (gravidade relativa: 0,38) \n 4 - Júpiter (gravidade relativa: 2,64) \n 5 - Saturno (gravidade relativa: 1,15) \n "))

match op:
    case 1:
        tot = peso * 0.37
        print(f"Seu peso em Mercúrio: {tot:.2f} Kg")
    case 2:
        tot = peso * 0.88
        print(f"Seu peso em Vênus: {tot:.2f} Kg")
    case 3:
        tot = peso * 0.38
        print(f"Seu peso em Marte: {tot:.2f} Kg")
    case 4:
        tot = peso * 2.64
        print(f"Seu peso em Júpiter: {tot:.2f} Kg")
    case 5:
        tot = peso * 1.15
        print(f"Seu peso em Saturno: {tot:.2f} Kg")
    case _:
        print("Escolha um planeta!")