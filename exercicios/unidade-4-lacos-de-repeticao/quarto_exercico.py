#Construa um algoritmo que receba um número inteiro maior que 1, verifique se o número fornecido é primo ou não e mostre mensagem de número primo ou de número não primo. Um número é primo quando é divisível naturalmente apenas por 1 e por ele mesmo, ou seja, quando não há resto na divisão.
print("VERIFICADOR DE NUMERO PRIMO")
seletor = " "
while seletor != 'S':
    seletor_input = str(input("DIGITE 'R' PARA INICIAR E 'S' PARA SAIR: "))
    seletor = seletor_input.upper()
    print(seletor)
    if(seletor == 'R'):
        numero_digitado = float(input("Digite o numero para saber se é primo: "))
        if(numero_digitado % 1 == 0 and numero_digitado % numero_digitado == 0 and numero_digitado % 2 != 0):
            print("Primo")
        else:
            print("Não primo")
    elif(seletor == 'S'):
        break
    else:
        print("Digite algo 'R' ou 'S'")            
