lider = int(input("Qual a pontuação do lider?\n"))
lanterna = int(input("Qual a pontuação do lanterna?\n"))

while lanterna > lider:
    print("Pontuação do lanterna não pode ser maior que a do lider")
    lider = int(input("Qual a pontuação do lider?\n"))
    lanterna = int(input("Qual a pontuação do lanterna?\n"))

q_pontos = lider - lanterna
q_vitorias = q_pontos // 3

if q_pontos % 3 != 0:
    q_vitorias = q_vitorias + 1
    
print(f"O número de vitórias necessárias são: {q_vitorias}")