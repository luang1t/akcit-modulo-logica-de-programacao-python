#Tendo como dados de entrada, a altura e o sexo de uma pessoa, construa um algoritmo que calcule o peso ideal, utilizando as fórmulas abaixo, onde H é a altura da pessoa:
#se o sexo for masculino: (72.7*H)-58;
#se o sexo for feminino: (62.1*H)-44.7.

altura = float(input("Digite sua altura: "))
sexo = str(input("Informe o seu sexo.\nDigite M para mulher e H para homem: "))

if(sexo=='M' or sexo=='m'):
    peso_ideal_mulher = (62.1*altura) - 44.7
    print(f"Seu peso ideal sendo mulher e tendo {altura}m de altura é {peso_ideal_mulher}kg")
elif(sexo=='H' or sexo=='h'):
    peso_ideal_homem = (72.7*altura) - 58    
    print(f"Seu peso ideal sendo homem e tendo {altura}m de altura é {peso_ideal_homem}kg")
else:
    print("Digitou algo errado. Volte e digite o solicitado!")    