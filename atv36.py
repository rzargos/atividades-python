info = {
 'Área Norte': [2819, 7236],
 'Área Leste': [1440, 9492],
 'Área Sul': [5969, 7496],
 'Área Oeste': [14446, 49688],
 'Área Centro': [22558, 45148]}

medias = {}

for area, especies in info.items():
    media = sum(especies) / len(especies)
    medias[area] = media
    
maior_area = max(info, key=lambda a: sum(info[maior_area]))
maior_valor = sum(info[maior_area])
    
print("Média de espécies por área:")
for area, media in medias.items():
    print(f"{area}: {media:.2f}")

print("\nÁrea com maior diversidade biológica:")
print(f"{maior_area} com {maior_valor} espécies.")