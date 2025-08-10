#Escreva um algoritmo que leia o nome do vendedor, o seu salário base mensal e o valor do total de vendas realizadas por ele durante o mês. Sabendo que este vendedor recebe comissão de 15% sobre o valor das vendas efetuadas por ele e que o seu salário final é a composição do salário base mais o valor da comissão, calcule e mostre o nome do vendedor, seu salário final e a porcentagem recebida a mais em relação ao seu salário base mensal.

nome_vendedor = str(input("Digite o nome do vendedor: "))
salario_base_mensal = float(input("Digite seu salário base: "))
total_vendas = float(input("Digite o valor total arrecadado em vendas: "))

comissao = total_vendas * 0.15

salario_final = salario_base_mensal+comissao

print(f"Graças a suas vendas esse mês você teve o total de 15% sobre total delas. O valor de R$:{comissao:.2f} foi acrescentado ao seu salário atual de R$:{salario_base_mensal:.2f} foi para R$:{salario_final:.2f}")
