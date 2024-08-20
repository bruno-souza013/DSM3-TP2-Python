#mostrara estatura de 3 pessoas em ordem decrescente
est1 = float(input("Digite a estatura da primeira pessoa: "))
est2 = float(input("Digite a estatura da segunda pessoa: "))
est3 = float(input("Digite a estatura da terceira pessoa: "))

if est1 > est2 and est1 > est3:
    maior = est1
    if est2 > est3:
        meio = est2
        menor = est3
    else: 
        meio = est3
        menor = est2
elif est2 > est1 and est2 > est3:
    maior = est2
    if est1 > est3:
        meio = est1
        menor = est3
    else: 
        meio = est3
        menor = est1
else:
    maior = est3
    if est1 > est2:
        meio = est1
        menor = est2
    else:
        meio = est2
        menor = est1

print(f"A ordem decrescente das estaturas é: \n {maior:.2f} \n {meio:.2f} \n {menor:.2f}")  
    
