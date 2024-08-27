#numero1 = int(input('informe o numero: \n'))
#numero2 = int(input('informe o numero: \n'))
#
#print('a soma e: ', numero1 + numero2)
#
#
#numeros = [1,5,74,7,999,24,87,100]
#
#print(max(numeros))# ve maior numero da lista
#print(min(numeros)) #ver o menor numero da lista
#print(len(numeros)) # ve a quantidades de objetos na lista
#print(len('raphael'))# conta a quantidade de caracteres
#print(sum(numeros))# soma tudo
#
#media = sum(numeros) / len(numeros)  
#--------------------------------------recebe uma lista e calcula a media---------------------------------------
#print(media)
#
#def media (numeros):
#    resultado = sum(numeros) / len(numeros)
#    return resultado
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------funcao de soma-----------------------
#def soma (numero1 , numero2):
#    soma = numero1 + numero2
#    return soma
#
#print(soma(1, 2))

#-----------------------------------------abreviando funçao-------------------------------------
#somar = lambda a, b: a + b
#
#print(somar(10, 5))
#
#--------------------------funçao de retorno-------------------------------
#def saudacao(nome):
#    print(f'ola {nome}')
#--------------------uso da funçao-------------------
#saudacao('raphael')

#funçao com parameto opcional
#def ola(nome, mensagem='Olá'):
#    print(mensagem , nome)
#
#ola('Raphael','Oi')
#ola('Raphael')
#
#funacao cm multiplo retorno
#--------------------------------funçao de multiplo retorno----------------------------
#def dividir (numero1 , numero2):
#    resposta = numero1 // numero2
#    resto = numero1 % numero2
#    return resposta, resto
#
#divisao, resto_divisao = dividir(9, 2)
#
#print(divisao)
#print(resto_divisao)
#
#numeros = [1,5,74,7,999,24,87,100]
#
#print(type(numeros))
#
#def exibir_informacoes(*args):
#    print('Argumentos posicionais:', args)
#
#exibir_informacoes(1,4, 'Raphael', 'Teste')
#
#
#def exibir_informacoes2(**args):
#    print('Argumentos nomeados:', args)
#
#exibir_informacoes2(nome= 'Raphael', idade =16 , curso ='python')
#------------------------chave: valor----------------------------------
#pessoas =[{
#    'nome': 'Raphael',
#    'idade': 16,
#    'estado_civil': 'enrolado',
#    'escolaridade': ' burro ',
#},
#{
#    'nome': 'Lucas',
#    'idade': 8,
#    'estado_civil': 'fudido',
#    'escolaridade': ' mais burro ainda ',
#}]
#
#print(pessoas[1])
