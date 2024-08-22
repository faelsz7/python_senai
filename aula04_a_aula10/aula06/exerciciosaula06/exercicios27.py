#Crie um programa que solicite ao usuário três números e exiba o maior deles.

numero1 = int(input('coloque seu primeiro numero: \n'))
numero2 = int(input('coloque seu segundo numero: \n'))
numero3 = int(input('coloque seu terceiro numero: \n'))

if numero1 > numero2 > numero3:
    print(f'{numero1} e maior que { numero2} e do numero {numero3}')
elif numero1 < numero2 < numero3:
    print(f'{numero3} e maior que { numero2} e do numero {numero1}')
elif numero1 < numero2 > numero3:
    print(f'{numero2} e maior que { numero1} e do numero {numero3}')
elif numero1 > numero2 < numero3:
    print(f'{numero2} e maior que { numero1} e do numero {numero3}')

