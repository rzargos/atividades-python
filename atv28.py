dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

data_valida = True

# Verifica se o mês é válido
if mes < 1 or mes > 12:
    data_valida = False

# Define quantidade de dias por mês
elif mes in [1, 3, 5, 7, 8, 10, 12]:
    max_dias = 31
elif mes in [4, 6, 9, 11]:
    max_dias = 30
elif mes == 2:
    # Verifica se é ano bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        max_dias = 29
    else:
        max_dias = 28

# Verifica se o dia é válido para o mês
if dia < 1 or dia > max_dias:
    data_valida = False

# Resultado final
if data_valida:
    print("A data é válida!")
else:
    print("A data é inválida!")
