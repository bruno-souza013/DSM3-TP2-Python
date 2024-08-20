#6- Algoritmo para calcular reajuste de salario
sal = float(input("Digite o seu salário: "))
perc = float(input("Digite o percentual de reajuste: "))
novosal = sal + (sal * perc/100)
print(f"O sálario com o reajuste de {perc}% é R${novosal:.2f}")
print()