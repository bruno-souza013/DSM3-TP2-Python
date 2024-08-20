#12 - calcular a area de uma parede e do azulejo, em seguida calcular quantos são necessarios para azulejar a parede
alturaparede = float(input("Digite a altura da parede: "))
larguraparede = float(input("Digite a largura da parede: "))
alturazulejo = float(input("Digite a altura do azulejo: "))
larguraazulejo = float(input("Digite a largura do azulejo: "))
areaparede = alturaparede * alturaparede
areaazulejo = alturazulejo * larguraazulejo
totalazulejo = areaparede / areaazulejo
print(f"Para azulejar uma parede de area {areaparede:.2f} metros é necessário {totalazulejo:.2f} azulejos")