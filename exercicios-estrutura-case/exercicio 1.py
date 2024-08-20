#Verificação de letra consoante ou vogal

letra = (input("Digite uma letra para verificar se é vogal ou consoante: \n"))

match (letra.lower()):
    case "a":
        print(f"Letra digitada: {letra}, é vogal.")
    case "e":
        print(f"Letra digitada: {letra}, é vogal.")
    case "i":
        print(f"Letra digitada: {letra}, é vogal.")
    case "o":
        print(f"Letra digitada: {letra}, é vogal.")
    case "u":
        print(f"Letra digitada: {letra}, é vogal.")
    case _:
        print(f"Letra digitada: {letra}, é consoante.")