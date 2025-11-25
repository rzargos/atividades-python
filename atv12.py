tipoCombustivel = input('Qual o combustível escolhido? (E para Etanol e D para Diesel: )').upper()
quantidadeLitros = float(input('Quantos litros foram abastecidos: '))

valorEtanol = 1.70
valorDiesel = 2.00

if tipoCombustivel == 'E' and quantidadeLitros > 15:
    descontoEtanol = 0.96 # 4% de desconto
    valorEtanol = (valorEtanol * descontoEtanol)
    valorTotal = quantidadeLitros * valorEtanol
    print(f'O valor a ser pago é de R${valorTotal:.2f}')
elif tipoCombustivel == 'E' and quantidadeLitros <= 15:
    descontoEtanol = 0.98  # 2% de desconto
    valorEtanol = (valorEtanol * descontoEtanol)
    valorTotal = quantidadeLitros * valorEtanol
    print(f'O valor a ser pago é de R${valorTotal:.2f}')
    
if tipoCombustivel == 'D' and quantidadeLitros > 15:
    descontoDiesel = 0.95 # 5% de desconto
    valorDiesel = (valorDiesel * descontoDiesel)
    valorTotal = quantidadeLitros * valorDiesel
    print(f'O valor a ser pago é de R${valorTotal:.2f}')
elif tipoCombustivel == 'D' and quantidadeLitros <= 15:
    descontoDiesel = 0.97  # 3% de desconto
    valorDiesel = (valorDiesel * descontoDiesel)
    valorTotal = quantidadeLitros * valorDiesel
    print(f'O valor a ser pago é de R${valorTotal:.2f}')