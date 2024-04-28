passw = "senhapoucosegura"
entry = 0
user = str(input("Escreva o seu usuário!\n"))

tries = str(input(f"{user}, você tem 3 tentativas para acertar a senha!\n"))

for i in range(2,0,-1):
    if tries == passw:
        print(f"\nSenha correta!\n")
        print(f"\nSeja bem-vindo {user}!\n")
        entry = 1
        break
    
    tries = str(input(f"{user}, você tem {i} tentativas restantes!\n"))

    if i == 1:
        if tries == passw:
            print(f"\nSenha correta!\n")
            print(f"\nSeja bem-vindo {user}!\n")
            entry = 1
            break
    
if entry == 0:
    print("\nUsuário bloqueado por excesso de tentativas!")