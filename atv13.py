quantidade_vendas_2024 = int(input('Quantas vendas foram realizadas no ano de 2024: '))
quantidade_vendas_2025 = int(input('Quantas vendas foram realizadas no ano de 2025: '))

variacao_percentual = ((quantidade_vendas_2025 - quantidade_vendas_2024) / quantidade_vendas_2024) * 100

if variacao_percentual > 20:
    print(f'Nossa variação a partir do ano passado foi de {variacao_percentual}%, todos ganharão uma grande bonificação!')
elif 2 <= variacao_percentual <= 20:
     print(f'Nossa variação a partir do ano passado foi de {variacao_percentual}%, todos ganharão uma pequena bonificação!')
elif -10 <= variacao_percentual <= 2:
    print(f'Nossa variação a partir do ano passado foi de {variacao_percentual}%, teremos um novo planejamento de  incentivo às vendas')
else:
    print(f'Nossa variação a partir do ano passado foi de {variacao_percentual}%, teremos um corte de gastos')