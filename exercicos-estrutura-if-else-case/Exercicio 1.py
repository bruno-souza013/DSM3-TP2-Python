#Ler a daata de nascimento de uma pessoa, se ela tiver mais de 16 anos exibir a mensagem que ela pode votar. Utilizando IF

ano_nasc = int(input("Digite o ano em que nasceu: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - ano_nasc

if idade >= 16:
    print("Poderá votar!")
else:
    print(f"Você tem {idade} anos, ainda não poderá votar.")