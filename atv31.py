gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']

nota = 0
i = 0

while i < 10:
    resposta = input(f"Resposta da questão {i+1}: ").upper()

    # Verifica se digitou A, B, C ou D
    while resposta not in ['A', 'B', 'C', 'D']:
        print("Resposta inválida! Digite A, B, C ou D.")
        resposta = input(f"Resposta da questão {i+1}: ").upper()

    if resposta == gabarito[i]:
        nota += 1

    i += 1

print("\nNota final do aluno:", nota)

