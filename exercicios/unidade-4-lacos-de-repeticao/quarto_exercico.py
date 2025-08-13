#Construa um algoritmo que receba um número inteiro maior que 1, verifique se o número fornecido é primo ou não e mostre mensagem de número primo ou de número não primo. Um número é primo quando é divisível naturalmente apenas por 1 e por ele mesmo, ou seja, quando não há resto na divisão.
print("VERIFICADOR DE NUMERO PRIMO")
points = 0
seletor = " "

while seletor != 'S':
    seletor_input = str(input("DIGITE 'R' PARA INICIAR E 'S' PARA SAIR: "))
    seletor = seletor_input.upper()
    print(seletor)
    if(seletor == 'R'):
        soma = 0
        numero = int(input("Digite um número: "))
        interacao_for = numero
        for i in range (1,(interacao_for+1)):
            if(numero % i == 0):
                soma += 1
        if(soma==2):
            print("Não primo")
        else:
            print("Primo")                    
    elif(seletor == 'S'):
        break
    else:
        print("Digite algo 'R' ou 'S'")            
