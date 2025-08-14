#Elabore um algoritmo que seja capaz de obter o quociente inteiro da divisão de dois números fornecidos, sem utilizar a operação de divisão (/).

a= int(687)
b= int(8)
c = int(0)
while a >= b:    
    c+=1
    a -= b
quociente = b*c    
print(c,quociente)