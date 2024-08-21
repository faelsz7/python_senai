numero1 = 10
numero2 = 10

#operador maior
print(numero1 > numero2)#maior
print(numero2 > numero1)
#operador menor
print(numero1 < numero2)#menor
print(numero2 < numero1)

print(numero1 == numero2)#igual
print(numero1 >= numero2)#maior ou igual
print(numero1 <= numero2)#menos ou igual
print(numero1 != numero2)#diferente

idade = int(input('informe sua idade: \n'))

if (idade >= 112):
    print('invalido')
elif(idade > 18):
    print('maior de idade')
elif(idade < 0):
    print('invalido')
else:
    print('menor de idade')
if (idade <= 17):
    |print('menor de idade')| tambem funcionaria :)

idade = int(input('informe sua idade: \n'))

if (idade >= 18):
    print('pode assistir')
elif(idade >= 16):
    acompanhado = input('Esta acompanhado de adulto. sim ou nao? \n')
    if (acompanhado == 'sim'):
        print('pode assistir')
    else:
        print('nao pode assistir')
else:
    print('nao pode assistir')  
 
-----------------------encurtando-----------------------

idade = int(input('informe sua idade: \n'))

if (idade < 18):
    acompanhado =input('Esta acompanhado de adulto. sim ou nao? \n')
    if (acompanhado == 'sim'):
        print('pode assistir')
    else:
        print('nao pode assistir')
else:
    print('pode asssistir')
-----------tabela verdade (end)--------------
alladin = input('Alladin apareceu? \n')
jasmine = input('Jasmine apareceu? \n')

if (alladin == "sim") and (jasmine == "sim"):
    print("Love a noite toda")
else:
    print('Não rolou encontro')
----------- tabela or (ou)--------------

alladin = input('Alladin apareceu? \n')
jasmine = input('Jasmine apareceu? \n')

if (alladin == "sim") or (jasmine == "sim"):
    print("Love a noite toda")
else:
    print('Não rolou encontro')

alladin = input('Alladin apareceu? \n')
jasmine = input('Jasmine apareceu? \n')

if not((alladin == "sim") or (jasmine == "sim")):
    print("Love a noite toda")
else:
    print('Não rolou encontro')

