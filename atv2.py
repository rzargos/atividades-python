percentual = float(input("Informe o percentual de crescimento (%): "))

if percentual > 0:
    print(f"Houve crescimento de {percentual}%.")
elif percentual < 0:
    print(f"Houve decrescimento de {percentual}%.")
else:
    print("Não houve crescimento nem decrescimento (percentual igual a 0).")
