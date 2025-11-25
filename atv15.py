colA = 4
colB = 10

dias = 0

while colA < colB:
    dias += 1
    colA = colA * 1.03
    colB = colB * 1.015
    
print(f'Levará {dias} dias para a colônia A se igualar ou ultrapassar a B')
print(f'Colônia A = {colA}')
print(f'Colônia B = {colB}')