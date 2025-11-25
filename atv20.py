num = int(input('Digite o número para saber se é primo: '))

if num <= 1:
    print(f'{num} não é um número primo')
else:
    primo = True
    
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
        
    if primo:
        print(f'{num} é um número primo!')
    else:
        print(f'{num} não é um número primo!')