num = int(input('Digite um número inteiro positivo qualquer: '))

lista_primos = []
n = 1

while n <= num:
    if n > 1:
        divisor = 2
        eh_primo = True
        
        while divisor <= int(n**0.5):
            if n % divisor == 0:
                eh_primo = False
                break
            divisor += 1
            
        if eh_primo:
            lista_primos.append(n)
            
    n += 1
    
print("Números primos entre 1 e", num, ":", lista_primos)
