candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulo = 0
branco = 0

for i in range(1,21):
    voto = int(input('Digite o número do seu candidato (1 a 4), 5 para anular, ou 6 para votar em branco: '))
    
    if voto < 0 or voto > 6:
        print(f'Revise seu voto, {voto} não é uma opção válida')
    elif voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    elif voto == 4:
        candidato4 += 1
    elif voto == 5:
        nulo += 1
    elif voto == 6:
        branco += 1
        
total_votos = candidato1 + candidato2 + candidato3 + candidato4 + nulo + branco

print(f'O número total de votos no candidato 1 foi de {candidato1}')
print(f'O número total de votos no candidato 2 foi de {candidato2}')
print(f'O número total de votos no candidato 3 foi de {candidato3}')
print(f'O número total de votos no candidato 4 foi de {candidato4}')
print(f'O número total de votos nulos foi de {nulo}')
print(f'O número total de votos em branco foi de {branco}')

relacao_nulo = (nulo / total_votos) * 100
relacao_branco = (branco / total_votos) * 100

print(f'A relação de votos nulo foi de {relacao_nulo:.2f}% em relação ao número total de votos')
print(f'A relação de votos em branco foi de {relacao_branco:.2f}% em relação ao número total de votos')