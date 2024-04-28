lider = int(input("Qual a pontuação do lider?\n"))
lanterna = int(input("Qual a pontuação do lanterna?\n"))

while lanterna > lider:
    print("O lanterna tem mais pontos do que o lider!")
    print("Digite novamente!")
    lider = int(input("Qual a pontuação do lider?\n"))
    lanterna = int(input("Qual a pontuação do lanterna?\n"))

q_pontos = lider - lanterna
q_vitorias = q_pontos // 3
q_empates = 0

if q_pontos % 3 != 0:
    while q_empates + (q_vitorias * 3) < q_pontos:
        q_empates = q_empates + 1
print(f"O número de vitórias necessárias são: {q_vitorias} e de empates são: {q_empates}")

