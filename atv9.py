num = input("Digite um número: ")

try:
    valor = float(num)

    if valor.is_integer():
        print("O número é inteiro.")
    else:
        print("O número é decimal.")

except ValueError:
    print("Entrada inválida! Digite um número válido.")
