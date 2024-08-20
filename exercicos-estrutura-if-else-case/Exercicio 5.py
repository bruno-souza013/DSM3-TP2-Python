#Ler nome e idade de duas pessoas e nostrar os dados da pessoa mais alta:

nome = input("Digite o nome da primeira pessoa: ")
idade = int(input(f"Digite a idade do(a) {nome}: "))
altura = float(input("Digite a altura: "))

nome2 = input("Digite o nome da segunda pessoa: ")
idade2 = int(input(f"Digite a idade do(a) {nome2}: "))
altura2 = float(input("Digite a altura: "))

if altura > altura2:
    print(f" Nome: {nome} \n Idade: {idade} \n Altura: {altura} \n {nome} é mais alto(a)")
else:
    print(f" Nome: {nome2} \n Idade: {idade2} \n Altura: {altura2} \n {nome2} é mais alto(a)")