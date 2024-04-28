import random

def insercao_ordenada(vetor):
    for i in range(1, len(vetor)):
        guardar = vetor[i]
        j = i - 1
        while j >= 0 and guardar > vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = guardar

def inserir_valor(vetor, valor_novo):
    if len(vetor) == 10:
        if valor_novo >= vetor[-1]:
            vetor[-1] = valor_novo
            for i in range(len(vetor) - 1, 0, -1):
                if vetor[i] > vetor[i - 1]:
                    vetor[i], vetor[i - 1] = vetor[i - 1], vetor[i]
                else:
                    break

def remove_valor(vetor, valor_remover):
    if valor_remover in vetor:
        vetor.remove(valor_remover)
        vetor.append(0)
        insercao_ordenada(vetor)
        vetor.pop()

random_numbers = sorted([random.randint(0, 1000) for _ in range(10)], reverse=True)

while True:
    print("\nVetor atual:", random_numbers)
    print("1 - Inserir valor")
    print("2 - Remover valor")
    print("3 - Sair")
    escolha = int(input("Escolha uma opção: "))
    
    if escolha == 1:
        numero_novo = random.randint(0, 1000)
        print(f"Tentando inserir o número {numero_novo} no vetor.")
        inserir_valor(random_numbers, numero_novo)
    elif escolha == 2:
        remover_valor = int(input("Digite o valor a ser removido: "))
        print(f"Tentando remover o valor {remover_valor} do vetor.")
        remove_valor(random_numbers, remover_valor)
    elif escolha == 3:
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Escolha novamente.")
