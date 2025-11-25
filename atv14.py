num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))

inicio = min(num1, num2)
fim = max(num1, num2)

print('Números entre eles: ')

for i in range(inicio + 1, fim):
    print(i)