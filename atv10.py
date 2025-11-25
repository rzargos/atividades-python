# Lê dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\nEscolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite o número da operação desejada: ")

# Realiza a operação escolhida
if opcao == "1":
    resultado = num1 + num2
    oper = "Soma"
elif opcao == "2":
    resultado = num1 - num2
    oper = "Subtração"
elif opcao == "3":
    resultado = num1 * num2
    oper = "Multiplicação"
elif opcao == "4":
    if num2 == 0:
        print("Erro: divisão por zero não é permitida!")
        exit()
    resultado = num1 / num2
    oper = "Divisão"
else:
    print("Opção inválida!")
    exit()

# -------------------------
# Verificações sobre o número
# -------------------------

# Verifica se é positivo, negativo ou zero
if resultado > 0:
    sinal = "positivo"
elif resultado < 0:
    sinal = "negativo"
else:
    sinal = "zero"

# Verifica se é inteiro ou decimal
if resultado.is_integer():
    tipo = "inteiro"
else:
    tipo = "decimal"

# Verifica se é par ou ímpar (só faz sentido para inteiros)
if resultado.is_integer():
    if resultado % 2 == 0:
        paridade = "par"
    else:
        paridade = "ímpar"
else:
    paridade = "não é possível definir (número decimal)"

# -------------------------
# Exibe o resultado
# -------------------------

print(f"\nOperação escolhida: {oper}")
print(f"Resultado: {resultado}")

print("\nClassificação do número:")
print(f"- O número é {sinal}")
print(f"- O número é {tipo}")
print(f"- O número é {paridade}")
