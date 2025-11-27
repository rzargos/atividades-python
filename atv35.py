salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
abonos = {}

abono_min = 200
qtd_min = 0

for salario in salarios:
    abono = salario * 0.10
    
    if abono < abono_min:
        abono = abono_min
        qtd_min += 1
        
    abonos[salario] = abono
    
total_gasto = sum(abonos.values())
maior_abono = max(abonos.values())


print("Dicionário de salários e abonos:")
print(abonos)

print(f"\nTotal gasto com abonos: R$ {total_gasto:.2f}")
print(f"Quantidade de colaboradores que receberam o abono mínimo: {qtd_min}")
print(f"Maior abono pago: R$ {maior_abono:.2f}")