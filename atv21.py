faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0

while True:
    idade = int(input('Digite sua idade: '))
    
    if idade < 0:
        break
    
    if 0 <= idade <= 25:
        faixa1 += 1
    elif 26 <= idade <= 50:
        faixa2 += 2
    elif 51 <= idade <= 75:
        faixa3 += 1
    elif 76 <= idade <= 100:
        faixa4 += 1
    else:
        print('Idade fora do intervalo esperado (0,100). Não será contabilizada')
        
print("\nDistribuição das idades:")
print(f"0 - 25 anos: {faixa1}")
print(f"26 - 50 anos: {faixa2}")
print(f"51 - 75 anos: {faixa3}")
print(f"76 - 100 anos: {faixa4}")
