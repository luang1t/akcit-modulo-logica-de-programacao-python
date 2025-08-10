#Faça um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem decrescente. Utilize, para tal, uma seleção encadeada.
primeiro = int(input("Digite o primeiro numero: "))
segundo = int(input("Digite o segundo numero: "))
terceiro = int(input("Digite o terceiro numero: "))


if(primeiro>=segundo and segundo>=terceiro):
    print(f"{primeiro},{segundo},{terceiro}")
elif(primeiro>=terceiro and terceiro>=segundo ):
    print(f"{primeiro},{terceiro},{segundo}")
elif(segundo>=primeiro and primeiro>=terceiro ):
    print(f"{segundo},{primeiro},{terceiro}")
elif(segundo>=terceiro and terceiro>=primeiro ):
    print(f"{segundo},{terceiro},{primeiro}")
elif(terceiro>=primeiro and primeiro>=segundo):
    print(f"{terceiro},{primeiro},{segundo}") 
else:
    print(f"{terceiro},{segundo},{primeiro}")  
    
                                              
