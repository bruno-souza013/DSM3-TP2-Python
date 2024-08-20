#10 - Calcular o volume de um cilindro
from math import pi
raio = float(input("Digite o raio do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))
vol = pi * pow(raio,2) * altura
print(f"O volume do cilindro é: {vol:.2f}")
