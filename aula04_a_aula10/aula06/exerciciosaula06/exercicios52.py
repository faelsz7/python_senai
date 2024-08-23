#FUI INCAPAZ DE FAZER SEM CHAT GPT

senha_correta = "1234"
while True:
    senha_digitada = input("Digite a senha: ")
    if senha_digitada == senha_correta:
        print("Acesso permitido!")
        break
    else:
        print("Senha incorreta. Tente novamente.")
