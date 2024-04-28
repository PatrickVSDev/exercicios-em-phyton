try:    
    sexo =  str(input("Qual seu sexo masculino/M feminino/F = "))
    idade = int(input("Qual sua idade = "))
    contribuição = int(input("Qual seu tempo de contribuição = "))
except ValueError:
   print("Por favor, informe valores válidos para idade e tempo de contribuição (números inteiros).")

if sexo.lower() == "m":
    resul = contribuição + idade 
    if contribuição < 35:
        print("Você não pode se aposentar em 2023 por não ter o tempo de contribuição minimo.")
    elif resul >= 99:
        print("Parabéns! Você pode se aposentar em 2023.")
    elif resul < 99:
        print("Você não pode se aposentar em 2023 de acordo com as regras informadas.")

elif sexo.lower() == "f":
    resul = contribuição + idade 
    if contribuição < 30:
        print("Você não pode se aposentar em 2023 por não ter o tempo de contribuição minimo.")
    elif resul >= 89:
        print("Parabéns! Você pode se aposentar em 2023.")
    elif resul < 89:
        print("Você não pode se aposentar em 2023 de acordo com as regras informadas.")