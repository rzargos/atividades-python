vendas = {
    'Produto A': 300,
    'Produto B': 80,
    'Produto C': 60,
    'Produto D': 200,
    'Produto E': 250,
    'Produto F': 30
 }

total_vendas = sum(vendas.values())
print(f'Total de vendas: {total_vendas}')

produto_mais_vendido = max(vendas, key=vendas.get)
quantidade_mais_vendida = vendas[produto_mais_vendido]

print(f"Produto mais vendido: {produto_mais_vendido} ({quantidade_mais_vendida} unidades)")