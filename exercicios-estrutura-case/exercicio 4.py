#Calculo valor da compra e desconto

val = float(input("Digite o valor da compra: R$"))
op = int(input(" 1 - Á vista (15% Desconto) \n 2 - Cartão Débito (10% Desconto) \n 3 - Cartão crédito (5% Desconto) \n Escolha a opção referente a forma de pagamento: \n"))

match op:
    case 1:
        total = val - ((val * 15)/100)
        print(f"Forma de pagamento: A vista, valor total com desconto de 15% - R${total:.2f}")
    case 2:
        total = val - ((val * 10)/100)
        print(f"Forma de pagamento: Cartão Débito, valor total com desconto de 10% - R${total:.2f}")
    case 3:
        total = val - ((val * 5)/100)
        print(f"Forma de pagamento: Cartão crédito, valor total com desconto de 5% - R${total:.2f}")
    case _:
        print("Digite uma opção válida!")
