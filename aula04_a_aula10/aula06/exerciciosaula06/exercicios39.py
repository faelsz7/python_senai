#39. Crie um algoritmo que peça ao usuário para digitar
# uma senha e verifique se a senha é "1234".

senha = int(input(' crie uma senha de 4 digitos: \n'))

if (senha == 1234):
    print('sua senha nao pode ser 1234')
else:
    print('aprovado')