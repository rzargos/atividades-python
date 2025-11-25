soma = 0
quantidade = 0

while True:
    temp = float(input("Digite uma temperatura em °C (ou -273 para encerrar): "))

    if temp == -273:
        break

    soma += temp
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"A média das temperaturas é: {media:.2f}°C")
else:
    print("Nenhuma temperatura válida foi inserida.")
