#Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma certa cidade em um determinado dia. Para cada casa pesquisada, foi coletado o número do canal (5, 7, 10 ou 12) e o número de pessoas que o estavam assistindo naquela casa. Faça um algoritmo que receba esses dados da pesquisa, calcule e mostre a porcentagem de audiência de cada emissora. Termine a entrada dos dados da pesquisa informando o número do canal como sendo 0.

canal_e_sair = int(input("Digite o canal desejado (5, 7, 10 ou 12) ou (0) para sair do programa: "))
pessoas_assistindo = 0
numero_10 = 0
numero_5 = 0
numero_7 = 0
numero_12 = 0

while True:
    if canal_e_sair == 5:
        pessoas_assistindo = int(input("Digite quantas pessoas estão assistindo: "))
        numero_5 += pessoas_assistindo
    elif canal_e_sair == 7:
        pessoas_assistindo = int(input("Digite quantas pessoas estão assistindo: "))  
        numero_7 += pessoas_assistindo 
    elif canal_e_sair == 10:
        pessoas_assistindo = int(input("Digite quantas pessoas estão assistindo: "))
        numero_10 += pessoas_assistindo 
    elif canal_e_sair == 12:
        pessoas_assistindo = int(input("Digite quantas pessoas estão assistindo: ")) 
        numero_12 += pessoas_assistindo
    elif canal_e_sair == 0:
        break    
    else:
        print("Apenas são aceitos (5, 7, 10 ou 12) ou (0) para finalizar o programa!")
    canal_e_sair = int(input("Digite o canal desejado (5, 7, 10 ou 12) ou (0) para sair do programa: "))    

audiencia_total = numero_5+numero_7+numero_10+numero_12
if audiencia_total>0:
    porcentagem_5 = (numero_5/audiencia_total)*100             
    porcentagem_7 = (numero_7/audiencia_total)*100             
    porcentagem_10 = (numero_10/audiencia_total)*100             
    porcentagem_12 = (numero_12/audiencia_total)*100
    print(f"Audiencia total:\n{audiencia_total} Espectadores")  
    print(f"5 com {porcentagem_5}%")
    print(f"7 com {porcentagem_7}%") 
    print(f"10 com {porcentagem_10}%") 
    print(f"12 com {porcentagem_12}%")
else:
    print("Sem nenhum dado contabilizado")          
        