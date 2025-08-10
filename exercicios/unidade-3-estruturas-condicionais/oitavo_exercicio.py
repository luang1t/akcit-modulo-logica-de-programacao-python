#Faça um algoritmo que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostre a classificação dessa pessoa.

#(Altura < 1.20) and (peso <= 60) = A
#(Altura < 1.20) and ((peso > 60) or (peso <= 90)) = D
#(Altura > 1.20 and altura <= 1.7) and (peso <= 60) = B
#(Altura > 1.20 and altura <= 1.7) and ((peso > 60)or(peso <= 90))= E
#(Altura > 1.20 and altura <= 1.7) and (peso > 90) =  H
#(Altura > 1.70) and (peso <= 60) = C
#(Altura > 1.70) and ((peso > 60) or (peso <= 90)) = F
#(Altura > 1.70) and (peso > 90) = I

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

if(altura < 1.20) and (peso <= 60):
    print("A")
elif(altura < 1.20) and ((peso > 60) and (peso <= 90)):
    print("D")
elif(altura > 1.20 and altura <= 1.7) and (peso <= 60):
    print("B") 
elif(altura > 1.20 and altura <= 1.7) and ((peso > 60)and(peso <= 90)):
    print("E")
elif(altura > 1.20 and altura <= 1.7) and (peso > 90):
    print("H")  
elif(altura > 1.70) and (peso <= 60): 
    print("C")   
elif(altura > 1.70) and ((peso > 60) and (peso <= 90)):
    print("F")
else:
    print("I")    