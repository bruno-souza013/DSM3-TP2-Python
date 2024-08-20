#8 - some tres numeros e calcule o quadrado desse resultado
print("Digite 3 números: ")
n1 = float(input())
n2 = float(input())
n3 = float(input())
soma = n1 + n2 + n3
pot = pow(soma,2)
print(f"O resultado da soma de: {n1:.2f} + {n2:.2f} + {n3:.2f} é: {soma:.2f}")
print(f"O quadrado desse total é: {pot:.2f}")
print()