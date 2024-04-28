import random

def gerar_matriz_pixels(reta, colunas):
    matriz = [[random.randint(0, 255) for _ in range(colunas)] for _ in range(reta)]
    return matriz

def exibir_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(f"{valor:3}", end=" ")  
        print()  
reta = 10
colunas = 10

matriz_pixels = gerar_matriz_pixels(reta, colunas)

print("Matriz de 10x10 pixels:")
exibir_matriz(matriz_pixels)