#Calculo de lucro em relação ao valor do produto. abaixo de R$20,00 45% de lucro, acima de R$20,00 30% de lucro

prod = float(input("Digite o valor pago pelo produto: R$"))

if prod <= 20:
    tot = prod + ((prod * 45)/100)
    print(f"Valor ideal para venda com 45% de lucro: R${tot:.2f}")
else:
    tot = prod + ((prod * 30)/100)
    print(f"Valor ideal para venda com 30% de lucro: R${tot:.2f}")