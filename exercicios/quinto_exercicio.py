#Faça um algoritmo que receba o preço de custo de um produto e a margem de lucro sobre o mesmo em porcentagem (%), calcule e mostre o preço de venda já com o lucro incluído.
nome_produto = str(input("Digite o nome do produto: "))
preco_custo = float(input("Digite o valor de custo do produto: "))
margem_lucro = float(input("Digite a margem de lucro desejada: "))

lucro_desejado_bruto = preco_custo*(margem_lucro/100)
preco_venda = preco_custo + lucro_desejado_bruto

print(f"O produto {nome_produto} tem um valor de fabricação de R$:{preco_custo:.2f} e com o seu lucro desejado de {margem_lucro:.2f}% teremos o valor de R$:{lucro_desejado_bruto:.2f} de lucro desejado ou seja tem que vender o produto com um valor de R$:{preco_venda:.2f}.")

