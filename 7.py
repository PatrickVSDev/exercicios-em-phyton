import random

def jogar_dado():
    return random.randint(1, 6)

def verificar_vencedor(jogador_a, jogador_b):
    if jogador_a > jogador_b:
        return "A"
    elif jogador_a < jogador_b:
        return "B"
    else:
        return "Empate"

jogador_a = jogar_dado()
jogador_b = jogar_dado()

print(f"Jogador A obteve o número: {jogador_a}")
print(f"Jogador B obteve o número: {jogador_b}")

resultado = verificar_vencedor(jogador_a, jogador_b)

if resultado == "Empate":
    print("Empate! Nenhum jogador venceu.")
else:
    print(f"Jogador {resultado} venceu!")