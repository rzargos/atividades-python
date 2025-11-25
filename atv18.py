n = int(input("Digite um número inteiro para calcular o fatorial: "))

fatorial = 1
i = 1   

while i <= n:
    fatorial *= i   
    i += 1          

print(f"O fatorial de {n} é {fatorial}.")
