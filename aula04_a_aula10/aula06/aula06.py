#candidato = int(input('informe o numero do candidato \n'))
#
#if candidato ==13:
#    print('voutou no lua \n')
#elif candidato == 22:
#    print('votou no mito \n')
#else:
#    print('candidato invalido \n')
#
#candidato = int(input('informe o numero do candidato \n'))
#
#match candidato:
#    case 13:
#        print('voutou no lula')
#    case 22:
#        print('votou no mito')
#    case _:
#        print('invalido')
#
#--------------------------------------------------------------------
#atribuir valores a uma variavel
#
#numero = 10
#print(numero)
#
#numero += 10
#print (numero)
#
##numero = numero - 10
#numero -= 10
#print(numero)
#
##numero = numero * 10
#numero *= 10
#print(numero)
#
##numero = numero / 10
#numero /= 10
#print(numero)
#
#verificando se o numero e par ou impar
#
#numero = int(input('informe se o numero e par ou impar \n'))
#
#if numero % 2 == 0:
#    print('numero e par')
#else:
#    print('numero e impar')
#------------------------------------ao inves de prestar atençao na aula----------------------------------
#numero = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
#
#numero *= 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
#print(numero)
#
#numero += 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
#print(numero)
#----------------------------------------lacos de repetiçao for em portugues 'para'-------------------------------------------------------------------

#for i in range(5):
#    print(i)

#---------------------------------------------Listas-------------------------------------------------
#
#nomes = ['Luciano', 'Lucas', 'Raphael', 'Jamilly', 'Rebeca']
#print(nomes[2])
#
#
##for pessoa in nomes:
##    print(pessoa)
#
#frutas = ['goiaba', 'maçã', 'morango', 'abacate', 'laranga']
#print(frutas[0])
#
##for fruta in frutas:
##    print(fruta)
#
#for indice, fruta in enumerate(frutas):
#    print(f'sua fruta e {indice} - {fruta} ')

#------------------------lista que salva nome por nome--------------------------

#nomes = []
#
#for i in range(5):
#    nome = input('informe seu nome: \n')
#    nomes.append(nome) 
#
#for nome in nomes:
#    print(nome)
#
#print(nomes)
#----------------------comando que soletra o nome escrito-------------------------
#nome = 'raphael'
#
#for i in nome:
#    print(i)

#--------------------proximo laço de repetiçao---------------

#while em portugues enquanto

#numero = None #=(vazio)
#
#while numero != 0:
#    numero = int(input('informe um numero\n'))
#
#contador = 1
#numero = int(input('informe o numero:\n'))
#
#while contador <10:
#    print(numero * 2)
#    contador +=1

numero = 10
while True:
    numero *= 10
    print(numero)
    if numero > 100000001:
        break