notas = []

for i in range(1, 16):
    while True:
        nota = int(input(f"Digite a nota {i} (0 a 5): "))
        
        if 0 <= nota <= 5:
            notas.append(nota)
            break
        else:
            print("Valor inválido! A nota deve estar entre 0 e 5. Tente novamente.")

print(f"\nNotas válidas inseridas: {notas}")
