# Faça um algoritmo que receba o nome e o valor de um produto qualquer, calcule e mostre o valor das prestações, sabendo que o seu valor é dividido em 5x sem juros.

produto_nome = str(input("Digite o nome do produto: "))
produto_peco = float(input("Digite o valor do produto: ")) 
print(f"Você comprou {produto_nome} no valor de R$:{produto_peco} e vai parcelar em 5x de:")
prestacao_preco = produto_peco/5
n=5
while n!=0:
    print(f"{n}x - R$:{prestacao_preco: .2f}")
    n-=1
print("Ou seja, sem juros OMG!!!")    