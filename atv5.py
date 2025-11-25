precoProduto1 = float(input("Digite o preço do primeiro produto: "))
precoProduto2 = float(input("Digite o preço do segundo produto: "))
precoProduto3 = float(input("Digite o preço do terceiro produto: "))

precoProdutos = [precoProduto1,precoProduto2,precoProduto3]

maisBarato = min(precoProdutos)

print(f'O produto mais barato é o produto com valor de R${maisBarato:.2f}')