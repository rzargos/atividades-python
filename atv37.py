idades = {
 'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

todas_as_idades = []
acima_media = 0

for setor, idade in idades.items():
    
    soma_idades = sum(idade)
    media_setor = int(sum(idade) / len(idade))
    
    print(f'A média de idades do Setor {setor} é de {media_setor}')
    
for lista_idades in idades.values():
    
    todas_as_idades.extend(lista_idades)
    media_geral = int(sum(todas_as_idades) / len(todas_as_idades))
        
    print(f'Média geral das idades: {media_geral}')

    
for idade in todas_as_idades:
    if idade > media_geral:
        acima_media += 1
        
print(f'Existem {acima_media} pessoas com idade acima da média geral')
