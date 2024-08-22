#22. Escreva um programa que peça ao usuário para inserir dois números
# e verifique se o primeiro é maior que o segundo.



numero1 = int(input('coloque o primeiro numero: \n'))
numero2 = int(input('coloque o segundo numero: \n'))

if numero1 >= numero2:
    print(f'O numero {numero1} é maior que o numero {numero2}')
elif numero1 <= numero2:
    print(f'O numero {numero1} é menor que o numero {numero2}')