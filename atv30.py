doces = 0
amargos = 0
contador = 1

while contador <= 10:
    id_produto = int(input(f"Digite o ID do produto {contador}: "))

    if id_produto % 2 == 0:  # par → doce
        doces += 1
    else:  # ímpar → amargo
        amargos += 1

    contador += 1

print("\nQuantidade de produtos doces:", doces)
print("Quantidade de produtos amargos:", amargos)
