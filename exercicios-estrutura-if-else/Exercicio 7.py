#Algoritmo para ver se uma pessoa requer aposentadoria
rg = int(input("Digite o número do seu RG (Apenas números): "))
ano_nasc = int(input("Digite o ano de nascimento: "))
ano_ingresso = int(input("Digite o ano de ingresso na empresa: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - ano_nasc
tempo_trab = ano_atual - ano_ingresso

if idade >= 65:
    print("Requer aposentadoria!")
elif tempo_trab >= 30:
    print("Requer aposentadoria!")
elif idade >= 60 and tempo_trab >= 25:
    print("Requer aposentadoria!")
else:
    print("Não requer aposentadoria!")
