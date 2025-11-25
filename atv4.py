preco_ano1 = float(input("Digite o preço médio do carro no 1º ano: "))
preco_ano2 = float(input("Digite o preço médio do carro no 2º ano: "))
preco_ano3 = float(input("Digite o preço médio do carro no 3º ano: "))

precos = [preco_ano1, preco_ano2, preco_ano3]

maior_preco = max(precos)
menor_preco = min(precos)

print(f"O maior preço foi: R$ {maior_preco:.2f}")
print(f"O menor preço foi: R$ {menor_preco:.2f}")