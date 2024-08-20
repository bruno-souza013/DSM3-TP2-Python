#11 - Leia a descrição do produto e exiba seu valor total
nome = input("Digite o nome do produto: ")
qtd = int(input("Digite a quantidade comprada: "))
val = float(input("Digite o valor do produto: "))
total = qtd * val
print(f"O valor total do produto {nome} é R${total:.2f}")
print()