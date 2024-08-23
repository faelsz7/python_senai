#Crie um programa que solicite ao usuário um número
#  de 1 a 12 e exiba o mês correspondente.

mes = int(input('informe um numero de 1 a 12: \n'))

if (mes == 1):
    print('janeiro')
elif (mes == 2):
    print('fevereiro')
elif (mes == 3):
    print('março')
elif (mes == 4):
    print('abril')
elif (mes == 5):
    print('maio')
elif (mes == 6):
    print('junho')
elif (mes == 7):
    print('julho')
elif (mes == 8):
    print('agosto')
elif (mes == 9):
    print('setembro')
elif (mes == 10):
    print('outubro')
elif (mes == 11):
    print('novembro')
elif (mes == 12):
    print('dezembro')
else:
    print('invalido')