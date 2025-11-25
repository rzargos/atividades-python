lado1 = float(input('Digite o valor do primeiro lado do triângulo'))
lado2 = float(input('Digite o valor do segundo lado do triângulo'))
lado3 = float(input('Digite o valor do terceiro lado do triângulo'))

if lado1 + lado2 < lado3:
    print('Esse triângulo não é possível')
elif lado2 + lado3 < lado1:
    print('Esse triângulo não é possível')
else: 
    print('Esses valores podem ser usados para fazer um triângulo')
    if lado1 == lado2 == lado3:
        print('Esse triângulo é equilátero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Esse triângulo é isóceles')
    else:
        print('Esse triângulo é escaleno')