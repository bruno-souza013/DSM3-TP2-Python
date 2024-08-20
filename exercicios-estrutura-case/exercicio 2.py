#leia o indice de poluição e exiba a mensagem correspondente
op = int(input("Digite o índice de poluição, sendo: \n 0 até 2 - Aceitável \n 3 até 5 - Suspender atividades Grupo I \n 6 até 7 - Suspender atividades Grupo I e II \n Acima de 8 - Suspender atividades de todos os grupos. \n"))

match op:
    case 0 | 1 | 2:
        print("Aceitável")
    case 3 | 4 | 5:
        print("Suspender atividades do Grupo I")
    case 6 | 7:
        print("Suspender atividades do Grupo I e II")
    case _:
        print("Suspender atividades de todos os Grupos")
        
