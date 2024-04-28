nome = str(input("Escreva o seu nome!\n"))
av1 = float(input("Escreva a nota da sua prova 1! (0.0 a 10.0)\n"))
av2 = float(input("Escreva a nota da sua prova 2! (0.0 a 10.0)\n"))
proj = float(input("Escreva a nota do seu projeto! (0.0 a 10.0)\n"))

av1 = av1 * 0.7
av2 = av2 * 0.7
proj = proj * 0.3

mf = (av1 + av2 + proj) / (0.7 + 0.7 + 0.3)

if mf < 6:
    sit = "Reprovado!"

elif mf >= 6:
    sit = "Aprovado!"

mf = format(mf, ".1f")

print(f"\n{nome} - {mf} - {sit}")