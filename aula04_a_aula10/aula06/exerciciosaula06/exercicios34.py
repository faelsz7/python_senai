#34. Escreva um programa que peça ao usuário um número e 
# verifique se ele é positivo, negativo ou zero.

numero = int(input('escolha seus numeros: \n'))

if (numero >= 1):
    print('seu numero e positivo')
elif (numero == 0):
    print('seu numero e zero')
elif (numero <= -1):
    print('seu numero e negativo')