#Conversão de medidas

medida = float(input("Digite uma medida em metros para conversão \n"))
op = int(input("Selecione a opção desejada: \n 1 - Decímetros \n 2 - Centímetros \n 3 - Milímetros \n"))

match op:
    case 1:
        tot = medida * 10
        print(f"{medida} metros em Decímetros é: {tot:.2f}")
    case 2:
        tot = medida * 100
        print(f"{medida} metros em Centímetros é: {tot:.2f}")
    case 3:
        tot = medida * 1000
        print(f"{medida} metros em Milímetros é: {tot:.2f}")