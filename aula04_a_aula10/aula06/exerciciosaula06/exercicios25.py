#Escreva um programa que peça ao usuário
#  um número de 0 a 20 e verifique se ele está entre 10 e 15.

numero = int(input('escolha um numero de 0 a 20: \n'))

if (numero >= 10 and numero <= 15):
    print('o numero esta entre 10 a 15')
elif ( numero >= 0 and numero <= 20):
    print('o numero nao esta entre 10 e 15')
else:
    print('numero invalido')
