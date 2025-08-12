#Faça um algoritmo que escreva a tabuada de multiplicação completa dos números de 1 a 10, utilizando uma estrutura de repetição.

condicao = True
numero = 1
resultado = 0

while condicao:
    
    if(numero<=10):
        print(f"Tabuada do {numero}:")
        for i in range (1,11):
            resultado = numero * i
            print(f"{numero}x{i}={resultado}")
        numero+=1
    else:
        condicao = False