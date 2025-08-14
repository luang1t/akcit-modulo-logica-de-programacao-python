#Calcule o imposto de renda de um grupo de dez contribuintes, considerando que os dados de cada contribuinte (número de CPF, número de dependentes e renda mensal) são valores fornecidos pelo(a) usuário(a). Para cada contribuinte, será feito um desconto de 5% do salário mínimo por dependente. Observe que deve ser fornecido o valor atual do salário mínimo para que o algoritmo calcule os valores corretamente. Os valores da alíquota para cálculo do imposto são:

#        RENDA LÍQUIDA              |       ALÍQUOTA
#ATÉ 2 SALARIOS MINIMOS (INCLUSIVE) |   ISENTO
#2 A 3 SALARIOS MINIMOS (INCLUSIVE) |   5%
#3 A 4 SALARIOS (INCLUSIVE)         |   10%
#5 A 7 SALARIOS (INCLUSIVE)         |   15%
#ACIMA DE 7 SALARIOS MINIMOS        |   20%

numero_contribuintes = int(input("Digite o numero de contribuintes: "))
desconto_dependente = float('-inf')
salario_minimo = float(input("Digite o salario minimo atual: "))
salario_desconto_depende = 0

for i in range(numero_contribuintes):
    cpf = int(input("Digite o seu cpf: "))
    numero_dependentes = int(input("Digite o numero de dependentes: "))
    renda_mensal = float(input("Digite sua renda mensal: "))

    if numero_dependentes > 0:
        percentual_salario = salario_minimo * 0.05
        desconto_dependente = numero_dependentes * percentual_salario
        salario_desconto_depende = renda_mensal - desconto_dependente
    
    if(salario_desconto_depende>0):
        if salario_desconto_depende <= salario_minimo * 2:
            print("Insento")

        elif salario_desconto_depende > salario_minimo * 2 and salario_desconto_depende <= salario_minimo * 3:
            print("5%")
            cinco_porcento = salario_desconto_depende * 0.05
            novo_salario = salario_desconto_depende - cinco_porcento
            print(f"R$:{novo_salario} desconto de R${cinco_porcento}") 

        elif salario_desconto_depende > salario_minimo * 3 and salario_desconto_depende <= salario_minimo * 4:
            print("10%")
            dez_porcento = salario_desconto_depende * 0.1
            novo_salario = salario_desconto_depende - dez_porcento
            print(f"R$:{novo_salario} desconto de R${dez_porcento}")

        elif salario_desconto_depende > salario_minimo * 5 and salario_desconto_depende <= salario_minimo * 7:
            print("15%")
            quinze_porcento = salario_desconto_depende * 0.15
            novo_salario = salario_desconto_depende - quinze_porcento
            print(f"R$:{novo_salario} desconto de R${quinze_porcento}") 

        else: 
            print("20%")
            vinte_porcento = salario_desconto_depende * 0.2
            novo_salario = salario_desconto_depende - vinte_porcento
            print(f"R$:{novo_salario} desconto de R${vinte_porcento}") 

    else:
        if renda_mensal <= salario_minimo * 2:
            print("Insento")

        elif renda_mensal > salario_minimo * 2 and renda_mensal <= salario_minimo * 3:
            print("5%")
            cinco_porcento = renda_mensal * 0.05
            novo_salario = renda_mensal - cinco_porcento
            print(f"R$:{novo_salario} desconto de R${cinco_porcento}") 

        elif renda_mensal > salario_minimo * 3 and renda_mensal <= salario_minimo * 4:
            print("10%")
            dez_porcento = renda_mensal * 0.1
            novo_salario = renda_mensal - dez_porcento
            print(f"R$:{novo_salario} desconto de R${dez_porcento}")

        elif renda_mensal > salario_minimo * 5 and renda_mensal <= salario_minimo * 7:
            print("15%")
            quinze_porcento = renda_mensal * 0.15
            novo_salario = renda_mensal - quinze_porcento
            print(f"R$:{novo_salario} desconto de R${quinze_porcento}") 

        else: 
            print("20%")
            vinte_porcento = renda_mensal * 0.2
            novo_salario = renda_mensal - vinte_porcento
            print(f"R$:{novo_salario} desconto de R${vinte_porcento}")                      


