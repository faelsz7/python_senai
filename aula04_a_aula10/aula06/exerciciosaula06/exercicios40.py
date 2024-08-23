#40. Escreva um programa que peça ao usuário para inserir 
#três números e verifique se todos são iguais.

numero1 = int(input('coloque o primeiro numero:'))
numero2 = int(input('coloque o segundo numero:'))
numero3 = int(input('coloque o terceiro numero:'))

if (numero1 == numero2 == numero3):
    print('todos os numeros sao igual')
else:
    print('correto')
    