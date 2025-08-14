#Faça um algoritmo que receba o valor do salário mínimo atual. Receba também a quantidade de quilowatts consumidos e o código do tipo de consumidor de um conjunto de consumidores de quantidade inicial desconhecida, calcule e mostre:
#o valor de cada quilowatt, sabendo que o quilowatt custa 1/1.000 do salário mínimo informado;
#o valor a ser pago por cada consumidor, incluindo o acréscimo do tipo de consumidor. O acréscimo encontra-se na tabela a seguir:

#o faturamento geral da empresa;
#a quantidade de consumidores que pagam entre R$500,00 e R$1.000,00 de conta de energia
#Termine a entrada de dados do conjunto de consumidores com a quantidade de quilowatts igual a 0.

codigo = int(input("Digite o código\n1 - Residencial\n2 - Comercial\n3 - Industrial\n0 - Sair\n"))
faturamento_geral = 0
soma_consumidores = 0
while True:
    if codigo == 1:
        quillowatt_consumidos = float(input("Digite quantos quillowat você consumiu: "))
        salario_minimo = float(input("Digite o salário minimo: "))
        quilowatt_hora = salario_minimo*0.001
        valor_quillowat_consumido = quilowatt_hora*quillowatt_consumidos
        valor_quillowat_taxa = valor_quillowat_consumido + (valor_quillowat_consumido*0.05)
        faturamento_geral +=valor_quillowat_taxa
        if 500 <= valor_quillowat_taxa <= 1000:
            soma_consumidores+=1
             

    elif codigo == 2:
        quillowatt_consumidos = float(input("Digite quantos quillowat você consumiu: "))
        salario_minimo = float(input("Digite o salário minimo: "))
        quilowatt_hora = salario_minimo*0.001
        valor_quillowat_consumido = quilowatt_hora*quillowatt_consumidos
        valor_quillowat_taxa = valor_quillowat_consumido + (valor_quillowat_consumido*0.1)
        faturamento_geral +=valor_quillowat_taxa
        if 500 <= valor_quillowat_taxa <= 1000:
            soma_consumidores+=1 

    elif codigo == 3:
        quillowatt_consumidos = float(input("Digite quantos quillowat você consumiu: "))
        salario_minimo = float(input("Digite o salário minimo: "))
        quilowatt_hora = salario_minimo*0.001
        valor_quillowat_consumido = quilowatt_hora*quillowatt_consumidos
        valor_quillowat_taxa = valor_quillowat_consumido + (valor_quillowat_consumido*0.15)
        faturamento_geral +=valor_quillowat_taxa
        if 500 <= valor_quillowat_taxa <= 1000:
            soma_consumidores+=1

    elif codigo == 0:
        break

    else:
        print("Digite algo entre 1,2,3 ou 0 para finalizar")
    print("Proximo:")
    codigo = int(input("Digite o código\n1 - Residencial\n2 - Comercial\n3 - Industrial\n0 - Sair\n"))
print(f"faturamento geral da empresa:\nR$:{faturamento_geral}")
print(f"quantidade de consumidores que pagam entre 500 e 1000 {soma_consumidores}")

