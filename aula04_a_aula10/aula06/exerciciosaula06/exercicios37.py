#Desenvolva um algoritmo que peça ao usuário para digitar um número 
# e verifique se ele é múltiplo de 2 ou de 5.

numero = int(input('coloque um numero multiplo de 2 ou 5: \n'))

if numero % 2 == 0:
    print("o numero e multiplo de 2.")
elif numero % 5 == 0: 
    print("o numero e multiplo de 5.")
else:
    print('o numero nao e multiplo de 5, 3')