capacidade = 10
vagas = [0] * capacidade

while True:
    print("\nMenu:")
    print("1 - Adicionar carro")
    print("2 - Liberar carro")
    print("3 - Verificar status")
    print("4 - Sair")
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        numero_vaga = int(input("Digite o número da vaga: "))
        placa = input("Digite a placa do carro: ")
        if 1 <= numero_vaga <= capacidade:
            if vagas[numero_vaga - 1] == 0:
                vagas[numero_vaga - 1] = placa
                print(f"Carro com placa {placa} estacionado na vaga {numero_vaga}.")
            else:
                print(f"A vaga {numero_vaga} já está ocupada pelo carro com placa {vagas[numero_vaga - 1]}.")
        else:
            print("Número de vaga inválido.")

    elif escolha == 2:
        numero_vaga = int(input("Digite o número da vaga: "))
        if 1 <= numero_vaga <= capacidade:
            if vagas[numero_vaga - 1] != 0:
                placa = vagas[numero_vaga - 1]
                vagas[numero_vaga - 1] = 0
                print(f"Carro com placa {placa} liberado da vaga {numero_vaga}.")
            else:
                print(f"A vaga {numero_vaga} já está vazia.")
        else:
            print("Número de vaga inválido.")

    elif escolha == 3:
        for numero_vaga in range(1, capacidade + 1):
            placa = vagas[numero_vaga - 1]
            if placa != 0:
                print(f"{numero_vaga} - {placa}")
            else:
                print(f"{numero_vaga} - Vazio")

    elif escolha == 4:
        break

    else:
        print("Opção inválida. Tente novamente.")