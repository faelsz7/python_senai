#35. Desenvolva um algoritmo que peça ao usuário para digitar dois 
#números e verifique se a multiplicação deles é igual a 20.

numero1 = int(input('escreva o primeiro numero: \n'))
numero2 = int(input('escreva o segundo numero: \n'))

resultado = numero1 * numero2

if resultado == 20:
    print('seu numero e igual a 20.')
else:
    print('seu numero nao e igual a 20')
    