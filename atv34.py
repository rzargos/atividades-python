votos = {
    'design_1': 1334,
    'design_2': 982,
    'design_3': 1751,
    'design_4': 210,
    'design_5': 1811
}

total_votos = sum(votos.values())

nome_vencedor = max(votos, key=votos.get)
votos_vencedor = votos[nome_vencedor]

porcentagem = (votos_vencedor / total_votos) * 100

print(f'O design vencedor foi o {nome_vencedor} com um total de {votos_vencedor} votos')
print(f'A porcentagem em relação ao total de votos foi de {porcentagem:.2f}%')