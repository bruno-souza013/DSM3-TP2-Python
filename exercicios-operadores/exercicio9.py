#9 - Leia a quantidade de votos e calcule o percentual de cada de acordo com a quantidade de eleitores
vb = int(input("Digite a quantidade de votos brancos: "))
nul = int(input("Digite a quantidade de votos nulos: "))
valido = int(input("Digite a quantidade de votos válidos: "))
eleitores = vb + nul + valido
pervb = (vb*100)/eleitores
pernul = (nul*100)/eleitores
perval = (valido*100)/eleitores
print(f"A porcentagem de votos brancos: {pervb:.2f}%")
print(f"A porcentagem de votos nulos: {pernul:.2f}%")
print(f"A porcentagem de votos validos: {perval:.2f}%")
print()
