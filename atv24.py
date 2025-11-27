papel = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

total_gasto = sum(papel)
media = sum(papel) / len(papel)

print(f'A média de gastos com papel foi de R${media:.2f}')

acima_3000 = 0
for valor in papel:
    if valor > 3000:
        acima_3000 += 1
        
porcentagem = (acima_3000 / len(papel)) * 100

print(f'A quantidade de compras acima de 3000 foram de: {acima_3000}')
print(f'A porcentagem em relação ao total de compras foi de {porcentagem}%')
    
    


