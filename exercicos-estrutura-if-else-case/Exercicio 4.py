#Ler dois números e apresentar a subtração do maior pelo menor
n1 = float(input("Digite um número: "))
n2 = float(input("Digite mais um número: "))

if n1 > n2:
    tot = n1 - n2
    print(f"{n1} - {n2} = {tot}")
else:
    tot = n2 - n1
    print(f"{n2} - {n1} = {tot}")