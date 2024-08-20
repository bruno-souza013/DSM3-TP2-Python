#Algoritmo para calcular rejuste salaria de funcionário

cat = (input("Digite a categoria do funcionário para calcular o reajuste salarial . \n 'A' - 10% \n 'B' - 15% \n 'C' - 25% \n"))

match (cat.upper()):
    case 'A':
        sal = float(input("Digite o salário atual da categoria: R$"))
        tot = sal + ((sal * 10)/100)
        print(f"Novo salário com reajuste de 10%: R${tot:.2f}")
    case 'B':
        sal = float(input("Digite o salário atual da categoria: R$"))
        tot = sal + ((sal * 15)/100)
        print(f"Novo salário com reajuste de 15%: R${tot:.2f}")
    case 'C':
        sal = float(input("Digite o salário atual da categoria: R$"))
        tot = sal + ((sal * 25)/100)
        print(f"Novo salário com reajuste de 25%: R${tot:.2f}")
    case _:
        print("Digite uma categoria válida!")
                      
