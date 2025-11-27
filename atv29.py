bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
crescimentos = []

i = 1

while i < len(bacterias):
    atual = bacterias[i]
    anterior = bacterias[i - 1]
    
    crescimento = 100 * (atual-anterior) / anterior
    
    crescimentos.append(crescimento)
    
    i += 1
    
print("Percentual de crescimento por dia:")
print(crescimentos)
    
    